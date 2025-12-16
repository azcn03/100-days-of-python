class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print(f"You got it wrong, The right answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}\n\n")
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)
        self.question_number += 1

    
    def still_has_questions(self):
        if len(self.question_list) <= self.question_number:
            return False
        else:
            return True
        
        

