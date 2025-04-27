import os
import subprocess

# Папка с видеофайлами
input_folder = "./videos"
# Папка для сохранения wav файлов
output_folder = "./wavs"

# Создаем папку для wav файлов, если её нет
os.makedirs(output_folder, exist_ok=True)

# Поддерживаемые расширения видео
video_extensions = (".mp4", ".avi", ".mov", ".mkv")

# Проходим по всем файлам в папке
for filename in os.listdir(input_folder):
    if filename.lower().endswith(video_extensions):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(output_folder, output_filename)

        # Команда ffmpeg для конвертации
        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-ar", "16000",
            "-ac", "1",
            output_path
        ]

        print(f"🎬 Конвертация {filename} -> {output_filename}")
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

print("\n✅ Все видео успешно конвертированы в WAV!")
