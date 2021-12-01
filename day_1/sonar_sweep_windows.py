from utils import get_input_list
from day_1.sonar_sweep import count_increase


def add_to_lists(item: int, start_index: int, end_index: int, list_to_add: list[list[int]]) -> list[list[int]]:
    """
        Given an item and list, add the items to the inner-lists at the specified indices

        :param item: The item to add
        :type item: int
        :param start_index: The start index to add from
        :type start_index: int
        :param end_index:  The end index to add to
        :type end_index: int
        :param list_to_add: The list of lists to add to
        :type list_to_add: list[list[int]]
        :returns: A new list with the item added in the specified lists
        :rtype: list[list[int]]
    """

    for i in range(start_index, end_index + 1):
        try:
            list_to_add[i].append(item)
        except IndexError:
            list_to_add.append([])
            list_to_add[i].append(item)
    return list_to_add


def get_window_lists(input_entries: list[int]) -> list[list[int]]:
    """
        Gets the windows of a given list
        
        :param input_entries: The list to get the windows of
        :type input_entries: list[int]
        :returns: A list of lists, the inner-lists representing windows
        :rtype: list[list[int]] 
    """

    output_list = []
    for index, entry in enumerate(input_entries):
        if index == 0:
            output_list.insert(0, [entry])
        elif index == 1:
            output_list[0].append(entry)
            output_list.insert(1, [entry])
        else:
            add_to_lists(entry, index - 2, index, output_list)
    return output_list[:-2]


def count_window_increase(input_entries: list[int]) -> int:
    """
        Count the number of increases from window to window in a given list

        :param input_entries: The list to first create windows and then count the increases of
        :type input_entries: list[int]
        :returns: The number of times an increase occurs
        :rtype: int
    """

    windows = get_window_lists(input_entries)
    window_sums = [sum(window) for window in windows]
    return count_increase(window_sums)


if __name__ == "__main__":
    raw_list = get_input_list("1_2.txt")
    input_list = [int(x) for x in raw_list]
    print("Total increases: ", count_window_increase(input_list))
