import tkinter as tk
import random
import math

class PursuerTwist:

    def __init__(
        self,
        overlay_frame,
        finish_callback
    ):

        self.overlay_frame = overlay_frame
        self.finish_callback = finish_callback

        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        self.canvas = tk.Canvas(
            self.overlay_frame,
            bg="#3d6db5",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.canvas.update()

        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()

        self.game_over = False

        # Reduced sensitivity multiplier
        self.sensitivity = 0.30

        direction = random.choice(
            [
                "right",
                "left",
                "top",
                "bottom"
            ]
        )

        self.direction = direction

        # ==================
        # SPAWNS
        # ==================

        if direction == "right":

            self.cursor_x = 150
            self.cursor_y = self.height / 2

            self.pursuer_x = 50
            self.pursuer_y = self.height / 2

            self.create_vertical_finish(
                self.width - 40
            )

        elif direction == "left":

            self.cursor_x = self.width - 150
            self.cursor_y = self.height / 2

            self.pursuer_x = self.width - 50
            self.pursuer_y = self.height / 2

            self.create_vertical_finish(
                0
            )

        elif direction == "top":

            self.cursor_x = self.width / 2
            self.cursor_y = self.height - 150

            self.pursuer_x = self.width / 2
            self.pursuer_y = self.height - 50

            self.create_horizontal_finish(
                0
            )

        else:

            self.cursor_x = self.width / 2
            self.cursor_y = 150

            self.pursuer_x = self.width / 2
            self.pursuer_y = 50

            self.create_horizontal_finish(
                self.height - 40
            )

        # ==================
        # PLAYER
        # ==================

        self.cursor = self.canvas.create_oval(
            self.cursor_x - 15,
            self.cursor_y - 15,
            self.cursor_x + 15,
            self.cursor_y + 15,
            fill="red"
        )

        self.cursor_label = (
            self.canvas.create_text(
                self.cursor_x,
                self.cursor_y - 30,
                text="YOU",
                fill="white",
                font=("Arial", 10, "bold")
            )
        )

        # ==================
        # PURSUER
        # ==================

        self.pursuer_speed = 1.8

        self.pursuer = self.canvas.create_oval(
            self.pursuer_x - 15,
            self.pursuer_y - 15,
            self.pursuer_x + 15,
            self.pursuer_y + 15,
            fill="black"
        )

        self.pursuer_label = (
            self.canvas.create_text(
                self.pursuer_x,
                self.pursuer_y - 30,
                text="PURSUER",
                fill="white",
                font=("Arial", 10, "bold")
            )
        )

        self.last_mouse_x = None
        self.last_mouse_y = None

        self.canvas.bind(
            "<Motion>",
            self.mouse_moved
        )

        self.move_pursuer()

        print(
            f"Pursuer direction: {direction}"
        )

    # ==================
    # FINISH LINE
    # ==================

    def create_vertical_finish(
        self,
        x
    ):

        size = 20

        for y in range(
            0,
            self.height,
            size
        ):

            for col in range(2):

                color = (
                    "white"
                    if
                    (y // size + col) % 2 == 0
                    else
                    "black"
                )

                self.canvas.create_rectangle(
                    x + col * size,
                    y,
                    x + (col + 1) * size,
                    y + size,
                    fill=color,
                    outline=color
                )

    def create_horizontal_finish(
        self,
        y
    ):

        size = 20

        for x in range(
            0,
            self.width,
            size
        ):

            for row in range(2):

                color = (
                    "white"
                    if
                    (x // size + row) % 2 == 0
                    else
                    "black"
                )

                self.canvas.create_rectangle(
                    x,
                    y + row * size,
                    x + size,
                    y + (row + 1) * size,
                    fill=color,
                    outline=color
                )

    # ==================
    # PLAYER MOVEMENT
    # ==================

    def mouse_moved(
        self,
        event
    ):

        if self.game_over:
            return

        if self.last_mouse_x is None:

            self.last_mouse_x = event.x
            self.last_mouse_y = event.y
            return

        dx = (
            event.x
            - self.last_mouse_x
        )

        dy = (
            event.y
            - self.last_mouse_y
        )

        self.cursor_x += (
            dx
            * self.sensitivity
        )

        self.cursor_y += (
            dy
            * self.sensitivity
        )

        self.last_mouse_x = event.x
        self.last_mouse_y = event.y

        self.canvas.coords(
            self.cursor,
            self.cursor_x - 15,
            self.cursor_y - 15,
            self.cursor_x + 15,
            self.cursor_y + 15
        )

        self.canvas.coords(
            self.cursor_label,
            self.cursor_x,
            self.cursor_y - 30
        )

        self.check_finish()

    # ==================
    # PURSUER
    # ==================

    def move_pursuer(self):

        if self.game_over:
            return

        dx = (
            self.cursor_x
            - self.pursuer_x
        )

        dy = (
            self.cursor_y
            - self.pursuer_y
        )

        distance = math.sqrt(
            dx * dx
            + dy * dy
        )

        if distance > 0:

            self.pursuer_x += (
                dx
                / distance
            ) * self.pursuer_speed

            self.pursuer_y += (
                dy
                / distance
            ) * self.pursuer_speed

        self.canvas.coords(
            self.pursuer,
            self.pursuer_x - 15,
            self.pursuer_y - 15,
            self.pursuer_x + 15,
            self.pursuer_y + 15
        )

        self.canvas.coords(
            self.pursuer_label,
            self.pursuer_x,
            self.pursuer_y - 30
        )

        self.pursuer_speed += 0.001

        if distance < 30:

            self.display_game_over()
            return

        self.canvas.after(
            16,
            self.move_pursuer
        )

    # ==================
    # WIN
    # ==================

    def check_finish(self):

        if self.direction == "right":

            if self.cursor_x >= self.width - 40:
                self.win()

        elif self.direction == "left":

            if self.cursor_x <= 40:
                self.win()

        elif self.direction == "top":

            if self.cursor_y <= 40:
                self.win()

        elif self.direction == "bottom":

            if self.cursor_y >= self.height - 40:
                self.win()

    def win(self):

        if self.game_over:
            return

        self.game_over = True

        for widget in (
            self.overlay_frame.winfo_children()
        ):
            widget.destroy()

        self.finish_callback()

    # ==================
    # LOSE
    # ==================

    def display_game_over(self):

        self.game_over = True

        for widget in (
            self.overlay_frame.winfo_children()
        ):
            widget.destroy()

        label = tk.Label(
            self.overlay_frame,
            text="THE PURSUER GOT YOU",
            font=("Arial", 24, "bold"),
            bg="#3d6db5",
            fg="red"
        )

        label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

