from utils import get_input_list, bin_to_dec


def get_counts(input_bins: list[str]) -> list[list[int]]:
    """
        Gets the counts of 1s and 0s in a list of bytes
        :param input_bins: The list of bytes to get the counts of
        :type input_bins: list[str]
        :returns: A 2D array, each internal array containing the counts of 0s and 1s
        :rtype: list[list[int]]
    """

    counts = [[0, 0] for x in range(len(input_bins[0].strip()))]
    for byte in input_bins:
        for index, bit in enumerate(byte.strip()):
            counts[index][int(bit)] += 1
    return counts


def construct_gamma_rate(counts: list[list[int]]):
    """
        Gets the gamma rate given the counts of a list of bytes

        :param counts: The counts to use to get the gamma rate
        :type counts: list[list[int]]
        :returns: The gamma rate, in binary of the submarine
        :rtype: str, int
    """

    output_bin = ""
    for pair in counts:
        output_bin += "0" if pair[0] > pair[1] else "1"
    return output_bin, bin_to_dec(output_bin)


def construct_epsilon_rate(counts):
    """
        Gets the epsilon rate given the counts of a list of bytes

        :param counts: The counts to use to get the epsilon rate
        :type counts: list[list[int]]
        :returns: The epsilon rate, in binary of the submarine
        :rtype: str, int
    """

    output_bin = ""
    for pair in counts:
        output_bin += "0" if pair[0] < pair[1] else "1"
    return output_bin, bin_to_dec(output_bin)


def get_reactor_rates(input_bytes: list[str]) -> None:
    """
        Get the rates of the reactor

        :param input_bytes: The bytes to use to get the rates
        :type input_bytes: list[str]
    """

    counts = get_counts(input_bytes)
    bin_gamma, dec_gamma = construct_gamma_rate(counts)
    bin_epsilon, dec_epsilon = construct_epsilon_rate(counts)
    print("Binary Gamma: ", bin_gamma)
    print("Binary Epsilon: ", bin_epsilon)
    print("Decimal Gamma: ", dec_gamma)
    print("Decimal Epsilon: ", dec_epsilon)
    print("Power Consumption Rate: ", dec_epsilon * dec_gamma)


if __name__ == "__main__":
    get_reactor_rates(get_input_list('3.txt'))
