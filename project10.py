price = float(input("Enter the purchase price: "))

downPaymentRate = 0.10
annualRate = 0.12
monthlyRate = annualRate / 12
months = 24

downPayment = price * downPaymentRate
balance = price - downPayment

# Payment that amortizes the balance to 0 in exactly 24 months
if monthlyRate == 0:
    monthlyPayment = balance / months
else:
    monthlyPayment = balance * (monthlyRate / (1 - (1 + monthlyRate) ** (-months)))

print("\nDown payment: $", format(downPayment, ",.2f"), sep="")
print("Monthly payment: $", format(monthlyPayment, ",.2f"), sep="")

print("\nMonth\tBalance\t\tInterest\tPrincipal\tPayment\t\tRemaining")
print("----------------------------------------------------------------------")

for month in range(1, months + 1):
    interest = balance * monthlyRate
    principal = monthlyPayment - interest
    payment = monthlyPayment

    # Last payment adjustment to guarantee remaining balance is exactly 0.00
    if month == months:
        principal = balance
        payment = interest + principal

    remaining = balance - principal

    # Avoid negative pennies from floating point rounding
    if remaining < 0:
        remaining = 0.0

    print(month,
          "\t$" + format(balance, ",.2f"),
          "\t$" + format(interest, ",.2f"),
          "\t\t$" + format(principal, ",.2f"),
          "\t$" + format(payment, ",.2f"),
          "\t$" + format(remaining, ",.2f"))

    balance = remaining
