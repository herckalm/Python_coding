from foodMenu import Food, buildMenu


def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)

    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return result, totalValue


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print(f"Total value of items taken = {val}")
    for item in taken:
        print(f"\t{item}")


def testGreedys(foods, maxUnits):
    print(f"Use greedy by value to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.getValue)
    print(f"\nUse greedy by cost to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
    print(f"\nUse greedy by density to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
