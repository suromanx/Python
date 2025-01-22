class Car:
    def __init__(self, color, consumption, tank_volume, mileage=0):
        self.color = color
        self.consumtion = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return 'Двигатель запущен'
        return 'Двигатель уже был запущен'

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return 'Двигатель Остановлен'
        return 'Двигатель уже был остановлен'

    def drive(self, distance):
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / 100 * self.consumtion < distance:
            return "Малый запас топлива."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumtion
        return f'Проехали {distance}км. Остаток топлива {self.reserve}'

    def refuel(self):
        self.reserve = self.tank_volume

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumtion(self):
        return self.consumtion




######################################

class ElectricCar:

    def __init__(self, color, consumption, bat_capasity, mileage=0):
        self.color = color
        self.consumtion = consumption
        self.bat_capasity = bat_capasity
        self.reserve = bat_capasity
        self.mileage = mileage
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return 'Двигатель Запущен'
        return 'Двигатель уже был Запущен'

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return 'Двигатель Остановлен'
        return 'Двигатель уже был остановлен'

    def drive(self, distance):
        if not self.engine_on:
            return 'Двигатель не Запущен'
        if self.reserve / self.consumtion * 100 < distance:
            return 'Малый заряд батареи'
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumtion
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

    def recharge(self):
        self.reserve = self.bat_capasity

    def get_mileage(self):
        return self.mileage

    def get_reserve(self):
        return self.reserve

    def get_consumtion(self):
        return self.consumtion

def range_reserve(car):
    return car.get_reserve() / car.get_consumtion() * 100


car_1 = Car(color='black', consumption=10, tank_volume=55)
car_2 = ElectricCar(color='black', consumption=10, bat_capasity=90)
print(f"Запас хода: {range_reserve(car_1)} км.")
print(f"Запас хода: {range_reserve(car_2)} км.")