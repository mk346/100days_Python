from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    incorrect_answer = question['incorrect_answers']
    new_question = Question(question_text, question_answer, incorrect_answer)
    question_bank.append(new_question)
quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


