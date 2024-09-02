print("Welcome to the Quiz Game!")

AskToPlay = input("Would you like to play? ")

if AskToPlay.lower() != "yes":
    quit()

print("Okay! Lets play :)")
score = 0

answer = input("What is the name of microsoft CEO? ")
if answer.lower() == "bill gates":
    print("That's a correct answer. Well done!")
    score = score + 1
else:
    print("Wrong answer!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("That's a correct answer. Well done!")
    score = score + 1
else:
    print("Wrong answer!")

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("That's a correct answer. Well done!")
    score = score + 1
else:
    print("Wrong answer!")

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("That's a correct answer. Well done!")
    score = score + 1
else:
    print("Wrong answer!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " %.")
