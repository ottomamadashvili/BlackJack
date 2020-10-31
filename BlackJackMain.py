import PrintingCards
import Casino
import CardManipulation
from Money import check_enough_amount
from Money import input_bet
from time import sleep


name = input("Ra gqvia: ")
player = Casino.Player(name,check_enough_amount())
bet=input_bet(player.balance)
PrintingCards.printingFirst()
hit_or_stay= input("Hit or Stay? ")
yes_or_no="ki"

while yes_or_no=="ki":
    while hit_or_stay.lower() == 'hit':
        CardManipulation.player_cards_list.append(player.hit())
        PrintingCards.justPrint()

        if CardManipulation.player_points() > 21:
            print("\n\n\n\n\t\t****Burst! Dealer Won****")
            player.balance-=bet
            PrintingCards.justPrintFull(player.balance)
            yes_or_no = input("ginda kide tamashi? ki/ara ")
            if yes_or_no.lower() == "ki":
                if player.balance > 0:
                    CardManipulation.player_cards_list.clear()
                    CardManipulation.dealer_cards_list.clear()
                    bet = input_bet(player.balance)
                    PrintingCards.printingFirst()
                    hit_or_stay = input("Hit or Stay?")
                else:
                    print("fuli agar gaqvs, bye!")
                    break
                continue
            else:
                print("your balance is", player.balance)
                break
        hit_or_stay = input("Hit or Stay? ")


    while hit_or_stay.lower() =='stay':

        if CardManipulation.dealer_points() > CardManipulation.player_points() and CardManipulation.dealer_points()<=21:
            player.balance -= bet
            print("\nDealer  Won!")
            PrintingCards.justPrintFull(player.balance)



            yes_or_no = input("ginda kide tamashi? ki/ara ")
            if yes_or_no.lower() == "ki":
                if player.balance > 0:
                    CardManipulation.player_cards_list.clear()
                    CardManipulation.dealer_cards_list.clear()
                    bet = input_bet(player.balance)
                    PrintingCards.printingFirst()
                    hit_or_stay = input("Hit or Stay?")
                else:
                    print("fuli agar gaqvs, bye!")
                    break
                continue
            else:
                print("your balance is", player.balance)
                break



        if CardManipulation.dealer_points()>21:
            player.balance += bet
            print(f'player Won! your balance is: {player.balance}')

            yes_or_no = input("ginda kide tamashi? ki/ara ")
            if yes_or_no.lower() == "ki":
                if player.balance > 0:
                    CardManipulation.player_cards_list.clear()
                    CardManipulation.dealer_cards_list.clear()
                    bet = input_bet(player.balance)
                    PrintingCards.printingFirst()
                    hit_or_stay = input("Hit or Stay?")
                else:
                    print("fuli agar gaqvs, bye!")
                    break
                continue
            else:
                print("your balance is", player.balance)
                break


        CardManipulation.dealer_cards_list.append(player.hit())
        PrintingCards.justPrintFull(player.balance)
        sleep(1.5)


print("morcha kino")