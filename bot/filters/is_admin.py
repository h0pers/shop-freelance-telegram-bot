from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from bot.config import ADMINS


class OnlyAdmin(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs):
        for admin_id in ADMINS:
            if message.from_user.id == admin_id:
                print(message.from_user.id)
                print(admin_id)
                return True

        return False


class OnlyAdminCallback(BaseFilter):
    async def __call__(self, query: CallbackQuery, *args, **kwargs):
        for admin_id in ADMINS:
            if query.from_user.id == admin_id:
                return True

        return False
