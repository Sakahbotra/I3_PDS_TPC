total_balance = 5000
bucks_100 = 50
bucks_50 = 100
bucks_20 = 75
bucks_10 = 250
bucks_5 = 200
bucks_1 = 1000

transactionAmount = int(input("Enter the transaction amount: "))
if transactionAmount > total_balance:
    print("You don't have enough balance to make this transaction.")
else:
    total_balance -= transactionAmount
    print("Transaction successful.")
    print("Your new balance is:", total_balance)

while transactionAmount > 0:
    if(transactionAmount // 100) and (bucks_100 > 0):
        b_100 = transactionAmount // 100
        bucks_100 -= b_100
        transactionAmount %= 100
    elif(transactionAmount // 50) and (bucks_50 > 0):
        b_50 = transactionAmount // 50
        bucks_50 -= b_50
        transactionAmount %= 50
    elif(transactionAmount // 20) and (bucks_20 > 0):
        b_20 = transactionAmount // 20
        bucks_20 -= b_20
        transactionAmount %= 20
    elif(transactionAmount // 10) and (bucks_10 > 0):
        b_10 = transactionAmount // 10
        bucks_10 -= b_10
        transactionAmount %= 10
    elif(transactionAmount // 5) and (bucks_5 > 0):
        b_5 = transactionAmount // 5
        bucks_5 -= b_5
        transactionAmount %= 5
    elif(transactionAmount // 1) and (bucks_1 > 0):
        b_1 = transactionAmount // 1
        bucks_1 -= b_1
        transactionAmount %= 1
