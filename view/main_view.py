import tkinter as tk

from twists.teleport_button import TeleportButtonTwist
from twists.bloodmoon import BloodmoonTwist
from twists.capslock_demon import CapslockDemonTwist
from twists.self_aware_calculator import SelfAwareCalculatorTwist
from twists.broken_calculator import BrokenCalculatorTwist
from twists.lavaloon import LavaloonTwist
from twists.black_hole import BlackHoleTwist

class MainView:

    def __init__(self, root, twist_manager):

        self.root = root
        self.twist_manager = twist_manager

        self.root.title("Notepad")
        self.root.geometry("800x600")

        self.twist_active = False

        # Notepad area
        self.text_area = tk.Text(
            root,
            font=("Consolas", 12),
            wrap="word"
        )

        self.text_area.pack(
            expand=True,
            fill="both"
        )

        # Overlay (hidden by default)
        self.overlay_frame = tk.Frame(
            self.root,
            bg="#202020"
        )

        # Detect typing
        self.text_area.bind(
            "<KeyRelease>",
            self.on_text_changed
        )

        # Status bar
        self.status_label = tk.Label(
            root,
            text="Twists Completed: 0/3",
            anchor="w"
        )

        self.status_label.pack(
            fill="x",
            side="bottom"
        )

    def on_text_changed(self, event):

        if self.twist_active:
            return
        
        if (self.twist_manager.completed_twists >= 3):
            return

        current_text = self.text_area.get(
            "1.0",
            "end-1c"
        )

        character_count = len(current_text)

        # print(
        #     f"Characters: {character_count}"
        # )

        if self.twist_manager.should_trigger_twist(
            character_count
        ):
            self.trigger_twist()

    def trigger_twist(self):

        self.twist_active = True

        twist_name = (
            self.twist_manager
            .get_current_twist()
        )

        objective = (
            self.twist_manager
            .get_current_objective()
        )

        self.show_warning_overlay(
            twist_name,
            objective
        )

        print(
            f"Starting twist: {twist_name}"
        )

    def fake_twist(self):

        twist_name = (
            self.twist_manager
            .get_current_twist()
        )

        if twist_name == "Teleporting Button":

            TeleportButtonTwist(
                self.overlay_frame,
                self.finish_twist
            )

        elif twist_name == "Bloodmoon":

            BloodmoonTwist(
                self,
                self.finish_twist
            )
        
        elif twist_name == "Capslock Demon":

            CapslockDemonTwist(
                self.overlay_frame,
                self.finish_twist
            )

        elif twist_name == "Self Aware Calculator":

            SelfAwareCalculatorTwist(
                self.overlay_frame,
                self.finish_twist
            )

        elif twist_name == "Broken Calculator":

            BrokenCalculatorTwist(
                self.overlay_frame,
                self.finish_twist
            )
            
        elif twist_name == "Lavaloon":

            LavaloonTwist(
                self.overlay_frame,
                self.finish_twist,
                self.retry_current_twist
            )

        elif twist_name == "Black Hole":

            BlackHoleTwist(
                self.overlay_frame,
                self.finish_twist,
                self.retry_current_twist
            )

        else:

            print(
                f"{twist_name} not implemented yet"
            )

            self.finish_twist()

    def finish_twist(self):

        self.twist_active = False

        self.twist_manager.complete_current_twist()

        completed = (self.twist_manager.completed_twists)
        
        self.update_twist_progress(
            completed
        )

        self.hide_overlay()
        
        if completed >= 3:
            self.show_victory_screen()

    def update_twist_progress(self, completed):

        self.status_label.config(
            text=f"Twists Completed: {completed}/3"
        )

    def show_warning_overlay(
        self,
        twist_name,
        objective
        ):


        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        warning_title = tk.Label(
            self.overlay_frame,
            text="⚠ WARNING ⚠",
            font=("Arial", 24, "bold"),
            fg="red",
            bg="#202020"
        )

        warning_title.place(
            relx=0.5,
            rely=0.3,
            anchor="center"
        )

        twist_label = tk.Label(
            self.overlay_frame,
            text=twist_name,
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#202020"
        )

        twist_label.place(
            relx=0.5,
            rely=0.45,
            anchor="center"
        )

        objective_label = tk.Label(
            self.overlay_frame,
            text=objective,
            font=("Arial", 12),
            fg="white",
            bg="#202020"
        )

        objective_label.place(
            relx=0.5,
            rely=0.6,
            anchor="center"
        )

        self.root.after(
            2000,
            self.start_twist_after_warning
        )

    def start_twist_after_warning(self):


        for widget in self.overlay_frame.winfo_children():
            widget.destroy()

        self.fake_twist()


    
    def hide_overlay(self):

        self.overlay_frame.place_forget()
        
    def show_victory_screen(self):

        self.overlay_frame.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        victory_text = """

    =================================

    CONGRATULATIONS

    You survived Notepad.

    The notebook seems satisfied...
    for now.

    [ENTER] Continue writing
    [ESC] Close session

    =================================
    """

        label = tk.Label(
            self.overlay_frame,
            text=victory_text,
            font=("Consolas", 14),
            bg="#202020",
            fg="white",
            justify="center"
        )

        label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.root.bind(
            "<Return>",
            self.continue_after_victory
        )

        self.root.bind(
            "<Escape>",
            self.close_session
        )

    def continue_after_victory(
        self,
        event=None
    ):

        self.root.unbind(
            "<Return>"
        )

        self.root.unbind(
            "<Escape>"
        )

        self.hide_overlay()

    def close_session(
        self,
        event=None
    ):

        self.root.destroy()

    def retry_current_twist(self):

        self.twist_active = True

        for widget in (
            self.overlay_frame.winfo_children()
        ):
            widget.destroy()

        twist_name = (
            self.twist_manager
            .get_current_twist()
        )

        objective = (
            self.twist_manager
            .get_current_objective()
        )

        self.show_warning_overlay(
            twist_name,
            objective
        )