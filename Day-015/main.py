MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please Insert Coins:")
    total=int(input("how many quarters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.1
    total+=int(input("how many nickel?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        global money
        money=drink_cost
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here if your {coffee_name} coffee ☕")

money=0

while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            profit=process_coins()
            if is_transaction_successful(profit, drink["cost"]):
                make_coffee(choice,drink["ingredients"])