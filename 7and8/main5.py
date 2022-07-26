def encrypt(word, shift):
    new_word = ""
    for i in word:
        if alphabet.index(i)+shift > 25:
            new_shift = (alphabet.index(i)+shift)-25
            new_word += alphabet[new_shift]
        else:
            new_word += alphabet[alphabet.index(i)+shift]
    print(new_word)

def decrypt(word, shift):
    new_word = ""
    for i in word:
        if alphabet.index(i) + shift < 0:
            new_shift = (alphabet.index(i) - shift) + 25
            new_word += alphabet[new_shift]
        else:
            new_word += alphabet[alphabet.index(i) - shift]
    print(new_word)

def ceaser(word, shift, type):
    if type == "decode":
        decrypt(word, shift)
    elif type == "encode":
        encrypt(word, shift)
    else:
        print("Wrong input")

if __name__ == "__main__":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print("""           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """)
    should_continue = True
    while should_continue:
        continue_inp = input("Do you want to use the caesar cipher? [Yes/No]: ")
        if continue_inp == "Yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            ceaser(text, shift, direction)
        else:
            print("Goodbye! ")
            should_continue = False
