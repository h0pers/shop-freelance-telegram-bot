from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.config import MessageText
from bot.keyboards.inline import welcome_inline_keyboard

admin_start = Router()


@admin_start.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=MessageText.WELCOME_ADMIN_TEXT.format(username=message.from_user.username or message.from_user.first_name))
