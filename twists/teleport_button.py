import tkinter as tk
import random

class TeleportButtonTwist:


    def __init__(
        self,
        overlay_frame,
        finish_callback
    ):

        self.overlay_frame = overlay_frame
        self.finish_callback = finish_callback

        self.teleports_remaining = random.randint(
            15,
            20
        )

        # Show overlay
        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        self.button = tk.Button(
            self.overlay_frame,
            text="CLICK ME",
            command=self.button_clicked
        )

        self.move_button()

    def move_button(self):

        x = random.randint(
            50,
            700
        )

        y = random.randint(
            50,
            500
        )

        self.button.place(
            x=x,
            y=y
        )

    def button_clicked(self):

        if self.teleports_remaining > 0:

            self.teleports_remaining -= 1

            self.move_button()

        else:

            self.button.destroy()

            self.finish_callback()

