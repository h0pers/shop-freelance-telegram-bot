import os

from time import sleep
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.beta import Thread

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

BOT_TOKEN = os.getenv('BOT_TOKEN')

DB_URL = conn_url = f'postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}/{os.getenv("POSTGRES_DB")}'

OPEN_AI_API = os.getenv('OPEN_AI_API')

OPEN_AI_ASSISTANCE_ID = os.getenv('OPEN_AI_ASSISTANCE_ID')

OPEN_AI_CLIENT = OpenAI(api_key=OPEN_AI_API)

PAYMENT_LINK = 'https://taplink.cc/pattaya_amazon'

ADMINS = [int(admin.strip()) for admin in os.getenv('TELEGRAM_ADMIN_ID').split(',')]

print(ADMINS)


def openai_message(message_text: str) -> str:
    thread = OPEN_AI_CLIENT.beta.threads.create()
    message = OPEN_AI_CLIENT.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message_text
    )
    run = OPEN_AI_CLIENT.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=OPEN_AI_ASSISTANCE_ID,
    )
    while run.status != 'completed':
        sleep(0.5)
        run = OPEN_AI_CLIENT.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

    messages = OPEN_AI_CLIENT.beta.threads.messages.list(
        thread_id=thread.id,
    )
    return messages.data[0].content[0].text.value


class MessageText:
    WELCOME_TEXT = 'Привет! Я здесь, чтобы ответить на ваши вопросы, когда вы не можете найти меня рядом. Что бы вы хотели узнать?'
    WELCOME_ADMIN_TEXT = 'Приветствую вас <b>@{username}</b>. Добро пожаловать в панель администратора. Ожидайте новых аппликаций.'
    DELIVERY_AND_COSTS_BUTTON_TEXT = 'Доставка - стоимость и время?'
    HELP_TO_CHOOSE_SPORT_BUTTON_TEXT = 'Помогите выбрать сорт'
    PAYMENT_HELP_BUTTON_TEXT = 'Куда можно оплатить?'
    CREATE_DIALOG_BUTTON_TEXT = 'Начать диалог с пользователем'
    DIALOG_CLOSE_TEXT = 'Диалог с пользователем <b>@{username}</b> закрыт'
    SET_PRICE_BUTTON_TEXT = 'Установить цену'
    SET_PRICE_TEXT = 'Установите цену. Цена указываться в рублях и должна иметь такой формат: 5000'
    PRICE_SUCCESSFUl_SET = 'Цена на эту заявку установлена в {price}₽'
    CREATE_DIALOG_TEXT = 'Все сообщение ниже будут отправлены этому пользователю, для отмены воспользуйтесь кнопкой <b>Выйти из диалога</b>'
    LEAVE_DIALOG_BUTTON = 'Выйти из диалога'
    USER_SEND_MESSAGE_TEXT = '''
<b>У вас новое сообщение от пользователя @{username}</b>
<b>Сообщение:</b> 
<code>{message}</code>
'''
    DIALOG_USER_NOTIFICATION = '''
<b>Сообщение от администрации:</b>
<code>{message}</code>'''
    DIALOG_MESSAGE_FROM_USER = '''
Сообщение от <b>{username}</b>:
<code>{message}</code>
'''
