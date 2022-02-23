temp = balance
i = 0
minPayment = 0

while balance != 0 and balance > 0 :
    minPayment += 10
    balance = temp
    while i < 12:
        i +=1
        balance = balance - minPayment
        interest = balance * (annualInterestRate / 12)
        balance = balance + interest
    i = 0
print("Lowest Payment: ", minPayment)
