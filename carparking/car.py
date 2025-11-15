#-----------------car parking management system-----------------#

class Car:
    def __init__(self, license_plate, owner_name, parking_spot):
        self.license_plate = license_plate
        self.owner_name = owner_name
        self.parking_spot = parking_spot

    def get_details(self):
        return {
            "License Plate": self.license_plate,
            "Owner Name": self.owner_name,
            "Parking Spot": self.parking_spot
        }
    def park(self):
        return f"Car {self.license_plate} parked at spot {self.parking_spot}."
    def leave(self):
        return f"Car {self.license_plate} has left the parking spot {self.parking_spot}."
    def charge_fee(self, hours_parked, rate_per_hour):
        return hours_parked * rate_per_hour 
    
# Example usage


car1 = Car("ABC123", "John Doe", "A1")
car1_details = car1.get_details()
print(car1_details)
car1_park_message = car1.park()
print(car1_park_message)
car1_leave_message = car1.leave()
print(car1_leave_message)
fee = car1.charge_fee(3, 5)  # 3 hours parked at $5 per hour
print(f"Parking fee for car {car1.license_plate}: ${fee}")

car2 = Car("XYZ789", "Jane Smith", "B2")
car2_details = car2.get_details()
print(car2_details)
car2_park_message = car2.park()
print(car2_park_message)
car2_leave_message = car2.leave()
print(car2_leave_message)
fee2 = car2.charge_fee(2, 5)  # 2 hours parked at $5 per hour
print(f"Parking fee for car {car2.license_plate}: ${fee2}")