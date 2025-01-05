from flask_appbuilder import Model
from pygments.lexer import default
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean

class Todo(Model):
    id = Column(Integer, primary_key=True)
    entry = Column(String(100), unique=False, nullable=False)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"{self.id}, {self.entry}, {self.completed}"