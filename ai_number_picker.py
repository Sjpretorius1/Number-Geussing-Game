from random import randint, shuffle, choice

class number:
    def __init__(self, number):
        self.number = number


def numberPicker():
    num_List = []
    for num in range(20):
        picked = randint(1, 20)
        num_List.append(picked)
    shuffle(num_List)
    return number(choice(num_List))