import random

class GameController:

    def __init__(self, twists):
        self.twists = random.sample(twists, 3)
        self.current_twist = 0

    def get_current_twist(self):
        return self.twists[self.current_twist]

    def next_twist(self):
        self.current_twist += 1