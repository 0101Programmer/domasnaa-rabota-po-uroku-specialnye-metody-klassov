class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor}? Такого этажа не существует!')
        else:
            print(*range(1, new_floor + 1), sep='\n')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: ЖК {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('Marble field', 22)
h2 = House('Chester', 101)

print(h1)
print(h2)
print()
print(len(h1))
print(len(h2))