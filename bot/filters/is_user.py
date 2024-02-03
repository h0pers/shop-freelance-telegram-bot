from aiogram.filters import BaseFilter
from aiogram.types import Message

from bot.config import ADMINS


class OnlyUser(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs) -> bool:
        for admin_id in ADMINS:
            if message.from_user.id != admin_id:
                return True

        return False
