from classes.ai_client import AIClient
from models.question.question_orm_manager import QuestionORMManager


def test_analyze_text():
	ai_client = AIClient()
	print(ai_client.analyze_text("My favorit book is Harry Poter becouse it’s very exiting and have a lot of intresting characters. I like the way J.K. Rowling writed the story, it makes you feel like you are part of the magical world. Also, the book teach important lessons about frendship and courage. I already readed it three times and I always discover something new."))

def test_generate_question():
	ai_client = AIClient()
	new_question = ai_client.generate_question("books", "easy")
	print(new_question)
	orm_manager = QuestionORMManager()
	orm_manager.add(new_question)