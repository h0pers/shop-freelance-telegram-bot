import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.handlers.main import get_all_routers
from bot.database.models.main import register_models

from bot.config import BOT_TOKEN

dp = Dispatcher(storage=RedisStorage(Redis(host=os.getenv('REDIS_HOST'))))


async def on_startup(bot: Bot) -> None:
    await bot.delete_webhook()


async def start_bot():
    await register_models()
    dp.include_routers(*get_all_routers())
    dp.startup.register(on_startup)
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
