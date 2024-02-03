from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.callback.welcome import WelcomeCallback
from bot.config import MessageText, openai_message

delivery_and_costs_router = Router()


@delivery_and_costs_router.callback_query(StateFilter(None), WelcomeCallback.filter(F.is_delivery_and_cost == 1))
async def delivery_and_cost_callback(query: CallbackQuery, callback_data: WelcomeCallback, state: FSMContext):
    openai_response = openai_message(message_text=MessageText.DELIVERY_AND_COSTS_BUTTON_TEXT)
    await query.message.reply(text=openai_response)
    await query.answer()
