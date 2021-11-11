
def questionAppleOrange():
    apple_Q = int(input("How many apples do you want to buy? "))
    orange_Q = int(input("How many oranges do you want to buy? "))
    return apple_Q, orange_Q

def price(appleNumber, orangeNumber):
    apple_P = appleNumber * 20
    orange_P = orangeNumber * 25
    total = apple_P + orange_P
    return total 

apples, oranges = questionAppleOrange()
total = price(apples, oranges)

print(f"The total amount is {total}.")