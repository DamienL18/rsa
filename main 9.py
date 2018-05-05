#n = 18923
#e = 443
#d = 4883

def run():
  print ("Hello would you like to encrypt or decrypt?")
  answer = input()
  if answer == 'encrypt':
    print ("Please enter the other users E and N:")
    e = int(input("E:" ))
    n = int(input("N:" ))
    encrypt(e, n)
  elif answer == 'decrypt':
    print ("Please enter D and N:")
    d = int(input("D:" ))
    n = int(input("N:" ))
    decrypt(d, n)
  


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

  
