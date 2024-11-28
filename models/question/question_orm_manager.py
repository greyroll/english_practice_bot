from pathlib import Path

from sqlmodel import Session, create_engine, select

from models.question.question_model import QuestionModel


class QuestionORMManager:

	def __init__(self):

		project_root = Path(__file__).resolve().parent.parent  # Два уровня вверх от текущего файла
		db_path = project_root / 'english_bot.db'  # Путь к базе данных в корне проекта

		self.engine = create_engine(f"sqlite:///{db_path}")

	def fetch_all(self) -> list[QuestionModel]:

		with Session(self.engine) as session:
			statement = select(QuestionModel)
			questions = list(session.exec(statement).fetchall())
		return questions

	def add(self, question: QuestionModel):

		with Session(self.engine) as session:
			session.add(question)
			session.commit()
			session.refresh(question)

	def add_all(self, questions: list[QuestionModel]):

		with Session(self.engine) as session:
			session.add_all(questions)
			session.commit()
			for question in questions:
				session.refresh(question)

	def create_table(self):
		"""
		Создаёт таблицу расписания в базе данных, если она еще не существует.
		"""
		QuestionModel.metadata.create_all(self.engine)

	# def fetch_by_id(self, appointment_id) -> AppointmentModel | None:
	# 	"""
	# 	Извлекает запись о встрече по уникальному идентификатору (appointment_id).
	#
	# 	:param appointment_id: int
	# 	:return: AppointmentModel, если запись найдена, или None, если запись не существует.
	# 	"""
	# 	with Session(self.engine) as session:
	# 		statement = select(AppointmentModel).where(AppointmentModel.appointment_id == appointment_id)
	# 		appointment = session.exec(statement).one_or_none()
	# 	return appointment
	#
	# def fetch_by_day_time(self, day: str, time: str) -> AppointmentModel | None:
	# 	"""
	# 	Извлекает запись о встрече на основе заданного дня и времени.
	#
	# 	:param day: str
	# 	:param time: str
	# 	:return: AppointmentModel, если запись найдена, или выдаает ValueError, если запись не существует.
	# 	"""
	# 	with Session(self.engine) as session:
	# 		statement = select(AppointmentModel).where(AppointmentModel.day == day, AppointmentModel.time == time)
	# 		appointment = session.exec(statement).one_or_none()
	# 	if appointment is None:
	# 		raise ValueError(f"No appointment found for day: {day} and time: {time}")
	# 	return appointment
	#
	# def fetch_available(self) -> list[AppointmentModel]:
	# 	"""
	# 	Извлекает все доступные для бронирования записи (is_available == 1).
	#
	# 	:return: list[AppointmentModel]
	# 	"""
	# 	with Session(self.engine) as session:
	# 		statement = select(AppointmentModel).where(AppointmentModel.is_available == 1)
	# 		appointments = session.exec(statement).fetchall()
	# 	return list(appointments)
	#
	# def fetch_unavailable(self) -> list[AppointmentModel]:
	# 	"""
	# 	Извлекает все забронированные записи (is_available == 0).
	#
	# 	:return: list[AppointmentModel]
	# 	"""
	# 	with Session(self.engine) as session:
	# 		statement = select(AppointmentModel).where(AppointmentModel.is_available == 0)
	# 		appointments = session.exec(statement).fetchall()

	# 	return list(appointments)
	#
	#

	#
	# def update(self, appointment: AppointmentModel):
	# 	"""
	# 	Обновляет данные существующей записи в базе данных.
	#
	# 	:param appointment: AppointmentModel
	# 	"""
	# 	with Session(self.engine) as session:
	# 		statement = select(AppointmentModel).where(AppointmentModel.appointment_id == appointment.appointment_id)
	# 		results = session.exec(statement)
	# 		appointment_model = results.one()
	#
	# 		appointment_model.is_available = int(appointment.is_available)
	# 		appointment_model.user_id = appointment.user_id
	# 		appointment_model.user_name = appointment.user_name
	#
	# 		session.add(appointment_model)
	# 		session.commit()
	#
	# def remove(self, appointment_id: int):
	# 	"""
	# 	Удаляет запись по id.
	#
	# 	:param appointment_id: int
	# 	"""
	# 	with Session(self.engine) as session:
	# 		statement = select(AppointmentModel).where(AppointmentModel.appointment_id == appointment_id)
	# 		results = session.exec(statement)
	# 		appointment_model = results.one()
	# 		if appointment_model is None:
	# 			print(f"Appointment {appointment_id} is not found")
	# 		else:
	# 			session.delete(appointment_model)
	# 		session.commit()


