from utils import get_input_list

class Submarine:

    # Commands

    def up(self, amount: float):
        self.depth -= amount

    def down(self, amount: float):
        self.depth += amount

    def forward(self, amount: float):
        self.horizontal += amount

    def backward(self, amount: float):
        self.horizontal -= amount

    commands = {
        'up': up,
        'down': down,
        'forward': forward,
        'backward': backward
    }

    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def process_command(self, command):
        split_command = command.split(" ", 1)
        operator = split_command[0]
        args = [float(x) for x in split_command[1].split(" ")]
        try:
            self.commands[operator](*args)
        except KeyError:
            print("Invalid Operator: ", operator, "!")

    def control(self, command_list):
            for command in command_list:
                self.process_command(command)

    def get_coords(self):
        return self.depth * self.horizontal


if __name__ == "__main__":
    input_list = get_input_list("2_1.txt")
    sub = Submarine()
    sub.control(input_list)
    print("Coordinates Are: ", sub.get_coords())
