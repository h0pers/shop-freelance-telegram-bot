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
from bot.fsm.dialog import DialogStates
from bot.callback.dialog import DialogCallback
from bot.keyboards.inline import Inline, leave_dialog_button

dialog_router = Router()


@dialog_router.callback_query(StateFilter(None), DialogCallback.filter(F.create_dialog == 1))
async def create_dialog(query: CallbackQuery, callback_data: DialogCallback, state: FSMContext):
    async with SessionLocal.begin() as session:
        user = (await get(session, User, telegram_id=callback_data.user_chat_id)).scalar()
        user.in_dialog = True

    await state.set_state(DialogStates.creating_dialog)
    await state.update_data({'dialog_chat_id': callback_data.user_chat_id, 'dialog_username': callback_data.username})
    await query.message.answer(text=MessageText.CREATE_DIALOG_TEXT,
                               reply_markup=Inline([[leave_dialog_button]]).get_markup())


@dialog_router.callback_query(StateFilter(DialogStates.creating_dialog), DialogCallback.filter(F.close_dialog == 1))
async def close_dialog(query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    async with SessionLocal.begin() as session:
        user = (await get(session, User, telegram_id=data['dialog_chat_id'])).scalar()
        user.in_dialog = False
    await query.message.edit_text(text=MessageText.DIALOG_CLOSE_TEXT.format(username=data['dialog_username']))
    await state.clear()


@dialog_router.message(StateFilter(DialogStates.creating_dialog))
async def dialog_message(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(chat_id=data['dialog_chat_id'],
                           text=MessageText.DIALOG_USER_NOTIFICATION.format(message=message.text))
