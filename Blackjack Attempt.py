from random import randint

usedCards = [0]

def card():
    n = 0
    while n in usedCards:
        n = randint(1,52)
    name = 0
    value = 0
    if n in usedCards:
        print("duplicate card")
    else:
        if n >= 1 and n <= 13:
            suit = "Spades"
        elif n >= 14 and n <= 26:
            suit = "Hearts"
        elif n >= 27 and n <= 39:
            suit = "Clubs"
        elif n >= 40 and n <= 52:
            suit = "Diamonds"
        else:
            print("suit failed.")
        if n == 1 or n == 14 or n == 27 or n == 40:
            name = "Ace"
            value = 11
        elif n == 11 or n == 24 or n == 37 or n == 50:
            name = "Jack"
            value = 10
        elif n == 12 or n == 25 or n == 38 or n == 51:
            name = "Queen"
            value = 10
        elif n == 13 or n == 26 or n == 39 or n == 52:
            name = "King"
            value = 10
        elif n == 2 or n == 15 or n == 28 or n == 41:
            value = 2
            name = 2
        elif n == 3 or n == 16 or n == 29 or n == 42:
            value = 3
            name = 3
        elif n == 4 or n == 17 or n == 30 or n == 43:
            value = 4
            name = 4
        elif n == 5 or n == 18 or n == 31 or n == 44:
            value = 5
            name = 5
        elif n == 6 or n == 19 or n == 32 or n == 45:
            value = 6
            name = 6
        elif n == 7 or n == 20 or n == 33 or n == 46:
            value = 7
            name = 7
        elif n == 8 or n == 21 or n == 34 or n == 47:
            value = 8
            name = 8
        elif n == 9 or n == 22 or n == 35 or n == 48:
            value = 9
            name = 9
        elif n == 10 or n == 23 or n == 36 or n == 49:
            value = 10
            name = 10
        usedCards.append(n)
        print("This card is",name,"of",suit,".")
        print("It has a value of",value,".")
        print("NK: ",usedCards)
        return value

def dealer():
    card1 = card()
    card2 = card()
    dealerHand = card1 + card2
    #dealerHand = 21
    print(card1)
    print(card2)
    print("Dealer has",dealerHand)
    return dealerHand

def player():
    card1 = card()
    card2 = card()
    playerHand = card1 + card2
    print(card1)
    print(card2)
    print("Player has",playerHand)
    return playerHand

def gameEnd(playerHand,dealerHand):
    if playerHand == 21 and dealerHand == 21:
        print("Impressive! Both the dealer and the player have reached Blackjack!")
        return True
    elif playerHand == 21:
        print("Well done! You have achieved Blackjack and beaten the dealer.")
        return True
    elif dealerHand == 21:
        print("Unfortunately the dealer has beaten you this time. They had Blackjack.")
        return True
    else:
        return False


#playersNumber = input("How many players are there? ")
#playersNumber = int(playersNumber)
#while playersNumber > 0:
    #player()
    #playersNumber = playersNumber - 1

dealerHand = dealer()
playerHand = player()

end = False

if playerHand == 21:
    print("Well done! You have gotten Blackjack and beaten the dealer!")
elif dealerHand == 21:
    print("Unlucky, the daealer has Blackjack and wins this round.")
    print("Better luck next time.")
else:
    print("Hmm. This message should not have appeared.")
    print("It seems that something went wrong.")

#gameEnd(playerHand,dealerHand)

while end == False:
    #if playerHand < 21:
    #print("Player has",playerHand)
    if playerHand == 21 or dealerHand == 21:
        if playerHand == 21:
            print("Well done! You have gotten Blackjack and beaten the dealer!")
        elif dealerHand == 21:
            print("Unlucky, the daealer has Blackjack and wins this round.")
            print("Better luck next time.")
    else:
        
        print("Would you like to twist or stick?")
        answer = input()
        if answer == "twist" or answer == "Twist" or answer == "TWIST" or answer == "t" or answer == "T":
            card1 = card()
            playerHand = playerHand + card1
            print(card1)
            print("Player has",playerHand)
            end = gameEnd(playerHand,dealerHand)
            print("NK:",end)
            #if end == True:
                #break
            #else:
                #pass
        elif answer == "stick" or answer == "Stick" or answer == "STICK" or answer == "s" or answer == "S":
            if dealerHand > 21:
                print("Dealer went bust.")
                print("Player wins.")
                end = True
            elif dealerHand < 16:
                card1 = card()
                dealerHand = dealerHand + card1
                print(card1)
                print("Dealer has",dealerHand)
                end = gameEnd(playerHand,dealerHand)
            elif playerHand > 21:
                print("Looks like you went bust, bad luck.")
                print("The dealer wins his round.")
            elif playerHand == 21 or dealerHand == 21:
                if playerHand == 21:
                    print("Well done! You have gotten Blackjack and beaten the dealer!")
                elif dealerHand == 21:
                    print("Unlucky, the daealer has Blackjack and wins this round.")
                    print("Better luck next time.")
                elif playerHand > dealerHand:
                    print("Well done! You have beaten the dealer.")
                    end = True
                    #break
                elif dealerHand > playerHand:
                    print("Unfortunately the dealer has beaten you this time.")
                    end = True
                    #break
                elif playerHand == dealerHand:
                    print("The game is a tie. Neither the dealer nor the player wins.")
                    end = True
                    #break
                else:
                    print("Hmm. This message should not have appeared.")
                    print("It seems that something went wrong.")
    
            #if end == True:
                #break
            #else:
                #pass
        #blocked to make sure player/ dealer win at 21 or go bust etc.
        #else:
            #if playerHand > dealerHand:
                #print("Well done! You have beaten the dealer.")
                #end = True
                #break
            #elif dealerHand > playerHand:
                #print("Unfortunately the dealer has beaten you this time.")
                #end = True
                #break
            #elif playerHand == dealerHand:
                #print("The game is a tie. Neither the dealer nor the player wins.")
                #end = True
                #break
            #else:
                #print("Hmm. This message should not have appeared.")
                #print("It seems that something went wrong.")
    
    #else:
        #print("Player has",playerHand)
        #print("Dealer has",dealerHand)
    #else:
        #print("This means you went bust.")
        #print("You have lost.")
        #end = True
print("Got to the end.")

#card1 = card()
#card2 = card()
#card3 = card()
#card4 = card()
#print(card1)
#print(card2)
#print(card3)
#print(card4)
