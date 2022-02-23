monthlyInterest = annualInterestRate / 12
lower = balance / 12
higher = (balance *(1+monthlyInterest)**12)/12.0
temp = balance
month = 0

while balance != 0:     
    i = ((lower + higher) / 2)
    balance = temp
    while month < 12:
        month +=1
        balance = balance - i
        interest = balance * (annualInterestRate / 12)
        balance = balance + interest
    month = 0
    if balance <= 0:
        higher = i
    elif balance >= 0:
        lower = i
    balance = float(round(balance, 2))

print('Lowest payment: ' + str(round(i, 2)))
