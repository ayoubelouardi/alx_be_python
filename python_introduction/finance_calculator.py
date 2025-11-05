annual_intereset = 0.05

income_per_month = int(input("Enter your monthly income: "))
expenses_per_month = int(input("Enter your total monthly expenses: "))

savings_per_month = income_per_month - expenses_per_month


projected_saving = (savings_per_month * 12 + (savings_per_month * 12 * 0.05))


print("Your monthly savings are $", savings_per_month, ".", sep="")
print("Projected savings after one year, with interest, is: $", (projected_saving), ".", sep="")
