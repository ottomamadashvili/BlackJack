balance =0

def check_enough_amount():
    global balance
    if balance==0:
        while True:
            try:
                balance = int(input("Ramdeni larit Shedixar: "))

            except ValueError:
                print("sheiyvane cifri!")
                continue
            else:
                return balance

def input_bet(some_balance):
    while True:
        try:
            bet = int(input("sheiyvane beti: "))

        except ValueError:
            print("sheiyvane cifri!")
            continue
        else:
            if bet > some_balance and bet > 0:
                print("beti metia balansze an naklebia nulze")
            else:
                return bet
