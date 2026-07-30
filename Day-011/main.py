import art,random

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,comp_score):
    if user_score==comp_score:
        print("Its a draw!")
    elif user_score==0:
        print("You Win :), Its a BLACKJACK")
    elif comp_score==0:
        print("You Lose :(, Its a Computers BLACKJACK")
    elif user_score>21:
        print("You Went Over, You Lose :(")
    elif comp_score>21:
        print("Computer Went Over, You Win :)")
    elif user_score>comp_score:
        print("You Win :(")
    else:
        print("You Lose :(")

def play_game():
    print(art.logo)
    user=[]
    comp=[]
    user_score=-1
    comp_score=-1
    is_game_over=False
    for _ in range(2):
        user.append(deal_cards())
        comp.append(deal_cards())

    while not is_game_over:
        user_score=calculate_score(user)
        comp_score=calculate_score(comp)
        print(f"Your Cards: {user}, Your Score: {user_score}")
        print(f"Computer's First Cards: {comp[0]}")

        if user_score==0 or comp_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if user_should_deal=="y":
                user.append(deal_cards())
            else:
                is_game_over=True

        while comp_score!=0 and comp_score<21:
            comp.append(deal_cards())
            comp_score=calculate_score(comp)

        print(f"Your Final Hands: {user}, Your Final Score: {user_score}")
        print(f"Computer Final Hands: {comp}, Computer Final Score: {comp_score}")
        compare(user_score,comp_score)

play_game()