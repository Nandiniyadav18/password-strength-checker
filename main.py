import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry.get()
    
    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase
    if re.search("[A-Z]", password):
        score += 2
    else:
        suggestions.append("Add uppercase letter")

    # Lowercase
    if re.search("[a-z]", password):
        score += 2
    else:
        suggestions.append("Add lowercase letter")

    # Numbers
    if re.search("[0-9]", password):
        score += 2
    else:
        suggestions.append("Add numbers")

    # Special characters
    if re.search("[@#$%^&*]", password):
        score += 2
    else:
        suggestions.append("Add special character (@#$%^&*)")

    # Strength
    if score <= 4:
        strength = "Weak"
        color = "red"
    elif score <= 7:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    # Display result
    result_label.config(text=f"Strength: {strength} ({score}/10)", fg=color)

    if suggestions:
        suggestion_text.set("\n".join(suggestions))
    else:
        suggestion_text.set("Great! Strong password 💪")


# GUI Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Password Checker", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Input field
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

# Button
check_btn = tk.Button(root, text="Check Strength", command=check_password, bg="#4CAF50", fg="white")
check_btn.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# Suggestions
suggestion_text = tk.StringVar()
suggestion_label = tk.Label(root, textvariable=suggestion_text, bg="#f0f0f0", fg="black")
suggestion_label.pack(pady=10)

# Run app
root.mainloop()