# password_strength_meter.py

import streamlit as st
import re

# Basic list of common weak passwords (you can expand this)
common_passwords = {"123456", "password", "123456789", "qwerty", "12345678", "111111", "123123"}

def evaluate_password(password):
    score = 0
    feedback = []

    if password in common_passwords:
        feedback.append("This is a very common password.")
        return "Very Weak", feedback

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters.")
    
    # Character types
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
        
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Final judgment
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

# Streamlit UI
st.title("Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength, tips = evaluate_password(password)
    st.markdown(f"### Strength: {strength}")
    if tips:
        st.markdown("#### Suggestions:")
        for tip in tips:
            st.write(tip)