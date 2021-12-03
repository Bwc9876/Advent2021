from utils import get_input_list, bin_to_dec
from day_3.diagnostics import get_counts

O2 = True
CO2 = False


def get_winner(to_evaluate: list[int], system_type: bool) -> str:
    """
        Gets who wins in a given character pair
        :param to_evaluate: The pair to evaluate
        :type to_evaluate: list[int]
        :param system_type: The system type (O2 or CO2)
        :type system_type: bool
        :returns: Who won, 1 or 0
        :rtype: str
    """

    if system_type == O2:
        if to_evaluate[0] > to_evaluate[1]:
            return "0"
        else:
            return "1"
    else:
        if to_evaluate[0] == to_evaluate[1]:
            return "0"
        elif to_evaluate[0] < to_evaluate[1]:
            return "0"
        elif to_evaluate[1] < to_evaluate[0]:
            return "1"


def search_step(input_list: list[str], counts: list[list[int]], char_pos: int, system_type: bool):
    """
        A step during the search process

        :param input_list: The list of bytes to check
        :type input_list: list[str]
        :param counts: The counts of numbers
        :type counts: list[list[int]]
        :param char_pos: The character position to check
        :type char_pos: int
        :param system_type: The type of system (O2 or CO2)
        :type system_type: bool
        :returns: The narrowed-down list of bytes
        :rtype: list[str]
    """

    target_count = counts[char_pos]
    winner = get_winner(target_count, system_type)
    new_list = []
    for byte in input_list:
        if byte[char_pos] == winner:
            new_list.append(byte)
    return new_list


def search_for_val(input_bins: list[str], system_type: bool) -> str:
    """
        Searches for the diagnostics of either the O2 or the CO2 systems
        
        :param input_bins: The list to search in
        :type input_bins: list[str]
        :param system_type: The type of system to search for (O2 or CO2)
        :type system_type: bool
        :returns: The diagnostic information for the system
        :rtype: str
    """

    result_list = input_bins.copy()
    for i in range(len(input_bins[0])):
        if len(result_list) <= 1:
            break
        counts = get_counts(result_list)
        result_list = search_step(result_list, counts, i, system_type)
    if len(result_list) >= 1:
        return result_list[0]


if __name__ == "__main__":
    input_bytes = [x.strip() for x in get_input_list("3.txt")]
    o2_bin = search_for_val(input_bytes, O2)
    co2_bin = search_for_val(input_bytes, CO2)
    print("Oxygen Generator Rating Binary: ", o2_bin)
    print("CO2 Scrubber Rating Binary: ", co2_bin)
    print("Oxygen Generator Rating: ", bin_to_dec(o2_bin))
    print("CO2 Scrubber Rating: ", bin_to_dec(co2_bin))
    print("Life Support Rating: ", bin_to_dec(o2_bin) * bin_to_dec(co2_bin))
