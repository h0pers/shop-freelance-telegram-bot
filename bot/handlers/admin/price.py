from aiogram import Router, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.config import MessageText
from bot.database.main import SessionLocal
from bot.database.methods import update
from bot.database.methods.get import get
from bot.database.models.user import User
from bot.filters.is_admin import OnlyAdmin
from bot.filters.valid_price import ValidPrice
from bot.fsm.dialog import DialogStates
from bot.callback.dialog import DialogCallback
from bot.keyboards.inline import Inline, leave_dialog_button

price_router = Router()


@price_router.callback_query(StateFilter(None), DialogCallback.filter(F.set_price == 1))
async def set_price(query: CallbackQuery, callback_data: DialogCallback, state: FSMContext):
    await state.set_state(DialogStates.setting_price)
    await state.update_data({'dialog_chat_id': callback_data.user_chat_id, 'dialog_username': callback_data.username})
    await query.message.reply(text=MessageText.SET_PRICE_TEXT)


@price_router.message(StateFilter(DialogStates.setting_price), ValidPrice())
async def handle_price_message(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    price_successful_text = MessageText.PRICE_SUCCESSFUl_SET.format(price=message.text)
    await message.answer(text=price_successful_text)
    await bot.send_message(chat_id=data['dialog_chat_id'], text=price_successful_text)
