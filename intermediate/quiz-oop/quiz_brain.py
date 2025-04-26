class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        self.check_answer(user_answer)
        self.question_number += 1
        if self.question_number >= len(self.question_list):
            print("You've completed the quiz.")
            print(f"Your final score is: {self.score}")

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")
