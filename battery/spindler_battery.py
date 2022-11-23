from battery.battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        date_battery_needs_service = add_years_to_date(self.last_service_date, 3)
        return date_battery_needs_service