import CardManipulation
from random import choice


class CasinoMembers:
    def hit(self):

        while True:
            another_card = f"{choice(list(CardManipulation.cards.keys()))}{choice(CardManipulation.suits)}"
            if another_card not in CardManipulation.dealer_cards_list and another_card not in CardManipulation.player_cards_list:
                return another_card


class Player(CasinoMembers):

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance


