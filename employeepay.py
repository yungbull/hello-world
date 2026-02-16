# employeepay.py
# Calculates an employee's total weekly pay

hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the number of regular hours: "))
overtime_hours = float(input("Enter the number of overtime hours: "))

regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * (1.5 * hourly_wage)

total_pay = regular_pay + overtime_pay

print("The employee's total weekly pay is $", total_pay)
