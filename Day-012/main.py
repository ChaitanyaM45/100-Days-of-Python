import art, random
print(art.logo)
print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 to 100!")
num=random.randint(1,100)
diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
lives=0
if diff == 'easy':
    lives=10
else:
    lives=5
while lives > 0:
    print(f"You have {lives} lives left.")
    user_num=int(input("Make a guess: "))
    if user_num == num:
        print(f"You got it! The answer was {num}.")
    else:
        lives-=1
        if lives==0:
            print("You've run out of guesses.")
            break
        if user_num > num:
            print("Too high!\nGuess again.")
        else:
            print("Too low!\nGuess again.")