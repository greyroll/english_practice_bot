from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from loguru import logger

from handlers.user_status import UserStatus
from config import welcome_message
from funcs import create_keyboard



class UserHandlers:

	@staticmethod
	async def start_command(message: Message, state: FSMContext):

		"""
		Обрабатывает команду /start, предлагает пользователю выбрать день и переводит его в состояние выбора дня.
		"""

		await message.answer(
			text=welcome_message,
			reply_markup=create_keyboard(["Practice"])
		)
		await state.set_state(UserStatus.picking_action)
		logger.info(f"User {message.from_user.id} was offered to choose action")
		logger.info(f"User {message.from_user.id} status was changed to {await state.get_state()}")

	@staticmethod
	async def start_practice(message: Message, state: FSMContext):
		pass


