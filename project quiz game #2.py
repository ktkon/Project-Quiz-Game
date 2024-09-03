print("Welcome to the Quiz Game")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Let's start!")
score = 0

answer = input("Who is the president of the USA? ")
if answer == "joe biden":
    score += 1
    print("The answer is correct. Good Job!")
else:
    print("Incorrect answer!")

answer = input("Who is the CEO of Tesla? ")
if answer == "elon musk":
    score += 1
    print("The answer is correct. Good Job! ")
else:
    print("Incorrect answer!")

answer = input("Who is the president of Poland? ")
if answer == "andrzej duda":
    score += 1
    print("The answer is correct. Good Job!")
else:
    print("Incorrect answer!")

answer = input("Which band recorded 'Smells like teen spirit'? ")
if answer == "nirvana":
    score += 1
    print("The answer is correct. Good Job!")
else:
    print("Incorrect answer!")

answer = input("Who is the most beautiful girl in the world? ")
if answer == "alina":
    score += 1
    print("The answer is correct. Good Job!")
else:
    print("Incorrect answer!")

print("You've got a score of " + str(score) + " points")
