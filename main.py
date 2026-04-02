import re
import tkinter as tk
import random
import string

# Function to check password strength
def check_password():
    password = entry.get()
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 2
    else:
        suggestions.append("Add uppercase letter")

    if re.search("[a-z]", password):
        score += 2
    else:
        suggestions.append("Add lowercase letter")

    if re.search("[0-9]", password):
        score += 2
    else:
        suggestions.append("Add numbers")

    if re.search("[@#$%^&*]", password):
        score += 2
    else:
        suggestions.append("Add special character")

    # Strength logic
    if score <= 4:
        strength = "Weak"
        color = "red"
    elif score <= 7:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    result_label.config(text=f"{strength} ({score}/10)", fg=color)

    if suggestions:
        suggestion_text.set("\n".join(suggestions))
    else:
        suggestion_text.set("Great! Strong password 💪")


# Show/Hide password
def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")


# Password generator
def generate_password():
    length = 10
    characters = string.ascii_letters + string.digits + "@#$%^&*"
    password = ''.join(random.choice(characters) for i in range(length))
    
    entry.delete(0, tk.END)
    entry.insert(0, password)


# GUI Setup
root = tk.Tk()
root.title("Cyber Password Tool")
root.geometry("420x400")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="🔐 Password Strength Checker", 
                 font=("Arial", 16, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=15)

# Entry
entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
entry.pack(pady=10)

# Show password checkbox
show_var = tk.IntVar()
show_check = tk.Checkbutton(root, text="Show Password", variable=show_var,
                            command=toggle_password, bg="#1e1e2f", fg="white")
show_check.pack()

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

check_btn = tk.Button(btn_frame, text="Check Strength", command=check_password,
                      bg="#4CAF50", fg="white", width=15)
check_btn.grid(row=0, column=0, padx=5)

gen_btn = tk.Button(btn_frame, text="Generate Password", command=generate_password,
                    bg="#2196F3", fg="white", width=15)
gen_btn.grid(row=0, column=1, padx=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#1e1e2f")
result_label.pack(pady=10)

# Suggestions
suggestion_text = tk.StringVar()
suggestion_label = tk.Label(root, textvariable=suggestion_text,
                            bg="#1e1e2f", fg="lightgray", justify="center")
suggestion_label.pack(pady=10)

# Run
root.mainloop()
