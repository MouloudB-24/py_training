
def ask_name():
    answer_name = ""
    while answer_name == "":
        answer_name = input("What is your name ? ")
    return answer_name



def ask_age(person_name):
    age_int = 0
    while age_int == 0: 
        try :
            age_int = int(input(f"{person_name}, How old are you? "))
        except ValueError:
            print("Error : You must enter a number for your age!")
    return age_int



def show_person_information(name, age, size=0):
    print(f"\nYour name is {name}, you will be {age + 1} years old next year!")
    if age == 1 or age == 2:
        print("Your are baby!")
    elif age < 10:
        print("You are a child")
    elif age < 17:
        print("You are a minor!")
    elif age == 17:
        print("You are almost an adult!")
    elif age == 18:
        print("Just an adult: Congratulations!")
    elif age <= 60:
        print("You are an adult!")
    else:
        print("You are a senior!")
    
    # shiw size
    if size != 0:
        print(f"Your size is : {size} m")
            
NB_PERSONNES = 1

# Sow results
for i in range(NB_PERSONNES):
    name = "Personne" + str(i+1)
    age = ask_age(name)
    show_person_information(name, age, 1.80)
