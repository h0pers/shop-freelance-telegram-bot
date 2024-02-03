from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.callback.welcome import WelcomeCallback
from bot.config import MessageText, openai_message
from bot.keyboards.inline import pay_inline_keyboard

payment_help_router = Router()


@payment_help_router.callback_query(StateFilter(None), WelcomeCallback.filter(F.is_payment_help == 1))
async def payment_help_callback(query: CallbackQuery, callback_data: WelcomeCallback, state: FSMContext):
    open_ai_query_data = openai_message(message_text='Расскажи подробности оплаты. Как оплатить. Условие.')
    await query.message.reply(text=open_ai_query_data, reply_markup=pay_inline_keyboard.get_markup())
    await query.answer()
