from utils import get_input_list


def count_increase(input_entries: list[int]) -> int:
    """
        Given a list of depths, find the number of entries greater than the previous entries

        :param input_entries: The list of depths
        :type input_entries: list[int]
        :returns: The number of increases
        :rtype: int
    """

    increase_count = 0
    previous = None
    for entry in input_entries:
        if previous is not None:
            if entry > previous:
                increase_count += 1
        previous = entry
    return increase_count


if __name__ == "__main__":
    raw_list = get_input_list("1_1.txt")
    input_list = [int(x) for x in raw_list]
    print("Total increases: ", count_increase(input_list))
