import tkinter as tk
import mysql.connector
from tkinter import messagebox
import re


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


conn = mysql.connector.connect(
    host="127.0.0.1",
    user="sunkar",
    password="sunkarroot",
    database="test"
)
cursor = conn.cursor(buffered=True)


cursor.execute("CREATE TABLE IF NOT EXISTS users (email VARCHAR(255) PRIMARY KEY, password VARCHAR(255))")
conn.commit()


cursor.execute("CREATE TABLE IF NOT EXISTS registered_users (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), full_name VARCHAR(255), other_info TEXT)")
conn.commit()

def validate_login(email, password):
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    
    cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()

    if row is None:
        messagebox.showerror("Invalid Email", "Email not found. Please try again.")
    elif row[0] == password:
        messagebox.showinfo("Login Successful", "You are logged in successfully.")
    else:
        messagebox.showerror("Invalid Password", "Incorrect password. Please try again.")

def validate_registration(email, password, full_name, other_info):

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    cursor.execute("SELECT email FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()

    if row:
        messagebox.showerror("Email Exists", "Email is already registered. Please log in.")
    elif not re.match(r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$", password):
        messagebox.showerror("Invalid Password", "Password does not meet the specified criteria.")
    else:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        cursor.execute("INSERT INTO registered_users (email, full_name, other_info) VALUES (%s, %s, %s)",
                       (email, full_name, other_info))
        conn.commit()
        messagebox.showinfo("Registration Successful", "Account created successfully. You can now log in.")

def login_window():
    window = tk.Tk()
    window.title("Login")

    
    bg_color = "#E6E6E6"  # Grey
    fg_color = "black"

    window.configure(bg=bg_color)

    email_label = tk.Label(window, text="Email:", bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    email_label.pack()

    email_entry = tk.Entry(window, font=("Times New Roman", 12))
    email_entry.pack()

    password_label = tk.Label(window, text="Password:", bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    password_label.pack()

    password_entry = tk.Entry(window, show="*", font=("Times New Roman", 12))
    password_entry.pack()

    login_button = tk.Button(window, text="Login", command=lambda: validate_login(email_entry.get(), password_entry.get()), bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    login_button.pack()

    register_button = tk.Button(window, text="Create New Account", command=registration_window, bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    register_button.pack()

    center_window(window, 400, 200) 

    window.mainloop()

def registration_window():
    registration_window = tk.Tk()
    registration_window.title("Registration")


    bg_color = "#E6E6E6"  # Grey
    fg_color = "black"

    registration_window.configure(bg=bg_color)

    email_label = tk.Label(registration_window, text="Email:", bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    email_label.pack()

    email_entry = tk.Entry(registration_window, font=("Times New Roman", 12))
    email_entry.pack()

    password_label = tk.Label(registration_window, text="Password:", bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    password_label.pack()

    password_entry = tk.Entry(registration_window, show="*", font=("Times New Roman", 12))
    password_entry.pack()

    full_name_label = tk.Label(registration_window, text="Full Name:", bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    full_name_label.pack()

    full_name_entry = tk.Entry(registration_window, font=("Times New Roman", 12))
    full_name_entry.pack()

    other_info_label = tk.Label(registration_window, text="Other Information:", bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    other_info_label.pack()

    other_info_entry = tk.Entry(registration_window, font=("Times New Roman", 12))
    other_info_entry.pack()

    register_button = tk.Button(registration_window, text="Register", command=lambda: validate_registration(email_entry.get(), password_entry.get(), full_name_entry.get(), other_info_entry.get()), bg=bg_color, fg=fg_color, font=("Times New Roman", 12))
    register_button.pack()

    center_window(registration_window, 400, 250)

    registration_window.mainloop()

login_window()