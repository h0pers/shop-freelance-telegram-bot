import re

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ValidPrice(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs) -> bool:
        return message.text.isnumeric()
