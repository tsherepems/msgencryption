
text = input ("enter your message to be encrypted=")
key1 =int(input("enter a number less than 26 you want to encrypt with:"))
alphabets="abcdefghijklmnopqrstuvwxyz"
alphabets2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypt,decrypt= "", ""
if text.isupper():
    for letter in text:
        nposition=(alphabets2.find(letter)+key1)%26
        encrypt+=alphabets2[nposition]

    print("encrypted message is",encrypt)
    
    for letter in encrypt:
        nposition=(alphabets2.find(letter)-key1)%26
        decrypt = decrypt + alphabets2[nposition]
       
    key2=int(input("Enter the secret shift key password to decrypt:"))
    if(key2==key1):

        print("Decrypted message is:",decrypt)
    else:
        print("The secret password you entered is incorrect! PLEASE TRY AGAIN")    
else:    

    for letter in text:
 
        new_position=(alphabets.find(letter)+key1)%26
        encrypt+=alphabets[new_position]

    print("the encrypted message is :",encrypt)

    for letter in encrypt:
        new_position=(alphabets.find(letter)-key1)%26
        decrypt = decrypt + alphabets[new_position]

    key2=int(input("Enter the secret password to decrypt:"))
    if(key2==key1):
        print("Decrypted message is:",decrypt)
    else:
        print("The secret password you entered is incorrect! PLEASE TRY AGAIN")
exit
