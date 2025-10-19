# ----------------- 17 Octobre 25 -----------------------
def mask(card):
    operator = "-"
    if "-" not in card:
        operator = " "
    card = card.split(operator)
    for index in range(3):
        card[index] = "*" * 4
    card = operator.join(card)
    return card

# print(mask("6011 1111 1111 1117"))


# ----------------- 19 Octobre 25 -----------------------
def extract_attributes(element):
    if not "=" in element:
        return []
    
    attributs = []
    opeartor = ">"
    if "/>" in element:
        opeartor = "/>"
    element = element.replace('"', '')
    element_clean = element.split(opeartor)[0]
    attribut_clean = element_clean.split(" ")[1:]
    
    for attribut in attribut_clean:
        if attribut:
            if "=" in attribut:
                attributs.append(f'{attribut}')
            else:
                attributs[-1] = attributs[-1].rstrip('"') + f' {attribut}'
    
    attributs_final = []
    for attribut in attributs:
        attributs_final.append(attribut.replace("=" , ", "))

    return attributs_final


# print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))

# ----------------- 18 Octobre 25 -----------------------
def sock_pairs(pairs, cycles):
    number_sock = pairs * 2
    lost_sock = cycles // 2
    found_sock = cycles // 3
    descarde_sock = cycles // 5
    purchased_sock = 2 * (cycles // 10)
    
    extra_sock = found_sock + purchased_sock
    missing_sock = lost_sock + descarde_sock
    
    current_sock = number_sock + extra_sock
    
    if missing_sock <= current_sock:
        current_sock -= missing_sock
    else:
        current_sock = 0

    return current_sock // 2

print(sock_pairs(1, 8))


# ----------------- 18 Octobre 25 -----------------------
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)