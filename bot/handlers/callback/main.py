from aiogram import Router

from .delivery_and_costs import delivery_and_costs_router
from .payment_help import payment_help_router
from .help_to_choose_sport import help_to_choose_type_router
from bot.middleware.collect_data import CollectCallbackData

callback_router = Router()

callback_router.callback_query.middleware(CollectCallbackData())


def get_callback_router() -> Router:
    callback_routers = (delivery_and_costs_router, payment_help_router, help_to_choose_type_router,)
    callback_router.include_routers(*callback_routers)

    return callback_router
