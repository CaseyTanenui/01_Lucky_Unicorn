
keep_going = ""
while keep_going == "":

  # .lower() makes things lowercase (not UPPERCASE)
  show_instructions = input("Have you played before? ").lower()

  if show_instructions == "yes":
    print("program continues")
  elif show_instructions == "no":
    print("display instructions")
  else: 
    print("please enter yes / no")

  print()

