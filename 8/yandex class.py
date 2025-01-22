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

car_1 = Car(color = 'black', consumption=10,tank_volume=55)
car_2 = Car(color = 'black', consumption=22,tank_volume=70)

print(car_2.start_engine())
print(car_1.start_engine())
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(100))
print(car_1.drive(300))
print(f"Пробег {car_1.get_mileage()} км.")
print(f"Запас топлива {car_1.get_reserve()} л.")
print(car_1.stop_engine())
print(car_1.drive(100))

