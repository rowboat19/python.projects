print("Welcome to my Jojo's Bizzare Adventure Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("ORA! Let's play. Approach me!")
score = 0

answer = input("What is Jotaro's favorite color? ")
if answer.lower == "purple":
    print("ORA! Good Job. Keep going!")
    score += 1
else:
    print("WRONG! KILL DA HO!!! ORA ORA ORA ORA ORA! TRY AGAIN!")

answer = input("What is Dio's hair color? ")
if answer.lower == "yellow":
    print("ORA! Good Job. Keep going!")
    score += 1
else:
    print("WRONG! KILL DA HO!!! ORA ORA ORA ORA ORA! TRY AGAIN!")

answer = input("What is Joseph's best battle tactic? ")
if answer.lower == "running away":
    print("ORA! Good Job. Keep going!")
    score += 1
else:
    print("WRONG! KILL DA HO!!! ORA ORA ORA ORA ORA! TRY AGAIN!")

answer = input("What is Johnathan Joestar have on his left shoulder blade? ")
if answer.lower == "a star":
    print("ORA! Good Job. Keep going!")
    score += 1
else:
    print("WRONG! KILL DA HO!!! ORA ORA ORA ORA ORA! TRY AGAIN!")

print("You got " + str(score) + " questions correct! Good Job!")
print("You got " + str((score/4) * 100) + "%.") 