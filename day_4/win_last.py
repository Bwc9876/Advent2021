from utils import get_input_list
from day_4.bingo import make_cards


def find_last_winner(raw_input: list[str]) -> None:
    """
        Finds whichever card wins last

        :param raw_input: Same input as a regular bingo game
        :type raw_input: list[str]
    """

    print("Starting Bingo Simulation")
    to_call = [int(x) for x in raw_input.pop(0).split(",")]
    raw_input.pop(0)
    cards = make_cards(raw_input)
    loser = None
    for number in to_call:
        print("Calling", number)
        winners = []
        for index, card in enumerate(cards):
            if card.call_number(number):
                print("Card", index + 1, "Won")
                if len(cards) > 1:
                    winners.append(card)
                else:
                    print("Card", index + 1, "is the last winner!")
                    loser = cards[0]
                    break
        for winner in winners:
            cards.remove(winner)
        if loser is not None:
            break

    if loser is None:
        print("ERROR: ", "No Loser!")
    else:
        print(f"Losing score is", loser.calc_score())


if __name__ == "__main__":
    input_list = get_input_list("4.txt")
    find_last_winner(input_list)
