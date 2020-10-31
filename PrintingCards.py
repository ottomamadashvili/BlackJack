import CardManipulation
def printingFirst():
    #giving random values to players and dealing first two cards, on of the dealer's card is hidden
    CardManipulation.dealingFirst2Cards()
    CardManipulation.removing_suits(CardManipulation.dealer_cards_list)
    CardManipulation.removing_suits(CardManipulation.player_cards_list)
    playersOnes = ', '.join(CardManipulation.player_cards_list)
    print(f'Dealer has: {CardManipulation.dealer_cards_list[0]}  X')
    print(f'You have: {playersOnes} and Total is: {CardManipulation.player_points()}')



def justPrint():
    #printing only dealed cards, one of the dealer's is hidden
    playersOnes = ', '.join(CardManipulation.player_cards_list)

    print(f'\nDealer has: {CardManipulation.dealer_cards_list[0]}  X')
    print(f'You have: {playersOnes} and Total is: { CardManipulation.player_points() }')

def justPrintFull(balance):
    #pringing all the cards including player's balance.
    playersOnes = ', '.join(CardManipulation.player_cards_list)
    dealersOnes = ', '.join(CardManipulation.dealer_cards_list)
    print(f'\nDealer has: {dealersOnes } and Total is: {CardManipulation.dealer_points()}')
    print(f'You have: {playersOnes} and Total is: {CardManipulation.player_points()}\nYour Balance is: {balance} ')
