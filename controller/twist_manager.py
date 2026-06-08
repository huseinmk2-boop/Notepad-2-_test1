import random

class TwistManager:

    def __init__(self):
        
        self.available_twists = [
            "Lavaloon",
            "Self Aware Calculator",
            "Broken Calculator",
            "Teleporting Button",
            "Bloodmoon",
            "Capslock Demon",
            "Black Hole"
        ]

        self.selected_twists = random.sample(
            self.available_twists,
            3
        )

        self.completed_twists = 0

        # Hidden trigger thresholds
        self.trigger_points = [
            random.randint(85, 100),
            random.randint(200, 250),
            random.randint(399, 500)
        ]

        print("Trigger Points:", self.trigger_points)
        self.objectives = {

            "Lavaloon":
                "Hold the button until the progress bar is full.\nDon't let it touch you!",

            "Self Aware Calculator":
                "Solve the multiplication problem.",

            "Broken Calculator":
                "Solve the division problem.",

            "Teleporting Button":
                "Click the button.",

            "Bloodmoon":
                "Survive the Bloodmoon.",

            "Capslock Demon":
                "Type the sentence correctly.",

            "Black Hole":
                "Reach the finish line before the singularity consumes everything.\nYour cursor is your joystick"
        }
    
    def get_current_twist(self):

        if self.completed_twists < len(self.selected_twists):
            return self.selected_twists[
                self.completed_twists
            ]

        return None

    def complete_current_twist(self):

        self.completed_twists += 1

    def all_completed(self):

        return self.completed_twists >= len(
            self.selected_twists
        )

    def should_trigger_twist(self, character_count):

        if self.completed_twists >= 3:
            return False

        next_trigger = self.trigger_points[
            self.completed_twists
        ]

        return character_count >= next_trigger
    
    def get_current_objective(self):

        current_twist = self.get_current_twist()

        return self.objectives[current_twist]