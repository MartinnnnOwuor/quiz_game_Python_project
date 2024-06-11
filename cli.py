import sys
from database import get_db
from models import create_quiz, delete_quiz, get_all_quizzes, find_quiz_by_id, create_question, delete_question, get_all_questions, find_question_by_id, update_quiz, update_question

def print_menu():
    """Prints the CLI menu options."""
    print("\nQuiz Game CLI")
    print("1. Create a new quiz")
    print("2. Delete a quiz")
    print("3. Display all quizzes")
    print("4. Find quiz by ID")
    print("5. Create a new question")
    print("6. Delete a question")
    print("7. Display all questions")
    print("8. Find question by ID")
    print("9. Update a quiz")
    print("10. Update a question")
    print("11. Exit")

def get_valid_int(prompt):
    """Prompts the user for an integer and handles invalid input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Starting the Quiz Game CLI...")  # Debugging print statement
    db_generator = get_db()
    db = next(db_generator)
    print("Database session started.")  # Debugging print statement

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        print(f"User selected choice: {choice}")  # Debugging print statement

        if choice == '1':
            title = input("Enter quiz title: ")
            create_quiz(db, title)
            print(f"Quiz '{title}' created successfully!")
        elif choice == '2':
            quiz_id = get_valid_int("Enter quiz ID to delete: ")
            quiz = find_quiz_by_id(db, quiz_id)
            if quiz:
                delete_quiz(db, quiz_id)
                print(f"Quiz with ID {quiz_id} deleted successfully!")
            else:
                print(f"No quiz found with ID {quiz_id}.")
        elif choice == '3':
            quizzes = get_all_quizzes(db)
            for quiz in quizzes:
                print(f"Quiz ID: {quiz.id}, Title: {quiz.title}")
        elif choice == '4':
            quiz_id = get_valid_int("Enter quiz ID: ")
            quiz = find_quiz_by_id(db, quiz_id)
            if quiz:
                print(quiz)
            else:
                print(f"No quiz found with ID {quiz_id}.")
        elif choice == '5':
            quiz_id = get_valid_int("Enter quiz ID: ")
            quiz = find_quiz_by_id(db, quiz_id)
            if quiz:
                question_text = input("Enter question text: ")
                answer = input("Enter answer: ")
                create_question(db, quiz_id, question_text, answer)
                print(f"Question '{question_text}' created successfully!")
            else:
                print(f"No quiz found with ID {quiz_id}.")
        elif choice == '6':
            question_id = get_valid_int("Enter question ID to delete: ")
            question = find_question_by_id(db, question_id)
            if question:
                delete_question(db, question_id)
                print(f"Question with ID {question_id} deleted successfully!")
            else:
                print(f"No question found with ID {question_id}.")
        elif choice == '7':
            questions = get_all_questions(db)
            for question in questions:
                print(f"Question ID: {question.id}, Text: {question.question_text}, Answer: {question.answer}, Quiz ID: {question.quiz_id}")
        elif choice == '8':
            question_id = get_valid_int("Enter question ID: ")
            question = find_question_by_id(db, question_id)
            if question:
                print(question)
            else:
                print(f"No question found with ID {question_id}.")
        elif choice == '9':
            quiz_id = get_valid_int("Enter quiz ID to update: ")
            new_title = input("Enter new quiz title: ")
            quiz = update_quiz(db, quiz_id, new_title)
            if quiz:
                print(f"Quiz with ID {quiz_id} updated successfully!")
            else:
                print(f"No quiz found with ID {quiz_id}.")
        elif choice == '10':
            question_id = get_valid_int("Enter question ID to update: ")
            new_text = input("Enter new question text: ")
            new_answer = input("Enter new answer: ")
            question = update_question(db, question_id, new_text, new_answer)
            if question:
                print(f"Question with ID {question_id} updated successfully!")
            else:
                print(f"No question found with ID {question_id}.")
        elif choice == '11':
            print("Goodbye!")
            db_generator.close()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
