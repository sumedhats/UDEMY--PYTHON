from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    question_obj = Question(question_text, question_answer)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

print("🧠 Welcome to the India Quiz!\nAnswer with True or False.\n")

while quiz.still_has_questions():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"✅ Final Score: {quiz.score}/{quiz.question_number}")
