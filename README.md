# AI_consultant

Образ:
https://drive.google.com/file/d/15VMiQCMh1qRq7PVNVHzKmXFBgExk0vqh/view?usp=drive_link

Запуск:
docker load -i C:\Bot_reviews\my_bot_image.tar
docker run -e OPENAI_API_KEY='' -e MODEL='' -v C:\Bot_reviews:/app my_bot_image

На вход передается text.txt - где каждая строка, это одно сообщение пользователя.
На выходе генерируется result.txt - где сохраняется сообщение и ответ.
