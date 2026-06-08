import tkinter as tk

class LavaloonTwist:

    def __init__(
        self,
        overlay_frame,
        finish_callback,
        retry_callback
    ):

        self.overlay_frame = overlay_frame
        self.finish_callback = finish_callback
        self.retry_callback = retry_callback

        self.mouse_x = 0
        self.mouse_y = 0

        self.speed = 3

        self.lives = 3
        self.invincible = False

        self.progress = 0
        self.hovering = False

        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        self.canvas = tk.Canvas(
            self.overlay_frame,
            bg="black",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        # ==================
        # UI
        # ==================

        self.lives_label = tk.Label(
            self.overlay_frame,
            text="",
            font=("Arial", 16),
            bg="black",
            fg="white"
        )

        self.lives_label.place(
            relx=0.02,
            rely=0.02
        )
        
        self.update_lives_display()

        self.progress_label = tk.Label(
            self.overlay_frame,
            text="Progress",
            bg="black",
            fg="white"
        )

        self.progress_label.place(
            relx=0.4,
            rely=0.02
        )

        self.progress_bar = tk.Canvas(
            self.overlay_frame,
            width=300,
            height=20,
            bg="gray20",
            highlightthickness=1
        )

        self.progress_bar.place(
            relx=0.5,
            rely=0.02,
            anchor="n"
        )

        self.progress_fill = (
            self.progress_bar.create_rectangle(
                0,
                0,
                0,
                20,
                fill="green"
            )
        )

        self.hold_button = tk.Label(
            self.overlay_frame,
            text="HOLD HERE",
            font=("Arial", 14, "bold"),
            bg="white",
            padx=20,
            pady=10
        )

        self.hold_button.place(
            relx=0.5,
            rely=0.85,
            anchor="center"
        )

        self.hold_button.bind(
            "<Enter>",
            self.start_hover
        )

        self.hold_button.bind(
            "<Leave>",
            self.stop_hover
        )

        # ==================
        # LAVALOON
        # ==================

        self.circle = self.canvas.create_oval(
            100,
            100,
            150,
            150,
            fill="red"
        )

        self.canvas.bind(
            "<Motion>",
            self.mouse_moved
        )
        
        self.game_over = False
        
        self.move_lavaloon()
        self.update_progress()
        

    def start_hover(
        self,
        event
    ):

        self.hovering = True

    def stop_hover(
        self,
        event
    ):

        self.hovering = False

    def mouse_moved(
        self,
        event
    ):

        self.mouse_x = event.x
        self.mouse_y = event.y

    def update_lives_display(self):

        if self.lives == 3:

            text = "♥ ♥ ♥"

        elif self.lives == 2:

            text = "♥ ♥ ♡"

        elif self.lives == 1:

            text = "♥ ♡ ♡"

        else:

            text = "♡ ♡ ♡"

        self.lives_label.config(
            text=text,
            fg="red"
        )

    def lose_life(self):

        if self.invincible:
            return

        self.lives -= 1

        self.update_lives_display()

        self.invincible = True

        self.overlay_frame.after(
            1000,
            self.end_invincibility
        )

        if self.lives <= 0:

            self.display_game_over()

    def end_invincibility(self):

        self.invincible = False

    def display_game_over(self):

        if self.game_over:
            return
        
        self.game_over = True
        
        for widget in (
            self.overlay_frame.winfo_children()
        ):
            widget.destroy()

        game_over = tk.Label(
            self.overlay_frame,
            text="LAVALOON GOT YOU\n\n" "[R] Retry",
            font=("Arial", 24, "bold"),
            bg="black",
            fg="red"
        )

        game_over.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        
        self.overlay_frame.bind_all(
            "<r>",
            self.retry
        )

        self.overlay_frame.bind_all(
            "<R>",
            self.retry
        )

    def update_progress(self):

        if self.game_over:
            return
        
        if self.hovering:

            self.progress += 1

        else:

            self.progress -= 0.2

        self.progress = max(
            0,
            min(
                100,
                self.progress
            )
        )

        width = (
            self.progress * 3
        )

        self.progress_bar.coords(
            self.progress_fill,
            0,
            0,
            width,
            20
        )

        if self.progress >= 100:

            for widget in (
                self.overlay_frame.winfo_children()
            ):
                widget.destroy()

            self.finish_callback()
            return

        self.overlay_frame.after(
            50,
            self.update_progress
        )

    def move_lavaloon(self):
        
        if self.game_over:
            return
        
        coords = self.canvas.coords(
            self.circle
        )

        x1, y1, x2, y2 = coords

        circle_x = (
            x1 + x2
        ) / 2

        circle_y = (
            y1 + y2
        ) / 2

        dx = (
            self.mouse_x
            - circle_x
        )

        dy = (
            self.mouse_y
            - circle_y
        )

        distance = (
            dx ** 2
            + dy ** 2
        ) ** 0.5

        if distance > 0:

            move_x = (
                dx
                / distance
            ) * self.speed

            move_y = (
                dy
                / distance
            ) * self.speed

            self.canvas.move(
                self.circle,
                move_x,
                move_y
            )

        if distance < 25:

            self.lose_life()

        self.canvas.after(
            30,
            self.move_lavaloon
        )

    def retry(
        self,
        event=None
    ):

        self.overlay_frame.unbind_all(
            "<r>"
        )

        self.overlay_frame.unbind_all(
            "<R>"
        )

        self.retry_callback()
