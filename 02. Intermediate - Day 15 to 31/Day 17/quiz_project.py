from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_object = Question(question["question"], question["correct_answer"])
    question_bank.append(question_object)

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_question():
    quizbrain.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quizbrain.score}/{quizbrain.question_number}")
