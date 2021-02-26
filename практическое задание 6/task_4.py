class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nмашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость больше допустимой! {self.speed}'
        else:
            return f'Скорость {self.name} в пределах допустимой'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость больше допустимой! {self.speed}'
        else:
            return f'Скорость {self.name} в пределах допустимой'


class PoliceCar(Car):
    pass


town = TownCar('BMW', 79, 'черная', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Porshe', 170, 'красная', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Gazel', 30, 'белая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Ford', 100, 'белоголубая', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())
