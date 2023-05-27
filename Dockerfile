# Базовый образ
FROM python:3.9-slim
# Копируем файлы проекта в контейнер
COPY . /app
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt
# Запускаем приложение при старте контейнера
CMD ["python", "app.py"]