height = float(input("Enter the initial height: "))
bounces = int(input("Enter the number of bounces: "))

bounce_index = 0.6
total_distance = height

for count in range(bounces):
    height = height * bounce_index
    total_distance = total_distance + (2 * height)

print("Total distance traveled:", total_distance)
