import art
print(art.logo)
def highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bids in bidding_record:
        bid_amt=bidding_record[bids]
        if bid_amt>highest_bid:
            highest_bid=bid_amt
            winner=bids
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bid={}
should_continue = True
while should_continue:
    name=input("What is your name?: ")
    price=float(input("What is your bid: $"))
    bid[name]=price
    next_action=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if next_action=="no":
        should_continue=False
        highest_bidder(bid)
    elif next_action=="yes":
        print("\n"*20)
