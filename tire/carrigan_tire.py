from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
              
    def needs_service(self):
        if any(tire_value >= 0.9 for tire_value in self.tire_wear):
            return True
        else:
            return False
