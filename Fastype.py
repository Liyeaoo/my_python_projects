import time
print("Welcome to Fastype!\n")
time.sleep(1.5)


print("This game's goal is to make you a fast typer!")
time.sleep(1)

print("Options:\n" + "Easy mode\n" + "Normal mode\n" + "Hard mode\n")
time.sleep(0.5)
answer = input("What mode do you want to choose?\n\n" + "options above!\n\n""")
if answer == "Easy mode":
  print("\nFeeling easy today? Sure! " + "Generating words in progress\n")
  time.sleep(2.5)
  typed=input("Apple rights solo greetings paintings everybody professionally\n")
  timer = 10
  if typed =="Apple rights solo greetings paintings everybody professionally":
      print("Great job!")
  else:
      print("Wrong!")
elif answer == "Normal mode":
  print("Normal is always midmost! " + "Generating words " + "in progress")
  #CONTINUE LATER BY ADDING A HARD MODE, OPTIMIZING THE CODE, AND MAKING ELSE STATEMENTS
elif answer== "Hard mode":
 print("Want to challenge yourself? " + "Heh... " + "Get ready! " + "Generating words in progress")
