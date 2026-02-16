for i in range(3):
    print(f"\nTriangle #{i + 1}:")
    
    # Get inputs
    base = float(input("Enter the triangle's base: "))
    height = float(input("Enter the triangle's height: "))
    
    # Calculate area
    area = 0.5 * base * height
    
    # Print the result
    print(f"The area of triangle #{i + 1} is {area} square units.")
