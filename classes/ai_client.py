from openai import OpenAI

from models.question.question_model import QuestionModel
from secret import OPENAIKEY


class AIClient:

	def __init__(self):
		self.client = OpenAI(api_key=OPENAIKEY)

	def analyze_text(self, text: str, question: QuestionModel = None) -> str:
		system_message = "You are an English grammar checker and teacher. Your job is to help the user improve their writing skills."

		# Формируем запрос с вопросом и ответом пользователя
		user_message = (
			f"Here is the question the user was asked: '{question.question}'.\n"
			f"Difficulty: '{question.difficulty}'.\n"
			f"The user's response is: '{text}'.\n"
			"Please check the response for grammar and lexical errors, "
			"and provide feedback with corrections and explanations."
		) if question else (
			f"Check the text for grammar and lexical errors: '{text}'"
			"Please check the response for grammar and lexical errors, "
			"and provide feedback with corrections and explanations."
		)

		chat_completion = self.client.chat.completions.create(
			messages=[
				{"role": "system", "content": system_message},
				{"role": "user", "content": user_message}
			],
			model="gpt-4o",
		)
		response = chat_completion.choices[0].message.content
		return response

	def generate_question(self, category=None, difficulty="medium"):
		# Формируем системное сообщение и контекст
		system_message = "You are an assistant that creates questions for practicing English writing skills."
		user_message = f"Generate a {difficulty} level writing question for English learners." \
						"Return question only."

		if category:
			user_message += f" The question should be about the topic: {category}."

		chat_completion = self.client.chat.completions.create(
			model="gpt-4o",
			messages=[
				{"role": "system", "content": system_message},
				{"role": "user", "content": user_message}
			]
		)

		question = chat_completion.choices[0].message.content
		question = question.strip('\"')
		question_model = QuestionModel(question=question, difficulty=difficulty, category=category)
		return question_model
