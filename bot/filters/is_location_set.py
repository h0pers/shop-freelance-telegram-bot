from aiogram.filters import BaseFilter
from aiogram.types import Message, Location


class IsLocationSetFilter(BaseFilter):
    async def __call__(self, message: Message, *args, **kwargs):
        return message.location is not None
