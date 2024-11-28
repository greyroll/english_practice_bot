from sqlmodel import Field, SQLModel


class QuestionModel(SQLModel, table=True):
	__tablename__ = "questions"

	id: int | None = Field(default=None, primary_key=True)
	question: str
	difficulty: str
	category: str

	def __repr__(self):
		return (
			f"QuestionModel(id={self.id}, question='{self.question}', "
			f"difficulty='{self.difficulty}', category='{self.category}')"
		)


