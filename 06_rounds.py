import random

# Set balance for testing purposes...
balance = 5 

rounds_played = 0

play_again = input("Press <Enter> to Play...").lower()
while play_again == "":

  # Increase # of rounds played 
  rounds_played += 1

  # Print round number  
  print()
  print("*** Round #{} ***".format(rounds_played))
  
  chosen_num = random.randint(1 , 100)

  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    balance += 4
  
  # If the random # is is between 6 and 36
  # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    balance -= 1

  # The token is either a horse or a zebra 
  # In both cases, subtract $0.50 from balance  
  else:
    # If the chosen number is even
    # Item to a horse
    if chosen_num % 2 == 0:
      chosen = "horse"
    
    # Otherwise set it to a zebra   
    else:
      chosen = "zebra"
    balance -= 0.5

  print("You got a {}, your balance is ${:.2f}".format(chosen, balance))

  if balance < 1:
    play_again = "xxx"
    print("Sorry you have run out of money to play with")
  else:
    play_again = input("Press Enter to play again, or 'xxx' to quit")

print()
print("Final balance" , balance) 