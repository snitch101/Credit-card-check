import re
from cs50 import get_string

def main():

    #get valid card sequence from user
    card = get_card()

    #syntactic validation of card
    valid = check_card(card)

    if valid:
        if len(card) == 16:
            for i in range(len(card)):
                if int(card[0]) == 4:
                    print("VISA")
                    break
                elif int(card[0]) == 5 and 10 - int(card[1]) > 4 and 10 - int(card[1]) < 10:
                    print("MASTERCARD")
                    break
                else:
                    print("INVALID")
                    break
        elif len(card) == 15:
            for i in range(len(card)):
                if int(card[0]) == 3:
                    if int(card[1]) == 4 or int(card[1]) == 7:
                        print("AMEX")
                        break
                    else:
                        print("INVALID starting num")
                        break
        elif len(card) == 13:
            for i in range(len(card)):
                if int(card[0]) == 4:
                    print("VISA")
                    break
                else:
                    print("INVALID")
                    break
    else:
        print("INVALID principle")

#get card number from the user
def get_card():

    #get input from the user
    while True:
        card = get_string("Card: ")
        numbers = re.findall('[0-9]+', card)
        if card == numbers[0]:
            if len(card) == 16 or len(card) == 13 or len(card) ==15:
                break
            else:
                print("INVALID lenght")
                break
    return card

def check_card(card):

    sum_arr = []
    sum_card1 = 0
    for i in range(len(card) - 2, -1, -2):
        sum_arr.append(str(int(card[i]) * 2))
        if len(card) % 2 == 0:
            sum_card1 += int(card[i + 1])
        else:
            if i - 1 > 0:
                sum_card1 += int(card[i - 1])
            else:
                sum_card1 += int(card[len(card) - 1])
                sum_card1 += int(card[i - 1])


    sum_card2 = 0
    for i in range(0, len(sum_arr)):
        for j in range(0, len(sum_arr[i])):
            sum_card2 += int(sum_arr[i][j])

    sum_card3 = (sum_card1 + sum_card2) % 10

    if sum_card3 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

    #378282246310005