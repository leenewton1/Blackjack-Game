import random
import os
import time

end = False
Cards = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10 ,10, 10, 10]
Deck = Cards * 4  #4 Suits of each card


#Initial Draw Functions
def clear():
  os.system('clear')
def start_draw():
  C1 = random.randint(0,51)  #52 Total Cards, 51 Max Range due to start from 0
  C2 = random.randint(0,51) #Draw Card 2
  while C2 == C1: #Ensures C2 is different from C1
    C2 = random.randint(0,51)
  C3 = random.randint(0,51) #Draw Card 3
  while C3 == C1 or C3 == C2: #Ensures C3 is unique
    C3 = random.randint(0,51)
  return C1, C2, C3

def assign_p(player_hand):
  player_h = []
  for cards in player_hand:
    player_h.append(Deck[cards])
  return player_h

def assign_d(dealer_hand):
  dealer_h = []
  for cards in dealer_hand:
    dealer_h.append(Deck[cards])
  return dealer_h

def count_p(player_h):
  player = 0
  for cards in player_h:
    if cards == 1 and player < 11: 
      player += 11 #Assigns ace as 11 if player less than 11
    else:
      player += cards
  return player

def count_d(dealer_h):
  dealer = 0
  for cards in dealer_h:
    if cards == 1 and dealer < 11: 
      dealer += 11 #Assigns ace as 11 if player less than 11
    else:
      dealer += cards
  return dealer

def blackjack(player):
  blackjack = False
  if player == 21:
    blackjack = True
  return blackjack

def display(player, dealer, player_hand, dealer_hand):
  print(f"Your cards are {player_h}, total:{player}")
  print(f"Dealer has {dealer_h}, total:{dealer}\n")

#Draw Cards Functions
def draw_check():
  check = True
  ans = ''
  while check == True:
    print("Do you want to draw a card?")
    ans = input("Y/N: ").lower()
    if ans == 'y' or ans == 'n':
      check = False
    else:
      print("\nPlease input 'Y' or 'N' only.")
      check = True
  if ans == 'y':
    draw = True
  else:
    draw = False
  clear()
  return draw
  
def draw_h(player_hand, player_h):
  unique = False
  while unique == False: #Ensures card is unique
    x = random.randint(0,51) 
    for cards in player_hand:
      if x == cards:
        unique = False
        break
      else:
        unique = True
  print("You drew a card")
  print(f"You drew {Deck[x]}\n")
  player_h.append(Deck[x])
  return player_h

def draw_d(dealer_hand, dealer_h):
  unique = False
  while unique == False: #Ensures card is unique
    x = random.randint(0,51) 
    for cards in dealer_hand:
      if x == cards:
        unique = False
        break
      else:
        unique = True
  print("The dealer drew a card")
  print(f"He drew {Deck[x]}\n")
  dealer_h.append(Deck[x])
  return dealer_h

def bust(x):
  if x > 21:
    bust = True
    print("You're Bust!")
    return bust

def compare(player, dealer):
  if player > dealer or dealer > 21:
    print("Congratulations!")
    print("You Won!")
  elif player == dealer:
    print("Game Over, You're tied")
  else:
    print("Game Over, Dealer won.")
  
#Intial Draw
print("Welcome to Blackjack\n" "Dealer stands on all 17s\n")
C1, C2, C3 = start_draw()
player_hand = [C1, C3]
dealer_hand = [C2]
player_h = assign_p(player_hand)
dealer_h = assign_d(dealer_hand)
player = count_p(player_h)
dealer = count_d(dealer_h)
blackjack = blackjack(player)
display(player, dealer, player_h, dealer_h)
if blackjack == True:
  print("You Got Blackjack!")
  end = True

#Draw Cards
while end == False:
  draw = draw_check()
  if draw == True:
    player_h = draw_h(player_hand, player_h)
    player = count_p(player_h)
    display(player, dealer, player_h, dealer_h)
    bust = bust(player)
    if player == 21:
      draw = False
    if bust == True:
      end = True
  else:
    while dealer<17:
      print("Dealer is drawing a card...\n")
      time.sleep(1)
      dealer_h = draw_d(dealer_hand, dealer_h)
      dealer = count_d(dealer_h)
      display(player, dealer, player_h, dealer_h)
      time.sleep(4)
      clear()
    display(player, dealer, player_h, dealer_h)
    end = True
if bust == True:
  print("Game Over,\n" "You Lose.")
else:
  compare(player, dealer)
