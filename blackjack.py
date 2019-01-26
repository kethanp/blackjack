import itertools
import random
import time
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
global deck
deck= list(itertools.product(vals, suits))
random.shuffle(deck)
PlayerHand=[]
DealerHand=[]


def cardvalue(hand):
    value=0
    for card in range(len(hand)):
        if hand[card][0] == '2':
            value+=2
        if hand[card][0] == '3':
            value+=3
        if hand[card][0] == '4':
            value+=4
        if hand[card][0] == '5':
            value+=5
        if hand[card][0] == '6':
            value+=6
        if hand[card][0] == '7':
            value+=7
        if hand[card][0] == '8':
            value+=8
        if hand[card][0] == '9':
            value+=9
        if hand[card][0] == '10' or hand[card][0] == 'jack' or hand[card][0] == 'queen' or hand[card][0]== 'king':
            value+=10
        if hand[card][0] == 'ace':
            value+=11
    
    if value>21:
        for i in range(len(hand)):
            if 'ace'== hand[i][0]:
                value=value-10
            
    return (value)
            
def ODH():
    DealerHand.append(deck[0])
    del deck[0]
    DealerHand.append(deck[0])
    del deck[0]
    DHV=cardvalue(DealerHand)
    print("Dealers Card: " + str(DealerHand[0]))

def OPH():
    PlayerHand.append(deck[0])
    del deck[0]
    PlayerHand.append(deck[0])
    del deck[0]
    PHV=cardvalue(PlayerHand)
    print("Player Hand: "+ str(PlayerHand))
    print("Your Hand Value: "+str(PHV))
    
def NewHand():
    DealerHand.clear()
    PlayerHand.clear()

def hit(hand):
    hand.append(deck[0])
    del deck[0]
    
def DealerPlay(hand):
    DHV=cardvalue(DealerHand)
    while DHV<17:
        hit(DealerHand)
        DHV=cardvalue(DealerHand)
    else:
        return DHV
        
def show():
    print("Dealer Hand Value: "+str(cardvalue(DealerHand)))
   
def blackjack():
    while True:
        global deck
        if len(deck)<24:
            deck= list(itertools.product(vals, suits))
            random.shuffle(deck)
            print (deck)
        print('')
        ODH()
        OPH()
        if cardvalue(DealerHand) == 21:
            if cardvalue(PlayerHand) == 21:
                print('push')
                show()
                NewHand()
                time.sleep(0.0001)
                continue
            else:
                print('lose: dealer blackjack')
                show()
                NewHand()
                time.sleep(0.0001)
                continue
        if cardvalue(PlayerHand) == 21:
            print('win: player backjack')
            show()
            NewHand()
            time.sleep(0.0001)
            continue


        playerLose=True

        while playerLose:
            playeroption = (input('Do you want to hit(1) or hold(2): '))
            if playeroption == '1':
                hit(PlayerHand)
                print(PlayerHand)
                print(cardvalue(PlayerHand))
                if cardvalue(PlayerHand)> 21:
                    print('lose: player bust')
                    show()
                    NewHand()
                    time.sleep(0.0001)
                    playerLose=False
                    continue
                
                continue
            if playeroption == '2':
                break
            else:
                continue
        if playerLose==False:
            continue
        DealerPlay(DealerHand)
        if cardvalue(DealerHand)> 21:
            print('Win: Dealer Bust')
            show()
            NewHand()
            time.sleep(0.0001)
            continue
        elif cardvalue(DealerHand) > cardvalue(PlayerHand):
            print('Lose: Dealer Has The Best Score')
            show()
            NewHand()
            time.sleep(0.0001)
            continue
        elif cardvalue(DealerHand) < cardvalue(PlayerHand):
            print('Win: Player Has The Best Score')
            show()
            NewHand()
            time.sleep(0.0001)
            continue
        else:
            print('push')
            show()
            NewHand()
            time.sleep(0.0001)
            continue
        
        
        
        