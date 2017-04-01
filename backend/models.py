
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desired_grade = Column(Integer) # from 1 to 10
    subjects = relationship('Subjects')

    def __repr__():
        return str(self.name)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hours = Column(Integer)
    difficulty = Column(Integer) # from one to 10
    grade = Column(Integer)

    def __repr__():
        return str(self.name

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String(255))

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)