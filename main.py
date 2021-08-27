import random

intro = """
Think of a number from 0 to 1000.
And I will guess it in max 10 attempts.
"""
print(intro)

min = 0
max = 1000
guess = 0


def hint_analyzer(hint):
    while True:
        if hint == "you win":
            print("I win!")
            return False
        elif hint == "too big":
            global max
            max = guess
            return True
        elif hint == "too small":
            global min
            min = guess
            return True


while True:
    guess = int(((max - min) / 2) + min)
    print(f"My guess: {guess}")
    hint = input("Give me a hint: too small/too big/you win: ")
    if hint_analyzer(hint) is False:
        break
