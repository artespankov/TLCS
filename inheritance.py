import random

class Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __repr__(self):
        return "{} of {}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        one = self.suit, self.rank
        other = other.suit, other.rank
        return one < other


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def cards_amount(self):
        return len(self.cards)

    def __str__(self):
        cards = []
        for card in self.cards:
            cards.append(str(card))
        return "\n".join(cards)

    def remove_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)
        return card

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, number):
        for _ in range(number):
            hand.add_card(self.remove_card())

    def deal_hand(self, hands, cards_num):
        hands_list = []
        for hand in hands:
            hand_cards = []
            for j in range(cards_num):
                if not self.cards:
                    hands_list.append({hand: hand_cards})
                    return hands_list
                hand_cards.append(self.remove_card())
            hands_list.append({hand: hand_cards})
        return hands_list


class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label


if __name__ == "__main__":
    deck = Deck()

    deck.shuffle()

    hands_list = [Hand(label="Hand {}".format(i)) for i in range(12)]

    # deck.sort()
    # print(deck)

    setup = deck.deal_hand(hands_list, 5)

    print(setup)

