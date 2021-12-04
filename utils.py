def get_input_list(filename: str) -> list[str]:
    """
        Opens an input file and gives a list of lines

        :param filename: Name of the file
        :type filename: str
        :returns: A list of lines for the file
        :rtype: list[str]
    """

    with open(filename, 'r') as file:
        return file.readlines()


def bin_to_dec(input_bin: str) -> int:
    """
        Converts a binary number to decimal

        :param input_bin: The binary to parse
        :type input_bin: str
        :returns: The decimal number the given binary represents
        :rtype: int
    """

    output_dec = 0
    for index, number in enumerate(reversed(input_bin)):
        output_dec += int(number) * (2 ** index)
    return output_dec
