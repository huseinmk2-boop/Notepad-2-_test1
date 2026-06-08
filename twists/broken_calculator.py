import tkinter as tk
import random

class BrokenCalculatorTwist:

    def __init__(
        self,
        overlay_frame,
        finish_callback
    ):

        self.overlay_frame = overlay_frame
        self.finish_callback = finish_callback

        self.answer = random.randint(
            10,
            200
        )

        self.divisor = random.randint(
            10,
            99
        )

        self.dividend = (
            self.answer
            * self.divisor
        )

        self.correct_answer = (
            self.answer
        )

        self.expression = ""

        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        self.build_ui()

    def build_ui(self):

        # ==================
        # TOP ROW
        # ==================

        top_frame = tk.Frame(
            self.overlay_frame,
            relief="solid",
            bd=2
        )

        top_frame.pack(
            fill="x"
        )

        top_frame.grid_columnconfigure(
            0,
            weight=4
        )

        top_frame.grid_columnconfigure(
            1,
            weight=1
        )

        self.question_label = tk.Label(
            top_frame,
            text=f"{self.dividend} ÷ {self.divisor} = ?",
            font=("Arial", 16, "bold"),
            anchor="w",
            padx=15,
            pady=15
        )

        self.question_label.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        answer_frame = tk.Frame(
            top_frame,
            relief="solid",
            bd=1
        )

        answer_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        tk.Label(
            answer_frame,
            text="Answer"
        ).pack()

        self.answer_entry = tk.Entry(
            answer_frame,
            width=12
        )

        self.answer_entry.pack(
            pady=2
        )

        tk.Button(
            answer_frame,
            text="Submit",
            command=self.check_answer
        ).pack(
            pady=2
        )

        # ==================
        # DISPLAY AREA
        # ==================

        self.display_label = tk.Label(
            self.overlay_frame,
            text="",
            relief="solid",
            bd=2,
            anchor="e",
            font=("Consolas", 16),
            padx=15,
            pady=12
        )

        self.display_label.pack(
            fill="x"
        )

        # ==================
        # BUTTON AREA
        # ==================

        self.button_frame = tk.Frame(
            self.overlay_frame,
            relief="solid",
            bd=2
        )

        self.button_frame.pack(
            fill="both",
            expand=True
        )

        self.create_buttons()

    def create_buttons(self):

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]

        random.shuffle(
            buttons
        )

        for col in range(4):

            self.button_frame.grid_columnconfigure(
                col,
                weight=1
            )

        for row in range(4):

            self.button_frame.grid_rowconfigure(
                row,
                weight=1
            )

        row = 0
        col = 0

        for text in buttons:

            btn = tk.Button(
                self.button_frame,
                text=text,
                font=("Arial", 18),
                command=lambda t=text:
                self.button_pressed(t)
            )

            btn.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=4,
                pady=4
            )

            col += 1

            if col > 3:
                col = 0
                row += 1

    def shuffle_buttons(self):

        for widget in (
            self.button_frame
            .winfo_children()
        ):
            widget.destroy()

        self.create_buttons()

    def button_pressed(
        self,
        value
    ):

        if value == "C":

            self.expression = ""

        elif value == "=":

            self.calculate()

        else:

            self.expression += value

        self.refresh_display()

        self.shuffle_buttons()

    def refresh_display(self):

        self.display_label.config(
            text=self.expression
        )

    def calculate(self):

        try:

            result = eval(
                self.expression
            )

            self.expression = str(
                result
            )

        except:

            self.expression = "ERROR"

        self.refresh_display()

    def check_answer(self):

        try:

            user_answer = int(
                self.answer_entry.get()
            )

            if (
                user_answer
                ==
                self.correct_answer
            ):

                for widget in (
                    self.overlay_frame
                    .winfo_children()
                ):
                    widget.destroy()

                self.finish_callback()

            else:

                self.display_label.config(
                    text="WRONG ANSWER"
                )

        except:

            self.display_label.config(
                text="INVALID INPUT"
            )

