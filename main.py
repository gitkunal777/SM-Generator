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

# Program
usr_inp = input('Enter the secrate message: ')
encrypt(usr_inp)