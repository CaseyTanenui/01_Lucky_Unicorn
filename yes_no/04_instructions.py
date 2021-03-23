# Functions go here...
def yes_no(question):...

def instructions():
  print("*** How to Play ***")
  print()
  print("The rules of the game go here")
  print()
  return ""


# Main routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
  instructions()

print("Program Continues")