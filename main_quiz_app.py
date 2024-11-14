# main_quiz_app.py

from question_management import Quiz as QuizManager
from quiz_functionality import Quiz as QuizTaker

def main():
    # Create an instance of QuizManager or QuizTaker
    quiz_manager = QuizManager()

    # Add questions to the quiz
    quiz_manager.add_question("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa")
    quiz_manager.add_question("What is 27 squared?", ["627", "729", "707", "751"], "729")

    # Display the questions
    print("Questions in the quiz:")
    quiz_manager.display_questions()

    # If you want to actually run the quiz and take answers, you should use an instance of QuizTaker
    quiz_taker = QuizTaker()
    quiz_taker.add_question("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa")
    quiz_taker.add_question("What is 27 squared?", ["627", "729", "707", "751"], "729")

    # Start the quiz
    print("\nStarting the quiz...")
    quiz_taker.take_quiz()

if __name__ == "__main__":
    main()
