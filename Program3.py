
def askmoneyAappleP():
    money_A = float (input("How much money do you have: "))
    apple_P = float (input("Enter the price of the apple: "))
    return money_A, apple_P

def appleTmoneyL(money, price):
    apple_T = int(money//price)
    money_L = money%price
    return apple_T, money_L

money_, price_ = askmoneyAappleP()
totalA, leftM = appleTmoneyL(money_, price_)

print(f"You can buy {totalA} apples and your change is {leftM} pesos.")