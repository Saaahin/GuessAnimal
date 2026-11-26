from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
chat = client.chats.create(model="gemini-4-argon")  # общая память диалога
def check():
    prompt = f"""Проверь, подходит ли животное {guess} к твоему загаданному.
Если подходит, скажи «Вы победили!».
Если не подходит, скажи «Неверно» и дай новую, более информативную подсказку."""
    response = chat.send_message(prompt)
    print("Response:", response.text)
    return "Вы победили" in response.text
def start():
    global guess
    prompt = """Загадай случайное животное и играй со мной в «Угадай животное».
Описывай его постепенно, давая загадочные, косвенные подсказки, но никогда не называй
само животное или очевидные ключевые слова, связанные с ним. Например, если
ты загадал слона, не используй слова вроде «хобот», «большой», «Африка», «бивни»
и другие очевидные ассоциации. При неправильном ответе давай новую, более информативную
подсказку. Не повторяй подсказки. Начинай сразу с первой подсказки, не раскрывая
правила или ответ."""
    response = chat.send_message(prompt)
    print(response.text)
    while True:
        guess = input("What is your guess? - ")
        if check():
            break
print("\033[33m========= WELCOME =========\033[m")
print("\033[34mTo start the game, type \"START\" \033[m")
message = input()
if message == "START":
    start()






