# Используем официальный образ Python как базовый
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR ./

# Копируем файлы приложения в рабочую директорию
COPY main.py prompt.py text.txt ./

# Устанавливаем необходимые библиотеки
RUN pip install -r requirements.txt

# Определяем переменные окружения
ENV OPENAI_API_KEY=""
ENV MODEL=""

# Запускаем приложение
CMD ["python", "main.py"]
