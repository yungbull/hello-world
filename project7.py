startingSalary = float(input("Enter the starting salary: "))
increaseRate = float(input("Enter the percentage increase: "))
years = int(input("Enter the number of years: "))

salary = startingSalary

print("\nYear\tSalary")
print("----------------")

for year in range(1, years + 1):
    print(year, "\t$", format(salary, ",.2f"), sep="")
    salary += salary * (increaseRate / 100)
