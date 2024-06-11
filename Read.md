# QUIZ_MASTER

A GUI and CLI based quiz application built with Python

## Features 

- Create and manage quizzes.
- Add and edit questions for each quiz.
- Customize the look and feel of the application.
- Offers two environments for running the app; CLI and GUI.
- Delete quizzes and questions that are no longer relevant.
- View a list of available quizzes and questions.


## Project Structure

Quiz_Master/
├── cli.py
├── models.py
├── database.py
├── init_db.py
├── Pipfile
├── tkinter_app.py
├── Read.md
└── tests/
    └── test_modules.py




## Requirements

-Python 3.9 or higher
-SQLite database (or any other supported database)
-"pipenv" for managing dependencies
-Tkinter (included in the Python standard library)

## Installation

1. Clone the repository: `git clone https://github.com/your-username/Brain_Storm.git`
2. Navigate to the project directory: `cd Quiz_Master`
3. Install the required packages: `pipenv install`
4. Create a SQLite database: `sqlite3 db.sqlite3`
5. Run the application: `pipenv run python cli.py` (for app to run in terminal)
6. Run the application `pipenv run python tkinter_app.py` (for app to run in GUI)
    



## Usage

1. The GUI application will launch, displaying the main menu.
2. From the main menu, you can create a new quiz, take a quiz, or view a list of all available quizzes.
3. Once you have created a quiz, you can add and edit questions for it.
4. Once you have taken a quiz, you can view your results.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
5. Wait for your pull request to be reviewed and merged

Contributions are welcome! If you have any ideas for new features or bug fixes, please submit an issue or a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

