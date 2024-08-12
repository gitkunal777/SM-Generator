# Importing modules
from cryptography.fernet import Fernet as fnt

# Function(s)
def encrypt(text):
 print("")
 key = fnt.generate_key()
 encrypted_msg = fnt(key).encrypt(text.encode())
 print("Key: ",key.decode())
 print("")
 print("Encrypted Message: ",encrypted_msg.decode())

def decrypt(text, key):
 print("")
 key = key
 decrypted_msg = fnt(key).decrypt(text.encode())
 print("")
 print("Your Message: ",decrypted_msg.decode())

# Program
usr_inp = input('Enter [1] for reciver, [2] for sender: ')
if usr_inp == '1':
 print("")
 key = input("Enter the Key: ")
 print("")
 msg = input("Enter the Secrate Message: ")
 decrypt(msg, key)

else:
 print("")
 msg = input("Enter the Message: ")
 encrypt(msg)