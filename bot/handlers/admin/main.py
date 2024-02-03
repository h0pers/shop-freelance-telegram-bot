from aiogram import Router
from .start import admin_start
from .dialog import dialog_router
from .price import price_router

from bot.filters.is_admin import OnlyAdmin, OnlyAdminCallback
from bot.middleware.collect_data import CollectData

admin_router = Router()

admin_router.message.filter(OnlyAdmin())
admin_router.callback_query.filter(OnlyAdminCallback())

admin_router.message.middleware(CollectData())


def get_admin_router() -> Router:
    admin_routers = (admin_start, dialog_router, price_router,)
    admin_router.include_routers(*admin_routers)
    return admin_router
