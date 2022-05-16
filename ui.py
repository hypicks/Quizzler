from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 12, "bold")
FONT_TEXT = ("Arial", 20, "italic")


# Classes are named by pascal, no spaces
class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Make it a property which you can access in the class
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=300, height=415, padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 130, width=280, text="Text here", font=FONT_TEXT, fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img,
                                  bd=0,
                                  highlightthickness=0,
                                  activebackground=THEME_COLOR,
                                  command=self.true_answer)
        self.true_button.grid(row=2, column=1)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img,
                                   bd=0,
                                   highlightthickness=0,
                                   activebackground=THEME_COLOR,
                                   command=self.wrong_answer)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz! Well done!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Create two new methods that you can add as a command to the buttons. The methods need to call check_answer()
    # from the quiz_brain and pass of the string "True" or "False". This should print some feedback to the console
    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)