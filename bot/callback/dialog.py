from aiogram.filters.callback_data import CallbackData


class DialogCallback(CallbackData, prefix="application"):
    user_chat_id: int = None
    username: str = None
    create_dialog: int = 0
    close_dialog: int = 0
    set_price: int = 0
