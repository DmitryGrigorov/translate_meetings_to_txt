import whisper
import os
import torch
import sys
import time
from dotenv import load_dotenv
from tqdm import tqdm
from datetime import timedelta
import traceback
import torchaudio
from resemblyzer import VoiceEncoder, preprocess_wav
from sklearn.cluster import KMeans
import numpy as np

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
extensions = (".wav", ".mp3", ".m4a", ".flac", ".ogg", ".mp4", ".avi", ".mov", ".mkv")
media_files = [f for f in os.listdir(folder_path) if f.lower().endswith(extensions)]

def find_optimal_clusters(embeddings, max_clusters=6):
    distortions = []
    embeddings = np.array(embeddings)

    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=0).fit(embeddings)
        distortions.append(kmeans.inertia_)  # inertia = сумма квадратов расстояний до центров кластеров

    # Ищем резкое уменьшение (первое сильное падение)
    deltas = np.diff(distortions)
    deltas2 = np.diff(deltas)

    # Если мало точек, по умолчанию 2
    if len(deltas2) == 0:
        return 2

    # Ищем максимум второго производного изменения
    optimal_clusters = np.argmin(deltas2) + 2  # +2 потому что дважды дифференцировали

    return optimal_clusters


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

encoder = VoiceEncoder()  # Загружаем один раз

for filename in tqdm(media_files, desc="Обработка файлов", ncols=100):
    try:
        file_path = os.path.join(folder_path, filename)
        print(f"\n🚀 Работаем с файлом: {filename}")

        # Распознавание текста через Whisper
        result = model.transcribe(file_path, word_timestamps=True, language=None)

        detected_language = result.get("language", "неизвестно")
        print(f"🌍 Определенный язык: {detected_language}")

        # Загрузка аудиофайла
        wav, sr = torchaudio.load(file_path)
        wav = wav.mean(dim=0).numpy()  # Переводим в моно
        wav = preprocess_wav(wav, source_sr=sr)

        # Получение эмбеддингов
        frames = encoder.embed_utterance(wav, return_partials=True)[1]

        # Кластеризация голосов
        optimal_speakers = find_optimal_clusters(frames, max_clusters=6) # Автоматически определяем количество спикеров
        print(f"🔍 Автоматически определено количество спикеров: {optimal_speakers}")

        kmeans = KMeans(n_clusters=optimal_speakers, random_state=0).fit(frames)

        speaker_labels = kmeans.labels_

        final_text = ""
        srt_content = ""
        srt_counter = 1

        for i, segment in enumerate(result['segments']):
            start_srt = format_timestamp_srt(segment['start'])
            end_srt = format_timestamp_srt(segment['end'])
            text = segment['text'].strip()
            speaker = speaker_labels[min(i, len(speaker_labels)-1)]  # На случай несоответствия длин

            # Для txt
            final_text += f"[{start_srt} - {end_srt}] Спикер {speaker}: {text}\n"

            # Для srt
            srt_content += f"{srt_counter}\n{start_srt} --> {end_srt}\nСпикер {speaker}: {text}\n\n"
            srt_counter += 1

        # Сохраняем .txt
        output_txt = os.path.splitext(filename)[0] + ".txt"
        with open(os.path.join(results_folder, output_txt), "w", encoding="utf-8") as f:
            f.write(final_text)

        # Сохраняем .srt
        output_srt = os.path.splitext(filename)[0] + ".srt"
        with open(os.path.join(results_folder, output_srt), "w", encoding="utf-8") as f:
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
