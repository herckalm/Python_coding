import random


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ": <" + str(self.value) + "," + str(self.calories) + ">"


def buildMenu(names, values, calories):
    """ names, values, calories lists of same length.
        name a list of strings
        values, calories lists of numbers
        returns list of Foods"""
    menu = []

    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))
    return items


def testMaxVal(foods, maxUnits, algorithm):
    print(f"Menu contains {len(foods)} items")
    print(f"Use search tree to allocate {maxUnits} calories")
    val, taken = algorithm(foods, maxUnits)
    print(f"Total value of items taken = {val}")
    for item in taken:
        print(f"\t{item}")