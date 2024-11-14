class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")

        else:
            for i in range(1, new_floor + 1):
                print(i)

object = House("Кошкин дом", 6)

object.go_to(0)
object.go_to(2)
object.go_to(-1)
object.go_to(6)
object.go_to(7)