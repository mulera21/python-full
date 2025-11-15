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
# Example usage


car1 = Car("ABC123", "John Doe", "A1")
car1_details = car1.get_details()
print(car1_details)
car1_park_message = car1.park()
print(car1_park_message)