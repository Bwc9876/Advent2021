from statistics import median
from math import inf

from utils import get_input_list


def get_fuel_cost(crabs, target):
    total = 0
    for crab in crabs:
        total += sum(range(1, abs(target - crab) + 1))
    return total


def get_cheapest_fuel(raw_crabs):
    crabs = sorted([int(x) for x in raw_crabs.split(",")])
    target_num = median(crabs)
    cost = sum([abs(target_num - x) for x in crabs])
    return cost


def get_cheapest_fuel_exponential(raw_crabs):
    crabs = sorted([int(x) for x in raw_crabs.split(",")])
    minimum = inf
    for x in range(1, int(crabs[-1])):
        print(f"{x}/{int(crabs[-1])}", end="\r")
        total_cost = get_fuel_cost(crabs, x)
        if minimum > total_cost:
            minimum = total_cost
    print("")
    return minimum


if __name__ == "__main__":
    print(get_cheapest_fuel_exponential(get_input_list("7.txt")[0]))
