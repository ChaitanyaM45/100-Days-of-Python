class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.score=0
        self.question_list=q_list

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q{self.question_no}. {current_question.question} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower()==current_answer.lower():
            self.score+=1
            print("You Got it Right!")
        else:
            print("Wrong Answer.")
        print(f"The correct answer was {current_answer}.")
        print(f"Your Score: {self.score}/{self.question_no}")
        print("\n")