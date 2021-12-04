from utils import get_input_list


class Submarine:
    """
        A class that represents a submarine

        :ivar aim: The current aim of the submarine
        :type aim: int
        :ivar depth: How far below the water the submarine is
        :type depth: int
        :ivar horizontal: The horizontal position of the submarine
        :type horizontal: int
        :cvar commands: The available commands of the submarine
        :type commands: dict[str, func]
    """

    # Commands

    def up(self, amount: float):
        """
            Aim up

            :param amount: The amount to aim up
            :type amount: float
        """

        self.aim -= amount

    def down(self, amount: float):
        """
            Aim down

            :param amount: The amount to aim down
            :type amount: float
        """

        self.aim += amount

    def forward(self, amount: float):
        """
            Makes the submarine go forward

            :param amount: The amount to go forward by
            :type amount: float
        """

        self.horizontal += amount
        self.depth += self.aim * amount

    def backward(self, amount: float):
        """
            Makes the submarine go backward

            :param amount: The amount to go backward by
            :type amount: float
        """

        self.horizontal -= amount
        self.depth -= self.aim * amount

    commands = {
        'up': up,
        'down': down,
        'forward': forward,
        'backward': backward
    }

    # Methods

    def __init__(self):
        """
            Instantiates a new submarine
        """

        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def process_command(self, command: str):
        """
            Process a command on the submarine

            :param command: The command to execute
            :type command: str
        """

        split_command = command.split(" ", 1)
        operator = split_command[0]
        args = [float(x) for x in split_command[1].split(" ")]
        try:
            # noinspection PyArgumentList
            self.commands[operator](self, *args)
        except KeyError:
            print("Invalid Operator: ", operator, "!")

    def control(self, command_list: list[str]):
        """
            Executes a list of commands

            :param command_list: The commands to execute
            :type command_list: list[str]
        """

        for command in command_list:
            self.process_command(command)

    def get_coords(self) -> int:
        """
            Get the coordinates of the submarine

            :returns: The coordinates of the submarine
            :rtype: int
        """

        return self.depth * self.horizontal


if __name__ == "__main__":
    input_list = get_input_list("2.txt")
    sub = Submarine()
    sub.control(input_list)
    print("Coordinates Are: ", sub.get_coords())
