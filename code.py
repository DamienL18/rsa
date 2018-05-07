#n = 18923
#e = 443
#d = 4883
def run():
    numbers = 0
    print ("Hello would you like to encrypt or decrypt?")
    answer = input()
    while (numbers !=1):
      if  answer == 'encrypt':
       print ("Please enter the other users E and N:")
       e = int(input("E:" ))
       n = int(input("N:" ))
       encrypt(e, n)
       print ("Hello would you like to encrypt, decrypt or exit?")
       answer = input()
      elif answer == 'decrypt':
       print ("Please enter D and N:")
       d = int(input("D:" ))
       n = int(input("N:" ))
       decrypt(d, n)
       print ("Hello would you like to encrypt, decrypt or exit?")
       answer = input()
      elif answer == "exit":
       numbers = 1
      else: 
        print("PLease stay within the program bub!")
        print ("Hello would you like to encrypt, decrypt or exit?")
        answer = input()

def encrypt(e, n):
  encrypted_message = ""
  print ("Please type the message you would like to encrypt!")
  message = input()
  for x in message:
    numerize = ord(x)
    encryption = pow(numerize, e, n)
    denumerize = chr(encryption)
    encrypted_message += denumerize
  print (encrypted_message)
  
  
def decrypt(d, n):
  decrypted_message = ""
  print ("Please type the message you would like to decrypt!")
  encrypted_message = input()
  for t in encrypted_message:
    numerize = ord(t)
    decryption = pow(numerize, d, n)
    denumerize = chr(decryption)
    decrypted_message += denumerize
  print (decrypted_message)

  
