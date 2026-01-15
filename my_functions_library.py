def ask_user_for_numeric_value(min_value: str, max_value: str):
    entered_value_str = input(f"\nEnter your choice between {min_value} and {max_value}: ")
    
    try:
        entered_value_int = int(entered_value_str)
    except ValueError:
        print("You must enter a numeric value\n")
        return ask_user_for_numeric_value(min_value, max_value)
    
    if not (min_value <= entered_value_int <= max_value):
        print(f"You must enter a value between {min_value} and {max_value}\n")
        return ask_user_for_numeric_value(min_value, max_value)
    
    return entered_value_int
