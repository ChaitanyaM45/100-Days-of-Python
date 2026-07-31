import art, game_data, random
data=game_data.data
print(art.logo)
should_continue=True
points=0
a=random.choice(data)
b=random.choice(data)
while a==b:
    b=random.choice(data)

while should_continue:
    a_name=a["name"]
    a_desc=a["description"]
    a_country=a["country"]
    b_name=b["name"]
    b_desc=b["description"]
    b_country=b["country"]
    print(f"Compare A: {a_name}, a {a_desc}, from {a_country}")
    print(art.vs)
    print(f"Against B: {b_name}, a {b_desc}, from {b_country}")
    action=input("Who has more followers? Type 'A' or 'B': ").lower()

    if a["follower_count"]>b["follower_count"]:
        correct="a"
    else:
        correct="b"

    if action==correct:
        should_continue=True
        points+=1
        a=b
        b=random.choice(data)
        while a==b:
            b=random.choice(data)
        print("\n"*20)
        print(art.logo)
        print(f"You're right! Current score: {points}.")
    else:
        should_continue=False
        print(f"Sorry, that's wrong. Final score: {points}")