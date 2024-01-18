from sqlalchemy import Column, Integer, String


from database import Base

class Todo(Base):
    __tablename__ = "todos_prac"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
