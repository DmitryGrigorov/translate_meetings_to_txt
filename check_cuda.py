import torch

print("✅ PyTorch установлен. / ✅ PyTorch is installed.")
print("🔍 Проверка CUDA: / 🔍 Checking CUDA:")

if torch.cuda.is_available():
    print("🚀 CUDA доступна! / 🚀 CUDA is available!")
    print("🖥️ Устройство: / 🖥️ Device:", torch.cuda.get_device_name(0))
else:
    print("❌ CUDA недоступна. Используется CPU. / "
          "❌ CUDA is not available. Using CPU.")
    print(
        "\nЕсли вы все делали по инструкции и CUDA недоступен, "
        "выполните в терминале следующие команды:\n"
        "pip uninstall torch torchaudio -y\n"
        "pip install torch torchaudio --index-url "
        "https://download.pytorch.org/whl/cu118\n"
        "\nIf you followed the instructions and CUDA is not available, "
        "run the following commands in the terminal:\n"
        "pip uninstall torch torchaudio -y\n"
        "pip install torch torchaudio --index-url "
        "https://download.pytorch.org/whl/cu118\n"
    )
