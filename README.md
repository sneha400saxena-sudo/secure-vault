# 🔐 Secure Vault

## Overview

Secure Vault is a credential management application developed using Python and Streamlit. The application allows users to securely store and manage account credentials through user authentication, password hashing, and encrypted storage mechanisms.

The project was initially developed as a command-line application and later upgraded into a web-based application using Streamlit, demonstrating the transition from a console-based system to a user-friendly graphical interface.

---
## 🌐 Live Demo

🔗 Streamlit Deployment:

https://secure-vault-rngmjgmm6vmw3v543dewzg.streamlit.app/

The application can be accessed directly through the deployed Streamlit web interface.
---

## 🚀 Features

* User Registration and Login System
* Password Hashing using SHA-256
* Credential Encryption using Fernet Cryptography
* Secure Storage of User Credentials
* User-Specific Vault Management
* Login Attempt Limiting and Temporary Lockout
* Interactive Web Interface using Streamlit
* Credential Viewing with Controlled Decryption

---

## 🔒 Security Features

* Passwords are stored as SHA-256 hashes rather than plain text.
* User credentials are encrypted before being stored.
* Multiple failed login attempts trigger a temporary account lockout mechanism.
* Separate vault files are maintained for different users.
* Encryption and decryption operations are handled using the Cryptography library's Fernet implementation.

---

## 🧪 Project Evolution

### Version 1 – Command Line Application

**PBL_Project.py**

Features:

* User Registration
* User Login
* Password Hashing
* Credential Encryption
* Credential Storage
* Vault Access through CLI

### Version 2 – Web Application

**full_project.py**

Enhancements:

* Streamlit-based User Interface
* Improved User Experience
* Login Attempt Tracking
* Temporary Account Locking
* Interactive Credential Management

This progression demonstrates the evolution of the project from a command-line application into a web-based credential management system.

---

## 📂 Project Structure

```text
secure-vault/
│
├── PBL_Project.py
├── full_project.py
├── requirements.txt
├── users.json
├── secret.key
└── README.md
```

---

## 📋 Demo Files

This repository contains sample data files for demonstration purposes only.

No real credentials, passwords, or encryption keys are stored in the repository.

Files such as:

* users.json
* secret.key

are included solely to demonstrate the application's functionality and data structure.

---

## ⚠️ Disclaimer

This project was developed for educational and learning purposes.

Current limitations include:

* Password hashing uses SHA-256 without salting.
* Encryption keys are stored locally.
* Data is stored using local JSON files.
* The application is not intended for production use.

---

## 🔮 Future Improvements

* Replace SHA-256 password storage with bcrypt or Argon2.
* Implement password salting.
* Improve encryption key management.
* Add audit logging functionality.
* Add password strength analysis.
* Implement encrypted backup and recovery mechanisms.
* Migrate from JSON storage to a secure database solution.

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Cryptography (Fernet)
* JSON
* Hashlib

---

## ▶️ Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/sneha400saxena-sudo/secure-vault.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run full_project.py
```

---

## 🎯 Learning Outcomes

Through this project, the following concepts were explored:

* User Authentication
* Password Hashing
* Encryption and Decryption
* Secure Credential Storage
* Python Application Development
* Streamlit Web Development
* Basic Security Controls
* Project Migration from CLI to GUI

---

## 👩‍💻 Author

Sneha sneha

B.Tech CSIT (Cybersecurity)

Developed as a cybersecurity-focused learning project to explore secure credential management and cryptographic concepts.



