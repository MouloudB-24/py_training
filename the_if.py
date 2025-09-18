""" The calculator """

number_on_left = 10
number_on_right = 20
symbol = "+"
result = 0

if not (isinstance(number_on_left, int) and isinstance(number_on_right, int)):
    print("Left_number and Right_number must be integers")
    exit()

match symbol:
    case "+":
        print('The symbol is an addiction')
        result = number_on_left + number_on_right
        print(result)
    case "-":
        print("The symbol is a subtraction")
        result = number_on_left - number_on_right
        print(result)
    case "*":
        print("The symbol is a multiplication")
        result = number_on_left * number_on_right
        print(result)
    case "/":
        print("The symbol is a division")
        if number_on_right == 0:
            print("Impossible to divide by zero")
        else:
            result = number_on_left / number_on_right
            print(result)
    case _:
        print("The symbol is not an authorized operation.")
        exit()






