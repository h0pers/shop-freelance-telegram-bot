from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery

from bot.callback.welcome import WelcomeCallback
from bot.config import MessageText, openai_message

help_to_choose_type_router = Router()


@help_to_choose_type_router.callback_query(StateFilter(None), WelcomeCallback.filter(F.is_help_to_choose_sport == 1))
async def delivery_and_cost_callback(query: CallbackQuery, callback_data: WelcomeCallback):
    open_ai_query_data = openai_message(message_text='Помоги мне выбрать сорт')
    await query.message.reply(text=open_ai_query_data)
    await query.answer()
