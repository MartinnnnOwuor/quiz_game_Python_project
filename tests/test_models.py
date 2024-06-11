import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import create_quiz, create_question, get_all_quizzes, get_all_questions, find_quiz_by_id, find_question_by_id, delete_quiz, delete_question

class TestQuizGame(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.db = self.Session()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
        self.db.close()

    def test_create_quiz(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        self.assertEqual(quiz.title, "Sample Quiz")
        self.assertIsNotNone(quiz.id)

    def test_create_question(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        question = create_question(self.db, quiz.id, "What is the capital of France?", "Paris")
        self.assertEqual(question.question_text, "What is the capital of France?")
        self.assertEqual(question.answer, "Paris")
        self.assertEqual(question.quiz_id, quiz.id)

    def test_get_all_quizzes(self):
        create_quiz(self.db, "Sample Quiz 1")
        create_quiz(self.db, "Sample Quiz 2")
        quizzes = get_all_quizzes(self.db)
        self.assertEqual(len(quizzes), 2)

    def test_get_all_questions(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        create_question(self.db, quiz.id, "What is the capital of France?", "Paris")
        create_question(self.db, quiz.id, "What is the capital of Germany?", "Berlin")
        questions = get_all_questions(self.db)
        self.assertEqual(len(questions), 2)

    def test_find_quiz_by_id(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        found_quiz = find_quiz_by_id(self.db, quiz.id)
        self.assertEqual(found_quiz.id, quiz.id)
        self.assertEqual(found_quiz.title, quiz.title)

    def test_find_question_by_id(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        question = create_question(self.db, quiz.id, "What is the capital of France?", "Paris")
        found_question = find_question_by_id(self.db, question.id)
        self.assertEqual(found_question.id, question.id)
        self.assertEqual(found_question.question_text, question.question_text)

    def test_delete_question(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        question = create_question(self.db, quiz.id, "What is the capital of France?", "Paris")
        delete_question(self.db, question.id)
        found_question = find_question_by_id(self.db, question.id)
        self.assertIsNone(found_question)

    def test_delete_quiz(self):
        quiz = create_quiz(self.db, "Sample Quiz")
        delete_quiz(self.db, quiz.id)
        found_quiz = find_quiz_by_id(self.db, quiz.id)
        self.assertIsNone(found_quiz)

if __name__ == '__main__':
    unittest.main()
