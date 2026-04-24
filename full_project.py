import streamlit as st
import json
import os
import hashlib
import time
from cryptography.fernet import Fernet

# ------------------ SECURITY ------------------

def load_key():
    return open("secret.key", "rb").read()

def encrypt_data(data):
    f = Fernet(load_key())
    return f.encrypt(data.encode()).decode()

def decrypt_data(data):
    f = Fernet(load_key())
    return f.decrypt(data.encode()).decode()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------ LOAD USERS ------------------

if os.path.exists("users.json"):
    with open("users.json", "r") as f:
        users = json.load(f)
else:
    users = {}

# ------------------ SESSION INIT ------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "lock_time" not in st.session_state:
    st.session_state.lock_time = None

# ------------------ UI ------------------

st.title("🔐 Secure Vault")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

# ------------------ REGISTER ------------------

if menu == "Register":
    st.subheader("Create Account")

    reg_user = st.text_input("Username", key="reg_user")
    reg_pass = st.text_input("Password", type="password", key="reg_pass")

    if st.button("Register"):
        if reg_user in users:
            st.error("User already exists")
        else:
            users[reg_user] = hash_password(reg_pass)
            with open("users.json", "w") as f:
                json.dump(users, f)
            st.success("Registered successfully!")

# ------------------ LOGIN ------------------

elif menu == "Login":
    st.subheader("Login")

    login_user = st.text_input("Username", key="login_user")
    login_pass = st.text_input("Password", type="password", key="login_pass")

    LOCK_DURATION = 30

    # 🔒 Check lock
    if st.session_state.lock_time:
        elapsed = time.time() - st.session_state.lock_time

        if elapsed < LOCK_DURATION:
            remaining = int(LOCK_DURATION - elapsed)
            st.error(f"Locked. Try again in {remaining}s")
            st.stop()
        else:
            st.session_state.lock_time = None
            st.session_state.attempts = 0

    # 🔑 Login button
    if st.button("Login"):

        if login_user in users and users[login_user] == hash_password(login_pass):
            st.session_state.logged_in = True
            st.session_state.username = login_user
            st.session_state.attempts = 0
            st.success("Logged in!")

        else:
            st.session_state.attempts += 1
            remaining = 3 - st.session_state.attempts

            if remaining > 0:
                st.error(f"Wrong password. Attempts left: {remaining}")
            else:
                st.session_state.lock_time = time.time()
                st.error("Too many attempts! Locked for 30s 🔒")

# ------------------ VAULT ------------------

if st.session_state.logged_in:

    st.subheader(f"Welcome {st.session_state.username}")

    action = st.selectbox("Choose Action", ["Add", "View", "Logout"])

    filename = st.session_state.username + "_vault.json"

    # ---------- ADD ----------
    if action == "Add":

        app = st.text_input("App Name", key="app_name")
        uname = st.text_input("Username", key="vault_user")
        pwd = st.text_input("Password", type="password", key="vault_pass")

        if st.button("Save"):

            if not app or not uname or not pwd:
                st.warning("Fill all fields")
            else:
                data = []

                if os.path.exists(filename):
                    with open(filename, "r") as f:
                        data = json.load(f)

                data.append({
                    "app": app,
                    "username": encrypt_data(uname),
                    "password": encrypt_data(pwd)
                })

                with open(filename, "w") as f:
                    json.dump(data, f)

                st.success("Saved!")

    # ---------- VIEW ----------
    elif action == "View":

        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)

            for i, item in enumerate(data):
                st.write(f"### {item['app']}")

                if st.checkbox("Show", key=f"show_{i}"):
                    st.write("Username:", decrypt_data(item["username"]))
                    st.write("Password:", decrypt_data(item["password"]))

                st.write("---")
        else:
            st.info("No data found")

    # ---------- LOGOUT ----------
    elif action == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = None
        st.success("Logged out")