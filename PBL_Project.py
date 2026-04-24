# WORKING :-
# Added count login attempt in this 
# Only thing left is adding salt to password 
# Encryption (from python libraries)
# Secret key
from cryptography.fernet import Fernet

def load_key():
    with open("secret.key", "rb") as f:
        return f.read()
#Encrypt
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    return encrypted.decode()
#Decrypt
def decrypt_data(encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data.encode())
    return decrypted.decode()

#  HASHING USING SHA256 ( but salt not added ) (from python libraries)
def hash_password(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
import json
# Load existing users
# yahan per ek user jason ki file banayi hai jahan username and password save hain
try:
    with open("users.json", "r") as file:
        user = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    user = {}
# Humne vault menu ke code ko uppar rakha hai because hume main menu ko vault menu ko main menu sai connect karna tha jiske liye hum "vault_menu(username)" kiya and vault menu ke code ko function ke under likha  
# vault menu 
vault_data = {}
def vault_menu(username):
    while True:
        choice = input("Add Credentials (add) , View Credentials (view) , Logout (l): ")

        if choice == "add":
            App = input("Enter Application Name: ")
            Uname = input("Enter Username: ")
            Pwd = input("Enter Password: ")
            encrypted_Uname = encrypt_data(Uname)
            encrypted_Pwd = encrypt_data(Pwd)

            vault_data[App] = {
                "username": encrypted_Uname,
                "password": encrypted_Pwd }
# file handeling (AI sai kawai hai)
            with open(username + "_vault.txt", "a") as f:        # <---- isse jab bhi ek user vault main main menu main login karega tab uska personal space create ho jayega and vahan voh apne credentials save kar sakta hai 
                f.write(App + "," + encrypted_Uname + "," + encrypted_Pwd + "\n")

            print("Credential saved!")

        elif choice == "view":
            try:
                with open(username + "_vault.txt", "r") as f:
                    data = f.readlines()

                    if not data:
                        print("No credentials found.")
                    else:
                        print("\nSaved Credentials:")
                        for line in data:
                            App, enc_user, enc_pwd = line.strip().split(",")
                            Uname = decrypt_data(enc_user)
                            Pwd = decrypt_data(enc_pwd)
                            print(f"App: {App}, Username: {Uname}, Password: {Pwd}")

            except FileNotFoundError:
                print("No vault found yet.")

        elif choice == "l":
            print("Logging out...")
            break

        

# Main menu 
while True :
    choice = input("Do you want to register or login (r/l) or exist(e): ")

    if choice == "r":
# username ke main 6 sai zayada character hone chaiye , lowercase , uppercase , digit hone chaiye and special character nhi hone chaiye 
        username = input("Enter username: ")

        has_digit = False
        has_lowercase = False
        has_uppercase = False
        has_specialchar = False

        special_chars = "@!#$%^&*()+={}[]:;<>?-~"

        for i in username:
            if i.isdigit():
                has_digit = True
            elif i.isupper():
                has_uppercase = True
            elif i.islower():
                has_lowercase = True
            elif i in special_chars:
                has_specialchar = True

        if len(username) < 6 or not has_digit or not has_lowercase or not has_uppercase or has_specialchar:
            print("Invalid username")
        elif username in user:
            print("Username already exists")
        else:
#password main 8 sai zayada character hone chaiye , lowercase , uppercase , digit and special character  hone chaiye 
            password = input("Enter password: ")

            has_digit = False
            has_lowercase = False
            has_uppercase = False
            has_specialchar = False

            for i in password:
                if i.isdigit():
                    has_digit = True
                elif i.islower():
                    has_lowercase = True
                elif i.isupper():
                    has_uppercase = True
                else:
                    has_specialchar = True

            if len(password) >= 12 and has_digit and has_lowercase and has_uppercase and has_specialchar:
                print("Strong Password")
                hashed = hash_password(password)
                user[username] = hashed
                
            elif len(password) >= 8:
                print("Medium password - try stronger one")
                hashed = hash_password(password)
                user[username] = hashed  
            else:
                print("Weak password")
                exit()

            with open("users.json", "w") as file:
                json.dump(user, file)

            print("Successfully registered")
            

    elif choice == "l":
        username = input("Enter username: ")

        if username not in user:
            print("Username not found")
        else:
            attempts = 0
            while attempts < 3:
                password = input("Enter password: ")

                if user[username] == hash_password(password):
                    print("Successful login")
                    vault_menu(username)
                    break
                else:
                    attempts += 1
                    print(f"Wrong password. Attempts left: {3 - attempts}")

            if attempts == 3:
                print("Account LOCKED")

    