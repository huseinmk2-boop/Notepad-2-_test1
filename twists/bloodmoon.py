import tkinter as tk
import random

class BloodmoonTwist:

    def __init__(
        self,
        main_view,
        finish_callback
    ):

        self.main_view = main_view
        self.finish_callback = finish_callback

        self.messages = [
            "The moon is watching.",
            "Keep writing.",
            "Do not look behind you.",
            "Something feels wrong.",
            "The night grows darker.",
            "It sees your notes.",
            "Don't stop typing.",
            "The Bloodmoon hungers."
        ]

        # Remove warning overlay
        self.main_view.hide_overlay()

        # Save original colors
        self.old_text_bg = self.main_view.text_area.cget("bg")
        self.old_text_fg = self.main_view.text_area.cget("fg")

        self.old_status_bg = self.main_view.status_label.cget("bg")
        self.old_status_fg = self.main_view.status_label.cget("fg")

        # Apply Bloodmoon theme
        self.main_view.text_area.config(
            bg="#2b0000",
            fg="#dddddd",
            insertbackground="white"
        )

        self.main_view.status_label.config(
            bg="#550000",
            fg="white"
        )

        self.update_message()

        self.main_view.root.after(
            15000,
            self.end_bloodmoon
        )

    def update_message(self):

        self.main_view.status_label.config(
            text=random.choice(self.messages)
        )

        self.message_job = self.main_view.root.after(
            3000,
            self.update_message
        )

    def end_bloodmoon(self):

        self.main_view.root.after_cancel(
            self.message_job
        )

        self.main_view.text_area.config(
            bg=self.old_text_bg,
            fg=self.old_text_fg,
            insertbackground="black"
        )

        self.main_view.status_label.config(
            bg=self.old_status_bg,
            fg=self.old_status_fg
        )

        self.finish_callback()
