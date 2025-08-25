import whisper
import os
import torch
import sys
import time
from dotenv import load_dotenv
from tqdm import tqdm
from datetime import timedelta
import traceback

# Загрузка .env переменных
load_dotenv()

# Проверка наличия CUDA
device = "cuda" if torch.cuda.is_available() else "cpu"

if device == "cuda":
    print("🚀 Найдена видеокарта! Работаем на CUDA.")
    model_name = "medium"
else:
    print("🖥️ CUDA не найдена. Работаем на процессоре (CPU).")
    model_name = "small"

# Загрузка модели Whisper
print(f"📦 Загружаем модель Whisper: {model_name}")
model = whisper.load_model(model_name).to(device)

# Путь к папке с файлами
folder_path = "./wavs"
results_folder = os.path.join(folder_path, "results")
os.makedirs(results_folder, exist_ok=True)

# Подключение лог-файла
log_file = open(os.path.join(results_folder, "log.txt"), "w", encoding="utf-8")
original_stdout = sys.stdout
sys.stdout = log_file

# Запуск таймера
start_time = time.time()

# Допустимые расширения
extensions = (
    ".wav", ".mp3", ".m4a", ".flac", ".ogg", ".mp4", ".avi",
    ".mov", ".mkv"
)
media_files = [f for f in os.listdir(folder_path)
               if f.lower().endswith(extensions)]


def format_timestamp_srt(seconds):
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    millis = int((seconds - total_seconds) * 1000)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


# Логи
successfully_processed = []
failed_files = []

for filename in tqdm(media_files, desc="Обработка файлов", ncols=100):
    try:
        file_path = os.path.join(folder_path, filename)
        print(f"\n🚀 Работаем с файлом: {filename}")

        # Распознавание текста через Whisper
        result = model.transcribe(file_path, word_timestamps=True,
                                  language="ru")

        detected_language = result.get("language", "неизвестно")
        print(f"🌍 Определенный язык: {detected_language}")

        final_text = ""
        srt_content = ""
        srt_counter = 1

        for segment in result['segments']:
            start_srt = format_timestamp_srt(segment['start'])
            end_srt = format_timestamp_srt(segment['end'])
            text = segment['text'].strip()

            # Для txt
            final_text += f"[{start_srt} - {end_srt}]: {text}\n"

            # Для srt
            srt_content += (f"{srt_counter}\n{start_srt} --> {end_srt}\n"
                            f"{text}\n\n")
            srt_counter += 1

        # Сохраняем .txt
        output_txt = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(results_folder, output_txt), "w",
                  encoding="utf-8") as f:
            f.write(final_text)

        # Сохраняем .srt
        output_srt = os.path.splitext(filename)[0] + ".srt"
        with open(os.path.join(results_folder, output_srt), "w",
                  encoding="utf-8") as f:
            f.write(srt_content)

        print(f"✅ Успешно сохранены файлы: {output_txt}, {output_srt}")
        successfully_processed.append(filename)

    except Exception as e:
        print(f"❌ Ошибка при обработке {filename}: {e}")
        traceback.print_exc()
        failed_files.append((filename, str(e)))

# Финальный отчет
print("\n🎯 Обработка завершена!")
print(f"\n✅ Успешно обработано файлов: {len(successfully_processed)}")
for f in successfully_processed:
    print(f" - {f}")

if failed_files:
    print(f"\n❌ Ошибки при обработке файлов: {len(failed_files)}")
    for f, err in failed_files:
        print(f" - {f}: {err}")

# Таймер обработки
end_time = time.time()
elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)
print(f"\n🕒 Общее время обработки: {minutes} мин {seconds} сек")

# Завершение логирования
sys.stdout = original_stdout
log_file.close()

print("\n📄 Лог работы сохранён в файл: results/log.txt")
print("✅ Все файлы успешно обработаны!")
