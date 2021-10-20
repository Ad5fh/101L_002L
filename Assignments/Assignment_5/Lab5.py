## Aissatou Diallo
## ad5fh@umsystem.edu 
## CS 101 Lab
##PROBLEM: Caesar Encryption/Decryption, including cracking a string
##Algorithm: The program below is a Caesar Cipher Encryption/Decryption. It has two main functions, the first one is the encryption one which is used to encrypt a string. And the second one is used to decrypt a string.
#################################################################################################################################

def encrypt(text,shift):
      encode =""
 
    # traverse the string
      for i in range(len(text)):
         character = text[i]
 
        # Encrypt uppercase characters
         if character==' ':
           encode +=" "
           continue
         if (character.isupper()):
           encode += chr((ord(character) + shift-65) % 26 + 65)
 
        # Encrypt lowercase characters
         else:
          encode += chr((ord(character) + shift - 97) % 26 + 97)
      return encode.upper()
def decrypt(text,shift):
      decode = ""
 
    # traverse the string 
      for i in range(len(text)):
        character = text[i]
 
        # Encrypt uppercase characters
        if character==' ':
           decode +=" "
           continue
        if (character.isupper()):
          decode += chr((ord(character) - shift-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
          decode += chr((ord(character) - shift - 97) % 26 + 97)
 
      return decode.upper()
while(1):
 print()
 print('MAIN MENU')
 print("1) Encode a string")
 print("2) Decode a string")
 print("Q) Quit")
 selection=input("Enter your selection ==> ")
 if selection=='1':
#check the encryption function
    print()
    text = input("Enter (brief) text to encrypt: ")
    shift = int(input("Enter the number to shift letters by: "))
    print ("Encrypted: ",encrypt(text,shift))

 elif selection=='2':
     #check the decryption function
    text = input("Enter (brief) text to decrypt: ")
    shift = int(input("Enter the number to shift letters by: "))
    print ("Decrypted: " + decrypt(text,shift))
 elif selection== "Q" or selection== "q" :
      break
 continue
