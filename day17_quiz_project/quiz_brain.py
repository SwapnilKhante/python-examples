


class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_no = 0;
        self.score = 0;

    def still_has_questions(self):
        return len(self.question_bank) > self.question_no

    def next_question(self):
        question = self.question_bank[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no} : {question.text} (True/False): ")
        self.check_correct_answer(answer, question.answer)

    def check_correct_answer(self, answer, actual_answer):
        if answer.lower() == actual_answer.lower():
            print(f"You have got it right!")
            self.score += 1
        else:
            print(f"It's a wrong answer!")
        print(f"correct answer is {actual_answer}")
        print(f"Your current score is {self.score} / {self.question_no}")
        print()

