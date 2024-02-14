class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.d = {3: small, 2:medium, 1:big}

    def addCar(self, carType: int) -> bool:
        if self.d[carType]:
            self.d[carType] -= 1
            return True
        return False