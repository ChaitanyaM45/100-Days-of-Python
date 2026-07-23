import random

word_list = ["rohit", "chaitanya", "pranav", "yash", "vedant", "pratham", "pramod"]

chosen_word=random.choice(word_list)
# print(chosen_word)
display=[]
for letter in chosen_word:
    display.append('_')

lives=6
while '_' in display and lives>0:
    print(display)
    guess=input("Guess the letter:")
    guess=guess.lower()

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=guess
    else:
        lives-=1
        print("Wrong Guess")
        print(f"Lives Left: {lives}")

print(display)
if '_' not in display:
    print("You Win")
else:
    print("You Lose")
    print("The word was", chosen_word)