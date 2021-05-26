import random

tries = 0

print("Hey There! Whats Your Name? ")
name = input()

Numbers = random.randint(1, 100)
print("Alright " + name + " Can You Guess the Number Between 1 And 100.")
print("You`ve Got 10 lives, Use Them Wisely")

choose = input()
while tries < 10:
    print("Choose a Number: ")
    choose = input()
    choose = int(choose)

    tries = tries + 1

    if choose <= Numbers:
        print('Too Low Bro')

    if choose >= Numbers:
        print('Too High Bro')

    if choose == Numbers:
        break

if choose == Numbers:
    tries = str(tries)
    number = str(Numbers)
    print("Wahoo " + name + "! You Right My Number is " + number + " And It Only Toke You " + tries + " Tries To Get It!!!")
    print("GAME OVER")

if choose != Numbers:
    number = str(Numbers)
    print("Sorry, But The Number Was " + number)
    print("Better Luck Next Time")
    print("GAME OVER")
