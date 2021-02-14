from foodMenu import Food, buildMenu, buildLargeMenu, testMaxVal


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
       0/1 knapsack problem and the items of that solution"""

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


# names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
# values = [89, 90, 95, 100, 90, 79, 50, 10]
# calories = [123, 154, 258, 354, 365, 150, 95, 195]

for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, maxVal)

# foods = buildMenu(names, values, calories)

