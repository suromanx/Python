def create_car(color, consumption, tank_volume, mileage=0):
    return {'color': color,
            'consumption': consumption,
            'tank_volume': tank_volume,
            'reserve': tank_volume,
            'mileage': mileage,
            'engine_on': False
            }


def start_engine(car):
    if not car['engine_on'] and car['reserve'] > 0:
        car['engine_on'] = True
        return 'Двигатель Запущен'
    return "Двигатель уже был запущен."


def stor_engine(car):
    if car['engine_on']:
        car['engine_on'] = False
        return 'Двигатель Остановлен'
    return 'Двигатель уже был остановлен'


def drive(car, distanse):
    if not car['engine_on']:
        return 'Двигатель не запущен'
    if car['reserve'] / car['consumption'] * 100 < distanse:
        return 'Малый запас топлива'
    car['mileage'] += distanse
    car['reserve'] -= distanse / 100 * car['consumption']

    return f'Проехали {distanse}км. Остаток топлива {car["reserve"]}литров'


def refuel(car):
    car['reserve'] = car['tank_volume']


def get_mileage(car):
    return f'ПРобег {car["mileage"]}км'


def get_reserve(car):
    return f'Запас топлива {car["reserve"]}'


car_1 = create_car(color="black", consumption=10, tank_volume=55)
print(start_engine(car_1))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 100))
print(drive(car_1, 300))



