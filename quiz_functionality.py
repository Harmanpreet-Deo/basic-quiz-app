# quiz_functionality.py

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

    def take_quiz(self):
        score = 0
        for question in self.questions:
            print(question.question_text)
            for option in question.options:
                print(f" - {option}")
            answer = input("Your answer: ")
            if answer.lower() == question.correct_answer.lower():
                score += 1
        print(f"Your final score is {score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = Quiz()
    
    # Adding questions and taking the quiz
    quiz.add_question("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa")
    quiz.add_question("What is 27 squared?", ["627", "729", "707", "751"], "729")
    quiz.take_quiz()
