from aiogram.fsm.state import StatesGroup, State


class UserStatus(StatesGroup):
	"""
	Класс для управления состояниями пользователя и администратора в процессе взаимодействия с ботом.
	"""
	picking_action = State()  #
