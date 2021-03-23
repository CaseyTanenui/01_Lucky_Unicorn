# Functions go here...
def num_check(question, low, high): 
  error = "Please enter an whole number between 1 and 10\n"

valid = False 
while not valid:
  try:
    # Ask the quesion
   response = int(input(question))
    # If the amount is too low / too high give 
    if low < response <= high :
       return response 
      # Output an error 
      else:
        print(error)
        
      except ValueError:
        print(error)

# Main routine goes here...

error = "Please enter a whole number between 1 and 10"

valid = False 
while not valid:
  # Ask the question 
  response = int(input("How much would you like to play with?"))
  
  # If the ammount is too low / too high give 
  if 0 < response <= 10:
    print("You have asked to Play with ${}".format(response))

  # Output the error 
  else:
    print(error)
  
except ValueError 
