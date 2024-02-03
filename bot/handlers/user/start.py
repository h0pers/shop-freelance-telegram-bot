from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.config import MessageText
from bot.keyboards.inline import welcome_inline_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=MessageText.WELCOME_TEXT, reply_markup=welcome_inline_keyboard.get_markup())
