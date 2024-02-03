from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

cancel_action_router = Router()


@cancel_action_router.message(Command('cancel'))
async def cancel_action(message: Message, state: FSMContext):
    await message.answer(text='Вы успешно отменили действие', reply_markup=ReplyKeyboardRemove())
    await state.clear()
