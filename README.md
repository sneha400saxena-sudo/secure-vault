# 🔐 Secure Vault

A web-based Secure Vault application built using Python and Streamlit that allows users to store and manage credentials with encryption.

---

## 🚀 Features

- User Registration & Login system  
- Password hashing using SHA-256  
- Encrypted storage using Fernet (symmetric encryption)  
- Add and view credentials securely  
- Login attempt limit with temporary lock system  
- Interactive web interface using Streamlit  

---

## 🧪 Project Evolution

- `pbl_project.py` → Initial CLI-based version  
- `full_project.py` → Web-based version using Streamlit  

This demonstrates the transition from a command-line application to a user-friendly web interface.

---

## ⚠️ Disclaimer

This is a **demo project** and not intended for real-world password storage.

- Uses local JSON file storage  
- Encryption key is stored locally  
- Not production secure  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Cryptography (Fernet)  
- JSON  

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run full_project.py
