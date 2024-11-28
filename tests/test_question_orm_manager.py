from models.question.question_model import QuestionModel
from models.question.question_orm_manager import QuestionORMManager

def test_create_table():
	orm_manager = QuestionORMManager()
	orm_manager.create_table()

def test_add_all():
	orm_manager = QuestionORMManager()
	orm_manager.add_all([
		QuestionModel(id=1, question="What is your favorite book and why?", difficulty="easy", category="books"),
		QuestionModel(question="Do you think technology makes our lives better or worse? Explain your opinion.", difficulty="hard", category="technology"),
		QuestionModel(question="What are the advantages and disadvantages of working remotely?", difficulty="hard", category="work"),
		QuestionModel(question="What is one skill you want to learn and why?", difficulty="easy", category="personality")
	])