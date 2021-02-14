from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

question_set = random.choice(question_data)

for i in range(len(question_set)):
    new_q = Question(question_set[i]["question"], question_set[i]["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
