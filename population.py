population = float(input("Enter the initial population: "))
growth_rate = float(input("Enter the growth rate: "))
hours_per_growth = float(input("Enter the hours needed for this growth rate: "))
total_hours = float(input("Enter the total hours of growth: "))

number_of_growths = total_hours / hours_per_growth
final_population = population * (growth_rate ** number_of_growths)

print("The predicted population is:", final_population)
