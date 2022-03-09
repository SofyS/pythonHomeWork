class Car:
    speed = 0
    color = ""
    name = ""
    is_police = 0

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Cкорость машины {self.speed}км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 61:
            print("Превышении скорости! больше 60км/ч")
        else:
            print(f"Cкорость машины {self.speed}км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышении скорости! больше 60км/ч")
        else:
            print(f"Cкорость машины {self.speed}км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)