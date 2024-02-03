from typing import Tuple

from aiogram import Router

from .user.main import get_user_router
from .admin.main import get_admin_router
from .callback.main import get_callback_router
from .other import other_router


def get_all_routers() -> Tuple[Router]:
    return get_admin_router(), get_user_router(), get_callback_router(), other_router
