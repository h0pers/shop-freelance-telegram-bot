from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, Message

from bot.callback.dialog import DialogCallback
from bot.config import MessageText, openai_message, ADMINS
from bot.database.methods.get import get
from bot.database.models.user import User
from bot.filters.is_user import OnlyUser
from bot.keyboards.inline import Inline
from bot.database.main import SessionLocal

other_router = Router()


@other_router.message(OnlyUser())
async def user_send_message(message: Message, bot: Bot, state: FSMContext):
    create_dialog_button = InlineKeyboardButton(text=MessageText.CREATE_DIALOG_BUTTON_TEXT,
                                                callback_data=DialogCallback(user_chat_id=message.from_user.id,
                                                                             username=message.from_user.username or '',
                                                                             create_dialog=1).pack()
                                                )
    change_price_button = InlineKeyboardButton(text=MessageText.SET_PRICE_BUTTON_TEXT,
                                               callback_data=DialogCallback(user_chat_id=message.from_user.id,
                                                                            username=message.from_user.username or '',
                                                                            set_price=1).pack()
                                               )

    async with SessionLocal.begin() as session:
        user = (await get(session, User, telegram_id=message.from_user.id)).scalar()

    if not user.in_dialog:
        data = await state.get_data()
        openai_response = openai_message(message_text=message.text)
        dialog = f'Пользователь: {message.text}. BOT:{openai_response}'
        await state.update_data({"dialog": f'{data.get("dialog")}\n{dialog}'})
        await message.reply(text=openai_response)

        for admin_id in ADMINS:
            await bot.send_message(chat_id=admin_id,
                                   text=MessageText.USER_SEND_MESSAGE_TEXT.format(
                                       username=message.from_user.username or message.from_user.first_name,
                                       message=dialog or 'Не является текстом'
                                   ),
                                   reply_markup=Inline([[create_dialog_button], [change_price_button]]).get_markup()
                                   )
        return
    for admin_id in ADMINS:
        await bot.send_message(chat_id=admin_id,
                               text=MessageText.DIALOG_MESSAGE_FROM_USER.format(username=message.from_user.username,
                                                                                message=message.text
                                                                                ))
