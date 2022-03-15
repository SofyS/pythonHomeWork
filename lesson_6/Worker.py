class Worker:
    name = ""
    surname = ""
    position = ""
    __income = {
        "wage": 0,
        "bonus": 0
    }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income["wage"] = wage
        self.__income["bonus"] = bonus

    def get_income(self):
        return self.__income


class Position(Worker):
    def get_full_name(self):
        print(self.name + self.surname)

    def get_total_income(self):
        profit = self.get_income()

        print(profit["wage"] + profit["bonus"])