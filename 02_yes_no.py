#Functions go here..

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

# Main routine goes here...

show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("You said {} to having fun".format(having_fun))

show_instructions = ""
while show_instructions != "xxx":

  # .lower() makes things lowercase (not UPPERCASE)
  show_instructions = input("Have you played before? ").lower()

  if show_instructions == "yes" or show_instructions == "y":
    print("program continues")
  elif show_instructions == "no" or show_instructions == "n":
    print("display instructions")
  else: 
    print("please enter yes / no")

  print()
