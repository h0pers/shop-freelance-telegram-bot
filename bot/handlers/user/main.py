from aiogram import Router

from .start import start_router
from .cancel import cancel_action_router
from bot.middleware.collect_data import CollectData, CollectCallbackData

user_router = Router()

user_router.message.middleware(CollectData())


def get_user_router() -> Router:
    user_routers = (cancel_action_router, start_router,)
    user_router.include_routers(*user_routers)

    return user_router
