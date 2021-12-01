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
