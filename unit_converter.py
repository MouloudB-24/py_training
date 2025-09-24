# Program : Unit Converter - 09/2025

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
        unit1, unit2, factor = unit2, unit1, round(1/factor, 3)
        
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



while True:
    # conversion choice menu
    print("Welcome to the Unit Converter")
    print("1 - Inches to Cm")
    print("2 - Cm to Inches")

    choice = input("\nYour choice (1 or 2) : ")
    if choice == "1" or choice == "2":
        break
    print("Error: You must chooce 1 or 2\n")

while True:
    # Ask the user for the values to convert
    if perform_and_show_conversion("inches", "cm", 2.54, reverse=False if choice=="1" else True):
        break