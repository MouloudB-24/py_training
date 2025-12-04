# # ----------------- 17 Octobre 25 -----------------------
# def mask(card):
#     operator = "-"
#     if "-" not in card:
#         operator = " "
#     card = card.split(operator)
#     for index in range(3):
#         card[index] = ""  * 4
#     card = operator.join(card)
#     return card

# # print(mask("6011 1111 1111 1117"))


# # ----------------- 19 Octobre 25 -----------------------
# def extract_attributes(element):
#     if not "=" in element:
#         return []
    
#     attributs = []
#     opeartor = ">"
#     if "/>" in element:
#         opeartor = "/>"
#     element = element.replace('"', '')
#     element_clean = element.split(opeartor)[0]
#     attribut_clean = element_clean.split(" ")[1:]
    
#     for attribut in attribut_clean:
#         if attribut:
#             if "=" in attribut:
#                 attributs.append(f'{attribut}')
#             else:
#                 attributs[-1] = attributs[-1].rstrip('"') + f' {attribut}'
    
#     attributs_final = []
#     for attribut in attributs:
#         attributs_final.append(attribut.replace("=" , ", "))

#     return attributs_final


# # print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))

# # ----------------- 18 Octobre 25 -----------------------
# def sock_pairs(pairs, cycles):
#     number_sock = pairs  * 2
#     lost_sock = cycles // 2
#     found_sock = cycles // 3
#     descarde_sock = cycles // 5
#     purchased_sock = 2  * (cycles // 10)
    
#     extra_sock = found_sock + purchased_sock
#     missing_sock = lost_sock + descarde_sock
    
#     current_sock = number_sock + extra_sock
    
#     if missing_sock <= current_sock:
#         current_sock -= missing_sock
#     else:
#         current_sock = 0

#     return current_sock // 2

# print(sock_pairs(1, 8))


# # ----------------- 18 Octobre 25 -----------------------
# def caesar(text, shift, encrypt=True):

#     if not isinstance(shift, int):
#         return 'Shift must be an integer value.'

#     if shift < 1 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     if not encrypt:
#         shift = - shift
    
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     encrypted_text = text.translate(translation_table)
#     return encrypted_text

# def encrypt(text, shift):
#     return caesar(text, shift)
    
# def decrypt(text, shift):
#     return caesar(text, shift, encrypt=False)


# encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
# decrypted_text = decrypt(encrypted_text, 13)
# print(decrypted_text)



# def is_fizz_buzz(sequence):
    
#     nb_conditions_required = 2   
#     nb_conditions_verified = 1
    
#     integer_ascending = []
    
#     for i, item in enumerate(sequence, 1):
        
#         # The array must start at 1 and have no missing or extra elements
#         if i % 3 != 0  and i % 5 != 0 and  item != i:
#             return False
            
#         # Numbers that are multiples of 3 are replaced with "Fizz"
#         if i % 3 == 0:
#             nb_conditions_required += 1
#             if item == "Fizz":
#                 nb_conditions_verified += 1
                
#         # Numbers that are multiples of 5 are replaced with "Buzz"
#         if i % 5 == 0:
#             nb_conditions_required += 1
#             if item == "Buzz":
#                 nb_conditions_verified += 1 
        
#         # Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
#         if i % 3 == 0 and i % 5 == 0:
#             nb_conditions_required -= 1
#             if item == "FizzBuzz":
#                 nb_conditions_verified += 1
                    
#         # All other numbers remain as integers in ascending order, starting from 1.
#         if isinstance(item, int):
#             integer_ascending.append(item)
        
#     ascending_order = sorted(integer_ascending)
#     if integer_ascending == ascending_order:
#         nb_conditions_verified += 1
    
#     return nb_conditions_verified == nb_conditions_required

# # is_fizz_buzz([1, 2, "Fizz", 4])

