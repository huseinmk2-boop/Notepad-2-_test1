import tkinter as tk
from dotenv import load_dotenv
load_dotenv()

from view.main_view import MainView
from controller.twist_manager import TwistManager

root = tk.Tk()

manager = TwistManager()

print("Selected Twists:")
for twist in manager.selected_twists:
    print("-", twist)

app = MainView(
    root,
    manager
    )

root.mainloop()