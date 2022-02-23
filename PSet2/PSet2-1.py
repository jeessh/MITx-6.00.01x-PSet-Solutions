monthlyInterest = annualInterestRate/12.0

i = 0
while i < 12:

    minMonthlyPayment = monthlyPaymentRate * balance

    monthlyUnpaid = balance - minMonthlyPayment

    updatedBalance = monthlyUnpaid + monthlyInterest * monthlyUnpaid

    balance = updatedBalance

    i += 1

print("Remaining balance: " + str(round(updatedBalance, 2)))

