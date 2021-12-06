from utils import get_input_list


def fish_count(raw_starting_fish, days=80):
    """
        Counts fish after a specified number of days

        :param raw_starting_fish: Raw list of starting fish
        :type raw_starting_fish: str
        :param days: Number of days to simulate
        :type days: int
        :returns: How many fish there are after the days have passed
        :rtype: int
    """

    starting_fish = [int(x) for x in raw_starting_fish.split(',')]
    fishes = [0 for _ in range(9)]
    for x in starting_fish:
        fishes[x] += 1
    for day in range(1, days + 1):
        reset_fish = fishes.pop(0)
        fishes[6] += reset_fish
        fishes.append(reset_fish)
    print("\n")
    return sum(fishes)


if __name__ == "__main__":
    DAYS = 256
    raw_fish = get_input_list("6.txt")[0]
    print(f"Number of fish after {DAYS} days:", fish_count(raw_fish, days=DAYS))



