from math import floor

from utils import get_input_list


class Fish:

    def __init__(self, initial_count=8):
        self.initial_value = initial_count

    def get_after_days(self, days):
        return (floor(days / 7) ** (days / 7 - 8)) - self.initial_value


def fish_count(raw_starting_fish, days=80):
    fishes = [Fish(initial_count=int(x)) for x in raw_starting_fish.split(",")]
    total = len(fishes)
    for fish in fishes:
        total += fish.get_after_days(days)
    return total


if __name__ == "__main__":
    DAYS = 18
    raw_fish = get_input_list("6.txt")[0]
    print(f"Number of fish after {DAYS} days:", fish_count(raw_fish, days=DAYS))



