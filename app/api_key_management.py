import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('data/secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    return open('data/secret.key', 'rb').read()

def encrypt_api_key(api_key):
    key = load_key()
    fernet = Fernet(key)
    encrypted_api_key = fernet.encrypt(api_key.encode())
    with open('data/encrypted_api_key.enc', 'wb') as enc_file:
        enc_file.write(encrypted_api_key)
    return encrypted_api_key

def decrypt_api_key():
    key = load_key()
    fernet = Fernet(key)
    with open('data/encrypted_api_key.enc', 'rb') as enc_file:
        encrypted_api_key = enc_file.read()
    decrypted_api_key = fernet.decrypt(encrypted_api_key).decode()
    return decrypted_api_key
