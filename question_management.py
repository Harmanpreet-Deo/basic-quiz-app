# question_management.py

class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question_text, options, correct_answer):
        question = Question(question_text, options, correct_answer)
        self.questions.append(question)

    def display_questions(self):
        for idx, question in enumerate(self.questions, start=1):
            print(f"{idx}. {question.question_text}")
            for option in question.options:
                print(f" - {option}")

if __name__ == "__main__":
    quiz = Quiz()
    
    # Adding and displaying questions
    quiz.add_question("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa")
    quiz.add_question("What is 27 squared?", ["627", "729", "707", "751"], "729")
    quiz.display_questions()
