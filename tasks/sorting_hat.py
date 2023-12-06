from enum import Enum, auto
from random import choice
from os import walk

class House(Enum):
    Gryffindor = auto(),
    Ravenclaw = auto(),
    Hufflepuff = auto(),
    Slytherin = auto()

class SortingHat:
    def __init__(self, students):
        self.houses = dict()
        for student in students:
            house = choice(list(House))
            self.houses[student] = house

    def get_houses(self):
        h = []
        for student, house in self.houses.items():
            h.append((student, house.name))
        return h

    def __getitem__(self, student):
        return self.houses[student]

    def __repr__(self):
        return f"Hat: {str(self.get_houses())}"

    # def __str__(self):
    #     pass

    def __iter__(self):
        return SortingHat.Iter(self.get_houses())

    class Iter:
        def __init__(self, houses):
            self.houses = houses
            self.pos = 0

        def __next__(self):
            if self.pos == len(self.houses):
                raise StopIteration
            student = self.houses[self.pos]
            self.pos += 1
            return student

def main():

    hat = SortingHat(["Artemiy", "Alina", "Arina", "Varya", "Alexey"])
    print(hat)
    for choice in hat:
        print(choice)
    print(hat['Artemiy'])

    # *.txt *foo*
    # if "Artemiy" in hat:
    #     print("Hello")

    # it = hat.__iter__()
    # while True:
    #     try:
    #         print(it.__next__())
    #     except StopIteration:
    #         break

    # it = SortingHat.Iter(hat.get_houses())



    # hat = SortingHat(["Artemiy", "Alina", "Arina", "Varya", "Alexey"])
    # print(hat.get_houses())
    # l = [("Artemiy", "Hufflepuff"), ("Alina", "Slytherin")]
    # for el in l:
    #     print(l)

main()

