from utils import get_input_list


class Card:
    """
        A class that represents a bingo card

        :ivar rows: The rows of the card
        :type rows: list[list[int]]
        :ivar called: The numbers that have been called
        :type called: list[int]
    """

    @staticmethod
    def parse_row(raw_row: str) -> list[int]:
        """
            Gets a row as a list of integers

            :param raw_row: The row as a space-delimited string
            :type raw_row: str
            :returns: The row as a list of integers
            :rtype: list[int]
        """

        current_num = ""
        output_row = []
        for index, character in enumerate(raw_row):
            if index in [2, 5, 8, 11]:
                output_row.append(int(current_num))
                current_num = ""
            else:
                current_num += character
                if index == len(raw_row) - 1:
                    output_row.append(int(current_num))
        return output_row

    def __init__(self, raw_board: list[str]):
        """
            Instantiates a new card

            :param raw_board: The raw card as a list of strings
            :type raw_board: list[str]
        """

        self.rows = []
        self.called = []
        for line in raw_board:
            self.rows.append(self.parse_row(line))

    def check_list_called(self, list_to_check: list[int]) -> bool:
        """
            Check to see if all numbers in a list have been called

            :param list_to_check: The list to check the numbers of
            :type list_to_check: list[int]
            :returns: Whether all numbers have been called
            :rtype: bool
        """

        num_called = 0
        for number in list_to_check:
            if number in self.called:
                num_called += 1
        return num_called == len(list_to_check)

    def check_row_bingo(self) -> bool:
        """
            Check all rows to see if there's a bingo

            :returns: Whether a row has had a bingo
            :rtype: bool
        """

        for row in self.rows:
            if self.check_list_called(row):
                print("Bingo! (Row)")
                return True
        return False

    def get_column(self, index: int) -> list[int]:
        """
            Get a column given its index

            :param index: The index of the column to get
            :type index: int
            :returns: The column at the given index
            :rtype: list[int]
        """

        return [row[index] for row in self.rows]

    def check_column_bingo(self) -> bool:
        """
            Check to see if any columns have bingo

            :returns: Whether a column has bingo
            :rtype: bool
        """

        for column in [self.get_column(index) for index in range(len(self.rows[0]))]:
            if self.check_list_called(column):
                print("Bingo! (Column)")
                return True
        return False

    def calc_score(self) -> int:
        """
            Calculates the score of the bingo card

            :returns: The score of the bingo card (sum of all uncalled numbers * last called number)
            :rtype: int
        """

        sum_of_unmarked = 0
        for row in self.rows:
            for number in row:
                if number not in self.called:
                    sum_of_unmarked += number
        return sum_of_unmarked * self.called[-1]

    def evaluate(self) -> bool:
        """
            Evaluates this card to see if there's any bingo's

            :returns: Whether there are any bingo's
            :rtype: bool
        """

        return self.check_row_bingo() or self.check_column_bingo()

    def call_number(self, number: int) -> bool:
        """
            Adds a number to the list of called numbers and then evaluates

            :param number: The number to add to called numbers
            :type number: int
            :returns: Whether the card now has bingo from the new number
            :rtype: bool
        """

        self.called.append(number)
        return self.evaluate()


def make_cards(raw_cards: list[str]) -> list[Card]:
    """
        Creates cards given a list of raw lines

        :param raw_cards: The raw lines to create the cards from
        :type raw_cards: list[str]
        :returns: A list of card objects created from the raw lines
        :rtype: list[Card]
    """

    current_card = ""
    cards = []
    for index, raw_line in enumerate(raw_cards):
        if (index + 1) % 6 == 0:
            cards.append(Card(current_card.split("\n")[:-1]))
            current_card = ""
        else:
            current_card += raw_line
    return cards


def start_game(raw_lines: list[str]) -> None:
    """
        Begins a game of bingo and calls numbers until one card wins

        :param raw_lines: The raw lines to use for the game, first line should be a list of numbers to call, rest should be cards
        :type raw_lines: list[str]
    """

    print("Starting Bingo Simulation")
    to_call = [int(x) for x in raw_lines.pop(0).split(",")]
    raw_lines.pop(0)
    cards = make_cards(raw_lines)
    winner = None
    for number in to_call:
        print("Calling", number)
        for card in cards:
            if card.call_number(number):
                winner = card
                break
        if winner is not None:
            break
    if winner is None:
        print("ERROR: ", "No Winner!")
    else:
        print(f"Card #{cards.index(winner) + 1} wins!")
        print("Winning score is:", winner.calc_score())


if __name__ == "__main__":
    raw_input = get_input_list("4.txt")
    start_game(raw_input)
