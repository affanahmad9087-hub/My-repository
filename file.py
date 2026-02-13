import apv_calc
shape_choice = input("Enter shape (circle, rectangle, triangle, square, cylinder): ").lower()
cal_choice = input("Enter calculation (area, perimeter, volume): ")

if cal_choice == "area":
    result = apv_calc.calculate_area(shape_choice)
    print(f"The area of the {shape_choice} is: {result}")
elif cal_choice == "perimeter":
    result = apv_calc.calculate_perimeter(shape_choice)
    print(f"The perimeter of the {shape_choice} is: {result}")
elif cal_choice == "volume":
    result = apv_calc.calculate_volume(shape_choice)
    print(f"The volume of the {shape_choice} is: {result}")
else:
    print("Invalid calculation choice. Please choose area, perimeter, or volume.")
