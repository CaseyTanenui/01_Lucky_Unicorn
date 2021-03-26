import random

# Functions go here...
def num_check(question, low, high): 
  error = "Please enter an whole number between 1 and 10\n"

  valid = False 
  while not valid:
    try:
      # Ask the quesion
      response = int(input (question))
      # If the amount is too low / too high give 
      if low < response <= high:
        return response 

      # Output an error 
      else:
        print(error)
      
    except ValueError:
      print(error)


def yes_no(question):
  valid  = False
  while not valid:
    response = input (question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else:
      print("Please answer yes/no")


def show_instructions():
  print("Instructions go here")
  print()
  return ""


def statement_generator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration *len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)
  
  return ""

# main routine goes here

# initialise variables
rounds_played = 0

# get input from user etc...
print("*** Welcome to the Lucky Unicorn Game ***")
print()

need_instructions = yes_no("Have you played before? ")

if need_instructions == "no":
  show_instructions()

balance = num_check("How much do you want to play with? ", 1, 10)


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
    chose_dec = "*"
    balance += 4
  
  # If the random # is is between 6 and 36
  # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    chose_dec = "D"
    balance -= 1

  # The token is either a horse or a zebra 
  # In both cases, subtract $0.50 from balance  
  else:
    # If the chosen number is even
    # Item to a horse
    if chosen_num % 2 == 0:
      chosen = "horse"
      chose_dec = "H"
    
    # Otherwise set it to a zebra   
    else:
      chosen = "zebra"
      chose_dec = "Z"
    balance -= 0.5

  print()
  feedback = "You got a {}, your balance is ${:.2f}".format(chosen, balance)
  statement_generator(feedback, chose_dec)

  if balance < 1:
    play_again = "xxx"
    print("Sorry you have run out of money to play with")
  else:
    play_again = input("Press Enter to play again, or 'xxx' to quit")

print()
print("Final balance" , balance) 