"""
# 🔍 Déboguer un validateur d’ISBN

# 📘 Debug an ISBN Validator — Déboguer un validateur d’ISBN

L’ISBN (International Standard Book Number, numéro international normalisé du livre) est un identifiant unique assigné aux livres commerciaux.
Il peut comporter 10 chiffres ou 13 chiffres, et le dernier chiffre est un check digit (chiffre de contrôle) calculé à partir des autres chiffres.

Camperbot a essayé de construire son propre validateur d’ISBN, mais a commis plusieurs erreurs.

Dans ce lab, vous allez corriger le code existant pour qu’il fonctionne correctement.

---

# 🎯 Comportement attendu

Lorsque l’utilisateur lance le programme, il doit voir :

```
Enter ISBN and length:
```

Il doit entrer un ISBN sans tirets, suivi de sa longueur (10 ou 13), au format :

```
ISBN,length
```

### Exemples :

 `1530051126,10` → ISBN-10
 `9781530051120,13` → ISBN-13

---

# 🔢 Comment obtenir le check digit

Vous n'avez pas besoin de connaître la logique détaillée du calcul.

Les fonctions :

 calculate_check_digit_10
 calculate_check_digit_13

…se chargent de retourner le check digit attendu (en string / chaîne).

✔ Le check digit ISBN-10 peut être : 0–9 ou X
✔ Le check digit ISBN-13 peut être : 0–9

---

# 📝 Objectif : remplir les User Stories suivantes

### ✅ 1. Corriger l’IndentationError (erreur d’indentation) dans le code actuel.

### ✅ 2. Gérer les entrées sans virgule pour éviter un IndexError.

Si l’utilisateur n’entre pas deux valeurs séparées par une virgule :

➡️ Afficher : Enter comma-separated values.
➡️ Puis arrêter le programme.

### ✅ 3. Gérer les entrées où la longueur n’est pas un nombre (éviter le ValueError).

Si l’utilisateur entre une longueur invalide :

➡️ Afficher : Length must be a number.
➡️ Puis arrêter.

### ✅ 4. Corriger l’erreur off-by-one dans la fonction validate_isbn.

### ✅ 5. Corriger le TypeError lorsque l’utilisateur entre un ISBN valide.

### ✅ 6. Corriger l’IndexError présent dans le code lors d’un ISBN valide.

### ✅ 7. Gérer les ISBN contenant des caractères non numériques (sauf le check digit pour ISBN-10).

S’il y a des caractères invalides :

➡️ Afficher : Invalid character was found.

### ✅ 8. Pour l’entrée 1530051126,10, afficher : Valid ISBN Code.

### ✅ 9. Pour l’entrée 9781530051120,13, afficher : Valid ISBN Code.

---

# ⚠️ Important pour les tests

Vous devrez commenter l’appel à `main()` dans l’espace global, sinon les tests ne fonctionneront pas.

---

# 🧾 Résumé des messages attendus

| Code ISBN                       | Longueur               | Message attendu                                                                          | Exemple            |
| ------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------- | ------------------ |
| Valide                          | Valide                 | Valid ISBN Code.                                                                         | `1530051126,10`    |
| Invalid Number                  | Valide                 | Invalid ISBN Code.                                                                       | `1530051125,10`    |
| Ne correspond pas à la longueur | Valide                 | ISBN-10 code should be 10 digits long. ou ISBN-13 code should be 13 digits long.         | `9781530051120,10` |
| Caractères invalides            | Valide                 | Invalid character was found.                                                             | `15-0051126,10`    |
| N’importe quoi                  | Longueur invalide      | Length should be 10 or 13.                                                               | `1530051126,9`     |
| N’importe quoi                  | Longueur non numérique | Length must be a number.                                                                 | `1530051125,A`     |
| Pas séparé par une virgule      | —                      | Enter comma-separated values.                                                            | `1530051125`       |

---

# 🧪 Exemples à tester

### ✔ ISBN-10 valides

 `1530051126,10`
 `9971502100,10`
 `080442957X,10`

### ✔ ISBN-13 valides

 `9781530051120,13`
 `9781947172104,13`

"""


import pdb


def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    main_digits = isbn[0:length]
    given_check_digit = isbn[length-1]
    main_digits_list = []
    for digit in main_digits:
        if digit.isdigit():
            main_digits_list.append(int(digit))
        else:
            print(" Invalid character was found.")
            return
        
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')
        
        
def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit  * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit  * 1
        else:
            digits_sum += digit  * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')
    if "," not in user_input:
        print("Enter comma-separated values.")
        return
    values = user_input.split(',')
    isbn = values[0]
    length = values[1]
    if not length.isdigit():
        print("Length must be a number.")
        return
    length = int(length)
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

main()

# print(calculate_check_digit_10([1, 2, 3, 4, 5, 6, 7, 8]))