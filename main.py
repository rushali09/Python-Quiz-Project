from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
   # converting a list into object
   question_text = item["question"]
   question_answer = item["correct_answer"]
   # create an object and pass arguments
   question = Question(question_text, question_answer)
   # append objects into question_bank list
   question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
   quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")