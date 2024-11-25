# smartphone.py

class Smartphone:
    def __init__(self, brand, model, battery_percentage, operating_system):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.operating_system = operating_system

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Operating System: {self.operating_system}")
        print(f"Battery: {self.battery_percentage}%")

    def check_battery(self):
        if self.battery_percentage < 20:
            print("Warning: Low battery!")
        else:
            print("Battery is sufficient.")

# Child class inheriting from Smartphone
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery_percentage, operating_system, camera_quality):
        super().__init__(brand, model, battery_percentage, operating_system)
        self.camera_quality = camera_quality

    def display_info(self):
        super().display_info()
        print(f"Camera Quality: {self.camera_quality} MP")

# Example usage
phone = Smartphone("Apple", "iPhone 14", 50, "iOS")
phone.display_info()
phone.check_battery()

advanced_phone = AdvancedSmartphone("Samsung", "Galaxy S21", 15, "Android", 108)
advanced_phone.display_info()
advanced_phone.check_battery()
