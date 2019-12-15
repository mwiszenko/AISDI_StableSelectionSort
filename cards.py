import random
import itertools


def is_bigger(a, b):
    return values_dict[a[1]] > values_dict[b[1]]


# stable
def selection_sort(d):
    for i in range(len(d)):
        min_index = i
        for j in range(i + 1, len(d)):
            if is_bigger(d[min_index], d[j]):
                min_index = j
        min_val = d[min_index]
        while min_index > i:
            d[min_index] = d[min_index - 1]
            min_index -= 1
        d[i] = min_val
    return d


def run_tests():
    deck_one = [('S', '3'), ('D', '2'), ('H', '3'), ('C', '2')]
    deck_two = [('H', 'A'), ('H', '2'), ('S', '2'), ('C', '7')]
    deck_three = [('S', '7'), ('D', '2'), ('H', 'J'), ('H', '3'), ('D', '3')]
    deck_four = []
    deck_five = [('S', '7'), ('H', '7'), ('D', '7'), ('C', '7')]

    assert (selection_sort(deck_one) == [('D', '2'), ('C', '2'), ('S', '3'), ('H', '3')])
    assert (selection_sort(deck_two) == [('H', '2'), ('S', '2'), ('C', '7'), ('H', 'A')])
    assert (selection_sort(deck_three) == [('D', '2'), ('H', '3'), ('D', '3'), ('S', '7'), ('H', 'J')])
    assert (selection_sort(deck_four) == [])
    assert (selection_sort(deck_five) == [('S', '7'), ('H', '7'), ('D', '7'), ('C', '7')])


if __name__ == "__main__":
    # S = Spades, H = Hearts, D = Diamonds, C = Clubs
    colours = ['S', 'H', 'D', 'C']
    # J = Jack, Q = Queen, K = King, A = Ace
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    values_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
                   'A': 14}

    # create random deck of unique cards
    deck = [card for card in itertools.product(colours, values)]
    random.shuffle(deck)

    print("Deck before sorting:", deck)
    print("Deck after sorting:", selection_sort(deck))

    run_tests()
