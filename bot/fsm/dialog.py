from aiogram.fsm.state import StatesGroup, State


class DialogStates(StatesGroup):
    setting_price = State()
    creating_dialog = State()

