import tkinter as tk
from tkinter import messagebox
from database import get_db
from models import create_quiz, get_all_quizzes, delete_quiz, create_question, get_all_questions, delete_question, update_quiz, update_question, find_quiz_by_id, find_question_by_id

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        # Quiz management
        self.quiz_title_label = tk.Label(root, text="Quiz Title:")
        self.quiz_title_label.pack()
        self.quiz_title_entry = tk.Entry(root)
        self.quiz_title_entry.pack()

        self.create_quiz_button = tk.Button(root, text="Create Quiz", command=self.create_quiz)
        self.create_quiz_button.pack()

        self.delete_quiz_button = tk.Button(root, text="Delete Selected Quiz", command=self.delete_quiz)
        self.delete_quiz_button.pack()

        self.update_quiz_button = tk.Button(root, text="Update Selected Quiz", command=self.update_quiz)
        self.update_quiz_button.pack()

        self.list_quizzes_button = tk.Button(root, text="List Quizzes", command=self.list_quizzes)
        self.list_quizzes_button.pack()

        self.quizzes_listbox = tk.Listbox(root)
        self.quizzes_listbox.pack()
        self.quizzes = {}  # Dictionary to keep track of quizzes with their IDs

        # Question management
        self.question_text_label = tk.Label(root, text="Question Text:")
        self.question_text_label.pack()
        self.question_text_entry = tk.Entry(root)
        self.question_text_entry.pack()

        self.answer_label = tk.Label(root, text="Answer:")
        self.answer_label.pack()
        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.create_question_button = tk.Button(root, text="Create Question", command=self.create_question)
        self.create_question_button.pack()

        self.delete_question_button = tk.Button(root, text="Delete Selected Question", command=self.delete_question)
        self.delete_question_button.pack()

        self.update_question_button = tk.Button(root, text="Update Selected Question", command=self.update_question)
        self.update_question_button.pack()

        self.list_questions_button = tk.Button(root, text="List Questions for Selected Quiz", command=self.list_questions)
        self.list_questions_button.pack()

        self.questions_listbox = tk.Listbox(root)
        self.questions_listbox.pack()
        self.questions = {}  # Dictionary to keep track of questions with their IDs

        print("QuizApp initialized")  # Debugging print statement

    def create_quiz(self):
        """Creates a new quiz using the title from the entry field."""
        title = self.quiz_title_entry.get()
        db = next(get_db())
        create_quiz(db, title)
        messagebox.showinfo("Info", "Quiz created successfully!")
        self.list_quizzes()
        print(f"Quiz '{title}' created")  # Debugging print statement

    def delete_quiz(self):
        """Deletes the selected quiz."""
        selected_items = self.quizzes_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Warning", "No quiz selected")
            return

        selected_quiz = self.quizzes_listbox.get(selected_items[0])
        quiz_id = self.quizzes[selected_quiz]
        db = next(get_db())
        delete_quiz(db, quiz_id)
        messagebox.showinfo("Info", "Quiz deleted successfully!")
        self.list_quizzes()
        self.questions_listbox.delete(0, tk.END)
        self.questions.clear()
        print(f"Quiz with ID {quiz_id} deleted")  # Debugging print statement

    def update_quiz(self):
        """Updates the title of the selected quiz."""
        selected_items = self.quizzes_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Warning", "No quiz selected")
            return

        selected_quiz = self.quizzes_listbox.get(selected_items[0])
        quiz_id = self.quizzes[selected_quiz]
        new_title = self.quiz_title_entry.get()
        db = next(get_db())
        update_quiz(db, quiz_id, new_title)
        messagebox.showinfo("Info", "Quiz updated successfully!")
        self.list_quizzes()
        print(f"Quiz with ID {quiz_id} updated to '{new_title}'")  # Debugging print statement

    def list_quizzes(self):
        """Lists all quizzes in the listbox."""
        db = next(get_db())
        quizzes = get_all_quizzes(db)
        self.quizzes_listbox.delete(0, tk.END)
        self.quizzes.clear()
        for quiz in quizzes:
            display_text = f"Quiz ID: {quiz.id} Title: {quiz.title}"
            self.quizzes[display_text] = quiz.id
            self.quizzes_listbox.insert(tk.END, display_text)
        print("Quizzes listed")  # Debugging print statement

    def create_question(self):
        """Creates a new question for the selected quiz."""
        selected_items = self.quizzes_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Warning", "No quiz selected")
            return

        selected_quiz = self.quizzes_listbox.get(selected_items[0])
        quiz_id = self.quizzes[selected_quiz]
        question_text = self.question_text_entry.get()
        answer = self.answer_entry.get()
        db = next(get_db())
        create_question(db, quiz_id, question_text, answer)
        messagebox.showinfo("Info", "Question created successfully!")
        self.list_questions()
        print(f"Question '{question_text}' created for quiz ID {quiz_id}")  # Debugging print statement

    def delete_question(self):
        """Deletes the selected question."""
        selected_items = self.questions_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Warning", "No question selected")
            return

        selected_question = self.questions_listbox.get(selected_items[0])
        question_id = self.questions[selected_question]
        db = next(get_db())
        delete_question(db, question_id)
        messagebox.showinfo("Info", "Question deleted successfully!")
        self.list_questions()
        print(f"Question with ID {question_id} deleted")  # Debugging print statement

    def update_question(self):
        """Updates the text and answer of the selected question."""
        selected_items = self.questions_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Warning", "No question selected")
            return

        selected_question = self.questions_listbox.get(selected_items[0])
        question_id = self.questions[selected_question]
        new_text = self.question_text_entry.get()
        new_answer = self.answer_entry.get()
        db = next(get_db())
        update_question(db, question_id, new_text, new_answer)
        messagebox.showinfo("Info", "Question updated successfully!")
        self.list_questions()
        print(f"Question with ID {question_id} updated")  # Debugging print statement

    def list_questions(self):
        """Lists all questions for the selected quiz in the listbox."""
        selected_items = self.quizzes_listbox.curselection()
        if not selected_items:
            messagebox.showwarning("Warning", "No quiz selected")
            return

        selected_quiz = self.quizzes_listbox.get(selected_items[0])
        quiz_id = self.quizzes[selected_quiz]
        db = next(get_db())
        questions = get_all_questions(db)
        self.questions_listbox.delete(0, tk.END)
        self.questions.clear()
        for question in questions:
            if question.quiz_id == quiz_id:
                display_text = f"Question ID: {question.id} Text: {question.question_text} Answer: {question.answer}"
                self.questions[display_text] = question.id
                self.questions_listbox.insert(tk.END, display_text)
        print(f"Questions for quiz ID {quiz_id} listed")  # Debugging print statement

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
    print("GUI started")  # Debugging print statement
