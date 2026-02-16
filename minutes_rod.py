# minutes.py
# Calculates the number of minutes in a given number of years

years = int(input("Enter the number of years: "))

minutes_per_year = 365 * 24 * 60
total_minutes = years * minutes_per_year

print("The number of minutes in", years, "years is", total_minutes)
