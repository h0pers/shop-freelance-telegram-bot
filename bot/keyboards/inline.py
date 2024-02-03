from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.callback.dialog import DialogCallback
from bot.config import MessageText, PAYMENT_LINK
from bot.callback.welcome import WelcomeCallback


class Inline:
    inline_buttons: List[List[InlineKeyboardButton]]
    markup: InlineKeyboardMarkup

    def __init__(self, buttons_list: List[List[InlineKeyboardButton]]):
        self.inline_buttons = buttons_list

    def get_markup(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=self.inline_buttons)


delivery_and_costs_button = InlineKeyboardButton(text=MessageText.DELIVERY_AND_COSTS_BUTTON_TEXT,
                                                 callback_data=WelcomeCallback(is_delivery_and_cost=1).pack()
                                                 )

help_to_choose_sport_button = InlineKeyboardButton(text=MessageText.HELP_TO_CHOOSE_SPORT_BUTTON_TEXT,
                                                   callback_data=WelcomeCallback(is_help_to_choose_sport=1).pack()
                                                   )

payment_help_button = InlineKeyboardButton(text=MessageText.PAYMENT_HELP_BUTTON_TEXT,
                                           callback_data=WelcomeCallback(is_payment_help=1).pack()
                                           )

leave_dialog_button = InlineKeyboardButton(text=MessageText.LEAVE_DIALOG_BUTTON,
                                           callback_data=DialogCallback(user_chat_id=0,
                                                                        username='Удален',
                                                                        close_dialog=1).pack())

pay_button = InlineKeyboardButton(text='Оплатить', url=PAYMENT_LINK)
pay_inline_keyboard = Inline([[pay_button]])

welcome_inline_keyboard = Inline([[delivery_and_costs_button], [help_to_choose_sport_button], [payment_help_button]])
