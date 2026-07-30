def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operation={
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
import art
should_continue=True
while should_continue:
    print(art.logo)
    n1=float(input("Enter the first number: "))
    for symbol in operation:
        print(symbol)
    op_symbol=input("Enter the operation: ")
    n2=float(input("Enter the second number: "))
    answer=operation[op_symbol](n1,n2)
    print(f"{n1} {op_symbol} {n2} = {answer}")
    choice=input("Do you want to continue? (y/n): ")
    if choice=="y":
        should_continue=True
    else:
        should_continue=False