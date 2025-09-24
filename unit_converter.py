# Program : Unit Converter - 09/2025
from my_functions_library import ask_user_for_numeric_value

CONVESIONS = (
    ("pouces", "cm", 2.54),              
    
    ("m", "cm", 1000),
    
    ("km", "miles", 0.621371),
    
    ("lettre", "gallon", 0.264172),
)

def perform_and_show_conversion(unit1: str, unit2: str, factor: float, reverse: bool = False):
    """Convert units unit1 to unit2

    Args:
        unit1 (str): unit to convert
        unit2 (str): converted unit
        factor (float): multiplier factor between units

    Returns:
        True: user does not want to convert (quit th program)
        False: user provide a value to convert
    """
    if reverse:
        unit1, unit2, factor = unit2, unit1, 1/factor
        
    str_value = input(f"\nConversion {unit1} --> {unit2}. Enter the value in {unit1} (or 'q' to quit): ")
    if str_value == "q":
        print("Goodbye!")
        return True
    try:
        float_value = float(str_value)
    except ValueError:
        print("Error: You must enter a numeric value (use a point pfor decimals)")
        return perform_and_show_conversion(unit1, unit2, factor)
    
    converted_value = round(float_value * factor, 3)
    print(f"Conversion result: {float_value} {unit1} = {converted_value} {unit2}\n")
    return False


# Main menu
print("Welcome to the Unit Converter")
i = 1
for c in CONVESIONS:
    unit1 = c[0]
    unit2 = c[1]
    print(f"{i} - {unit1} to {unit2}")
    print(f"{i+1} - {unit2} to {unit1}")
    i += 2
    
max_choice_value = i - 1
choice = ask_user_for_numeric_value(1, max_choice_value)

index = (choice - 1) // 2
reverse = choice % 2 == 0

unit1, unit2, factor = CONVESIONS[index]

while True:
    # Ask the user for the values to convert
    if perform_and_show_conversion(unit1, unit2, factor, reverse):
        break
