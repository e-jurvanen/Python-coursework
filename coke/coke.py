due = 50

while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert Coin: "))
    if coin == 25:
        due = due - coin
    elif coin == 10:
        due = due - coin
    elif coin == 5:
        due = due - coin
    else:
        continue

if due == 0:
    print("Change Owed: 0")
else:
    print("Change Owed:", -due)
