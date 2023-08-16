from collections import namedtuple
from typing import Iterable, Optional

Item = namedtuple("Item", "name, value")

max_cost: Optional[int] = None


def counter(items: Iterable[Item]) -> int:
    global max_cost
    total = 0
    for i in items:
        total += i.value
    if not max_cost or total > max_cost:
        max_cost = total
    return total


def main():
    breakfast_items = [Item('Pancakes', 11), Item('Bacon', 4), Item('Coffee', 3), Item('Coffee', 3), Item('Scone', 2)]
    dinner_items = [Item('Pizza', 20), Item('Beer', 9), Item('Beer', 9)]

    breakfast_total = counter(breakfast_items)
    print(f"Breakfast was ${breakfast_total}")

    dinner_total = counter(dinner_items)
    print(f"Dinner was ${dinner_total}")

    print(f"Today your most expensive meal costs ${max_cost}")


if __name__ == '__main__':
    main()
