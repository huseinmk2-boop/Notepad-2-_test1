import tkinter as tk
import random

class CapslockDemonTwist:

    def __init__(
        self,
        overlay_frame,
        finish_callback
    ):

        self.overlay_frame = overlay_frame
        self.finish_callback = finish_callback

        self.capslock_on = False

        self.sentences = [
            "the moon watches silently",
            "this notepad is perfectly normal",
            "something is behind you",
            "the demon loves uppercase",
            "keep typing and do not stop",
            "this notepad feels strange",
            "i should not trust this program"
        ]

        self.target_sentence = random.choice(
            self.sentences
        )

        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        self.build_ui()

        self.toggle_capslock()

    def build_ui(self):

        self.title_label = tk.Label(
            self.overlay_frame,
            text="CAPSLOCK DEMON",
            font=("Arial", 18, "bold")
        )

        self.title_label.pack(
            pady=20
        )

        self.state_label = tk.Label(
            self.overlay_frame,
            text="CAPSLOCK: OFF",
            font=("Arial", 14)
        )

        self.state_label.pack()

        self.sentence_label = tk.Label(
            self.overlay_frame,
            text=self.target_sentence,
            font=("Arial", 14)
        )

        self.sentence_label.pack(
            pady=20
        )

        self.entry = tk.Entry(
            self.overlay_frame,
            width=60
        )

        self.entry.pack(
            pady=10
        )

        self.entry.focus_set()

        self.entry.bind(
            "<KeyRelease>",
            self.process_input
        )

    def toggle_capslock(self):

        self.capslock_on = (
            not self.capslock_on
        )

        current_text = self.entry.get()

        if self.capslock_on:

            self.state_label.config(
                text="CAPSLOCK: ON"
            )

            self.sentence_label.config(
                text=self.target_sentence.upper()
            )

            transformed = (
                current_text.upper()
            )

        else:

            self.state_label.config(
                text="CAPSLOCK: OFF"
            )

            self.sentence_label.config(
                text=self.target_sentence.lower()
            )

            transformed = (
                current_text.lower()
            )

        self.entry.delete(
            0,
            tk.END
        )

        self.entry.insert(
            0,
            transformed
        )

        self.toggle_job = (
            self.overlay_frame.after(
                1000,
                self.toggle_capslock
            )
        )

    def process_input(
        self,
        event
    ):

        current_text = self.entry.get()

        if self.capslock_on:

            transformed = (
                current_text.upper()
            )

        else:

            transformed = (
                current_text.lower()
            )

        if transformed != current_text:

            cursor_pos = self.entry.index(
                tk.INSERT
            )

            self.entry.delete(
                0,
                tk.END
            )

            self.entry.insert(
                0,
                transformed
            )

            self.entry.icursor(
                cursor_pos
            )

        self.check_answer()

    def check_answer(self):

        user_text = self.entry.get()

        if (
            user_text.strip().lower()
            ==
            self.target_sentence.lower()
        ):

            self.overlay_frame.after_cancel(
                self.toggle_job
            )

            for widget in (
                self.overlay_frame
                .winfo_children()
            ):
                widget.destroy()

            self.finish_callback()
