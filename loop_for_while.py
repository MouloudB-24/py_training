input_string =input("Enter a list of numbers separated by a comma : ", )
number_list = input_string.split(",")
number_list = [int(number) for number in number_list]

sum = 0
for number in number_list:
    sum = sum + number
print(sum)

average = sum / len(number_list)
print(average)

i = 0 
for number in number_list:
    if number > average:
        i = i + 1
print(i)

j = 0
for number in number_list:
    if number%2 == 0:
        j = j + 1
print(j)

    

