from model.twist_model import TwistModel

class BaseTwist(TwistModel):
    def __init__(self, name, objective):
        super().__init__(name, objective)
    
    def start(self):
        pass
    
    def complete(self):
        self.completed = True