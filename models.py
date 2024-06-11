from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Quiz(Base):
    __tablename__ = 'quizzes'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    # One-to-many relationship: A quiz can have multiple questions
    questions = relationship("Question", back_populates="quiz")

    def __repr__(self):
        return f"<Quiz(title='{self.title}')>"

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    answer = Column(String)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    
    # Many-to-one relationship: A question belongs to one quiz
    quiz = relationship("Quiz", back_populates="questions")

    def __repr__(self):
        return f"<Question(question_text='{self.question_text}', answer='{self.answer}')>"

# ORM methods for the Quiz and Question models
def create_quiz(db, title):
    quiz = Quiz(title=title)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def delete_quiz(db, quiz_id):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz:
        db.delete(quiz)
        db.commit()

def get_all_quizzes(db):
    return db.query(Quiz).all()

def find_quiz_by_id(db, quiz_id):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()

def update_quiz(db, quiz_id, new_title):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz:
        quiz.title = new_title
        db.commit()
        db.refresh(quiz)
    return quiz

def create_question(db, quiz_id, question_text, answer):
    question = Question(quiz_id=quiz_id, question_text=question_text, answer=answer)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def delete_question(db, question_id):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()

def get_all_questions(db):
    return db.query(Question).all()

def find_question_by_id(db, question_id):
    return db.query(Question).filter(Question.id == question_id).first()

def update_question(db, question_id, new_text, new_answer):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        question.question_text = new_text
        question.answer = new_answer
        db.commit()
        db.refresh(question)
    return question
