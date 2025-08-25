# translate_meetings_to_txt

## Description

This project is designed for **automatic conversion of meeting video and audio recordings to text** using OpenAI's Whisper model. The scripts support various audio and video file formats and automatically determine whether to use GPU or CPU for processing.

**Main Goal:** Convert video files from meetings/recordings into readable text documents

**Workflow:**
1. Video/audio files are placed in `videos_and_records/` folder
2. Conversion to WAV audio format
3. Files are moved to `wavs/` folder
4. Processing through Whisper model
5. Results are saved in `wavs/results/` as TXT and SRT files

> **Note:** If you are using an NVIDIA graphics card and want faster processing, you need to install the CUDA driver: [CUDA Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_network)

### Main Files

- **wavs_translate_to_text.py**: The main script for converting audio files to text. It loads the Whisper model, processes files from the specified folder, and saves the results in text format.
- **all_videos_to_wav.py**: A script for converting video files to WAV audio format. Videos should be placed in the `./videos_and_records` folder.
- **wavs_to_txt_with_speaker_indetification.py**: Enhanced version with speaker identification functionality.
- **check_cuda.py**: A utility script to check if CUDA (GPU support) is available and properly configured on your system. This helps ensure that your environment is set up to use GPU acceleration for faster processing with the Whisper model. Running this script before processing large files can help you verify that your setup will utilize the GPU, avoiding slower CPU-only processing.

### Purpose of the Scripts

These two scripts are designed to automate the process of converting video files into text:

1. **`all_videos_to_wav.py`**: Converts video files into WAV audio format. Videos should be placed in the `./videos_and_records` folder. After running the script, the audio files are saved in WAV format, ready for further processing.

2. **`wavs_translate_to_text.py`**: Uses the Whisper model from OpenAI to convert audio files (in WAV format) into text. It processes files from the `./wavs` folder and saves the results as text files in the `./wavs/results` folder.

Together, these scripts streamline the process of transforming video files into text documents.

### Requirements

- Python 3.10.9
- Installed dependencies from `requirements.txt`


### Installation

1. Clone the repository.
2. If you are using Windows 11, install ffmpeg using PowerShell (open PowerShell as Administrator):
   ```
   winget install --id=Gyan.FFmpeg --source=winget
   ```
3. (Recommended for Win10/11) Create and activate a virtual environment:
   ```
   python -m venv venv
   .\.venv\Scripts\activate.bat
   ```
4. Install the dependencies:
   ```
   pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install openai-whisper tqdm python-dotenv resemblyzer scikit-learn numpy
   ```
5. (Optional, but recommended) Install all dependencies from requirements.txt as a final step:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Place video and audio files in the `./videos_and_records` folder.
2. (Optional but recommended) Run `check_cuda.py` to verify that your system can use GPU acceleration:
   ```
   python check_cuda.py
   ```
   If CUDA is available, you will see a confirmation message. If not, follow the instructions to install or configure CUDA for optimal performance.
3. Run the `all_videos_to_wav.py` script to convert videos to WAV format:
   ```
   python all_videos_to_wav.py
   ```
4. Move the resulting audio files to the `./wavs` folder.
5. Run the `wavs_translate_to_text.py` script:
   ```
   python wavs_translate_to_text.py
   ```
6. Results will be saved in the `./wavs/results` folder.

---

### Russian Version

# translate_meetings_to_txt

## Описание

Этот проект предназначен для **автоматического преобразования видео и аудио записей встреч в текст** с использованием модели Whisper от OpenAI. Скрипты поддерживают различные форматы аудио и видео файлов и автоматически определяют, использовать ли GPU или CPU для обработки.

**Основная цель:** Конвертировать видеофайлы встреч/записей в читаемые текстовые документы

**Workflow:**
1. Видео/аудио файлы размещаются в папке `videos_and_records/`
2. Конвертация в аудио WAV формат
3. Файлы перемещаются в папку `wavs/`
4. Обработка через модель Whisper
5. Результаты сохраняются в `wavs/results/` как TXT и SRT файлы

> **Примечание:** Если вы используете видеокарту NVIDIA и хотите более быструю обработку, необходимо установить драйвер CUDA: [CUDA Downloads](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_network)

### Основные файлы

- **wavs_translate_to_text.py**: Основной скрипт для преобразования аудиофайлов в текст. Он загружает модель Whisper, обрабатывает файлы из указанной папки и сохраняет результаты в текстовом формате.
- **all_videos_to_wav.py**: Скрипт для преобразования видеофайлов в аудиоформат WAV. Видео должны быть помещены в папку `./videos_and_records`.
- **wavs_to_txt_with_speaker_indetification.py**: Улучшенная версия с функциональностью идентификации спикеров.
- **check_cuda.py**: Вспомогательный скрипт для проверки наличия и корректной настройки CUDA (поддержки GPU) на вашей системе. Это позволяет убедиться, что ваша среда готова использовать ускорение на GPU для более быстрой обработки с помощью модели Whisper. Рекомендуется запускать этот скрипт перед обработкой больших файлов, чтобы убедиться, что будет использоваться GPU, а не только CPU.

### Назначение скриптов

Эти два скрипта предназначены для автоматизации процесса перевода видеофайлов в текст:

1. **`all_videos_to_wav.py`**: Конвертирует видеофайлы в аудиоформат WAV. Видео должны быть помещены в папку `./videos_and_records`. После выполнения скрипта аудиофайлы сохраняются в формате WAV, готовые для дальнейшей обработки.

2. **`wavs_translate_to_text.py`**: Использует модель Whisper от OpenAI для преобразования аудиофайлов (в формате WAV) в текст. Он обрабатывает файлы из папки `./wavs` и сохраняет результаты в текстовом формате в папке `./wavs/results`.

Таким образом, оба скрипта работают вместе, чтобы преобразовать видеофайлы в текстовые документы.

### Требования

- Python 3.10.9
- Установленные зависимости из `requirements.txt`


### Установка

1. Клонируйте репозиторий.
2. Если у вас Windows 10/11, установите ffmpeg через PowerShell (откройте PowerShell от имени администратора):
   ```
   winget install --id=Gyan.FFmpeg --source=winget
   ```
3. (Рекомендуется в Win10/11) Создайте и активируйте виртуальное окружение:
   ```
   python -m venv venv
   .\.venv\Scripts\activate.bat
   ```
4. Установите зависимости:
   ```
   pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install openai-whisper tqdm python-dotenv resemblyzer scikit-learn numpy
   ```
5. (Опционально, но рекомендуется) Установите все зависимости из requirements.txt завершающим шагом:
   ```
   pip install -r requirements.txt
   ```

### Использование

1. Поместите видеофайлы и аудиозаписи в папку `./videos_and_records`.
2. (Опционально, но рекомендуется) Запустите `check_cuda.py`, чтобы убедиться, что ваша система может использовать ускорение на GPU:
   ```
   python check_cuda.py
   ```
   Если CUDA доступна, вы увидите соответствующее сообщение. Если нет, следуйте инструкциям по установке или настройке CUDA для оптимальной производительности.
3. Запустите скрипт `all_videos_to_wav.py`, чтобы преобразовать видео в формат WAV:
   ```
   python all_videos_to_wav.py
   ```
4. Переместите полученные аудиофайлы в папку `./wavs`.
5. Запустите скрипт `wavs_translate_to_text.py`:
   ```
   python wavs_translate_to_text.py
   ```
6. Результаты будут сохранены в папке `./wavs/results`.