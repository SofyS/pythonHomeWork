class Road:
    __length = 0
    __width = 0
    weigth = 25
    tickness = 0.05

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_asphalt(self):
        intake = self.__length * self.__width * self.weigth * self.tickness / 1000
        print(f'Нужно {intake} т асфальта')