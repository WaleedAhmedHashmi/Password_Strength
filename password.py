import streamlit as st # type: ignore
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase the length to at least 8 characters.")
    
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")
    
    if any(c in '!@#$%^&*' for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    common_passwords = ["password", "123456", "password123", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        feedback.append("Avoid common passwords like 'password123'.")
        score = 1 
    
    if score == 5:
        strength = "Strong"
    elif 3 <= score <= 4:
        strength = "Moderate"
    else:   
        strength = "Weak"
    
    return strength, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(characters) for _ in range(12))

st.title("Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    st.subheader(f"Password Strength: {strength}")
    if feedback:
        st.warning("\n".join(feedback))
    else:
        st.success("Your password is strong!")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text(f"Suggested Strong Password: {strong_password}")
