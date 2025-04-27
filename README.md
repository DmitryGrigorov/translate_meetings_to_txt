# translate_meetings_to_txt

## Описание

Этот проект содержит скрипты для преобразования аудиофайлов в текст с использованием модели Whisper от OpenAI. Скрипты поддерживают различные форматы аудио и видео файлов и автоматически определяют, использовать ли GPU или CPU для обработки.

### Основные файлы

- **wavs_translate_to_text.py**: Основной скрипт для преобразования аудиофайлов в текст. Он загружает модель Whisper, обрабатывает файлы из указанной папки и сохраняет результаты в текстовом формате.
- **all_videos_to_files.py**: Скрипт для преобразования видеофайлов в аудиоформат WAV. Видео должны быть помещены в папку `./videos`.

### Требования

- Python 3.10.9
- Установленные зависимости из `requirements.txt`

### Установка

1. Клонируйте репозиторий.
2. Установите зависимости с помощью команды:
   ```
   pip install -r requirements.txt
   ```

### Использование

1. Поместите видеофайлы в папку `./videos`.
2. Запустите скрипт `all_videos_to_files.py`, чтобы преобразовать видео в формат WAV.
3. Переместите полученные аудиофайлы в папку `./wavs`.
4. Запустите скрипт `wavs_translate_to_text.py`:
   ```
   python wavs_translate_to_text.py
   ```
5. Результаты будут сохранены в папке `./wavs/results`.

---

## Description

This project contains scripts for converting audio files to text using the Whisper model from OpenAI. The scripts support various audio and video file formats and automatically determine whether to use GPU or CPU for processing.

### Main Files

- **wavs_translate_to_text.py**: The main script for converting audio files to text. It loads the Whisper model, processes files from the specified folder, and saves the results in text format.
- **all_videos_to_files.py**: A script for converting video files to WAV audio format. Videos should be placed in the `./videos` folder.

### Requirements

- Python 3.10.9
- Installed dependencies from `requirements.txt`

### Installation

1. Clone the repository.
2. Install the dependencies using the command:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Place video files in the `./videos` folder.
2. Run the `all_videos_to_files.py` script to convert videos to WAV format.
3. Move the resulting audio files to the `./wavs` folder.
4. Run the `wavs_translate_to_text.py` script:
   ```
   python wavs_translate_to_text.py
   ```
5. Results will be saved in the `./wavs/results` folder.



