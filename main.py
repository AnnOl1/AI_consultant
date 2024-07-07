import openai
import os
import prompt
from openai import OpenAI

# Ваши ключи API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL")

openai.api_key = OPENAI_API_KEY

def process_messages():
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        # Чтение сообщений из файла text.txt
        with open('text.txt', 'r', encoding='utf-8') as file:
            messages = file.readlines()
        
        # Открываем файл для записи результатов
        with open('result.txt', 'w', encoding='utf-8') as result_file:
            for user_message in messages:
                try:
                    completion = client.chat.completions.create(
                        model=MODEL,
                        temperature=1,
                        messages=[
                            {"role": "system", "content": prompt.condiitions},
                            {"role": "user", "content": user_message.strip()}
                        ]
                    )
                    response_message = completion.choices[0].message.content
                    result_file.write(f"Отзыв: {user_message.strip()}\nОтвет: {response_message}\n\n")
                except Exception as e:
                    result_file.write(f"Отзыв: {user_message.strip()}\nОшибка: {e}\n\n")
    except Exception as e:
        print(f'Произошла ошибка: {e}')

# Запуск обработки сообщений
if __name__ == '__main__':
    process_messages()
