alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l',
             'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text , shift_key):
    cipher_text = " "
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key)%26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
        
    print(f"Here is the text after encryption :{cipher_text} \n")    

def decryption(cipher_text , shift_key):
    plain_text = " "
    for char in cipher_text:
        if char in alphabets:

            position = alphabets.index(char)
            new_position = (position - shift_key)%26
            plain_text += alphabets[new_position]
        else:
            plain_text += char    
    print(f"Here is the text after dencryption :{plain_text} \n")    


end = False

while not end :

    choice = input("Type 'encrypt' for encryption ,type 'decrypt' for decryption:\n")
    text = input("Type your message:\n")
    shift = int(input("Enter shift key:\n"))

    if (choice == "encrypt"):
        encryption(plain_text=text,shift_key=shift)

    elif (choice == "decrypt"):
        decryption(text,shift)  

    play_again = input ("Type 'YES' to plain again , type 'no' not to play : \n") 
    if play_again == "no":
        end = True
        print("Have a nice day!!")         