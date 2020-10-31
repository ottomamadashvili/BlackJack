from random import choice

suits = ["♧", "♢", "♡", "♤"]
cards = {
    "Ace": 1,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10


}

player_cards_list=[]
dealer_cards_list=[]

def dealingFirst2Cards():
    #randomly giving values to dealer's and player's first two cards

    val1=0
    while val1<2:
        some_cards = f"{choice(list(cards.keys()))}{choice(suits)}"
        if some_cards not in player_cards_list:
            player_cards_list.append(some_cards)
            val1+=1
    val2=0
    while val2<2:
        some_cards2 = f"{choice(list(cards.keys()))}{choice(suits)}"
        if some_cards2 not in player_cards_list:
            dealer_cards_list.append(some_cards2)
            val2+=1


def removing_suits(dealed_cards):
    #removing suits from player's or dealer's cards
    counter = []
    for item in dealed_cards:
        ##counter+=cards[item[:-1]]
        counter.append(cards[item[:-1]])

    return counter

def eleven_or_one(counter2):

    #Ace value either 1 or 11 + returning sum
    for item in counter2:
        if item == 1 and sum(counter2) < 22:
            counter2[counter2.index(item)] = 11



    for item in counter2:
        if item == 11 and sum(counter2) > 21:
            counter2[counter2.index(item)] = 1
    return sum(counter2)


def player_points():
    return eleven_or_one(removing_suits(player_cards_list))

def dealer_points():
    return eleven_or_one(removing_suits(dealer_cards_list))