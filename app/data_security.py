from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('data/secret.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('data/secret.key', 'rb').read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    return encrypted_file_path

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    decrypted_file_path = file_path.replace('.enc', '')
    with open(decrypted_file_path, 'wb') as dec_file:
        dec_file.write(decrypted)
    return decrypted_file_path
