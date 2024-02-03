from aiogram.filters.callback_data import CallbackData


class WelcomeCallback(CallbackData, prefix="welcome"):
    is_delivery_and_cost: int = 0
    is_help_to_choose_sport: int = 0
    is_payment_help: int = 0
