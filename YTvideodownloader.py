import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube

# User database (for demonstration purposes)
user_database = {
    "admin": "password"
}

# Function to check login credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_database and user_database[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        enable_video_downloader()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to enable the video downloader and hide the register button
def enable_video_downloader():
    username_label.pack_forget()
    username_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()
    register_button.pack_forget()  # Hide the register button
    status_label.config(text="")
    url_label.pack()
    url_entry.pack()
    download_button.pack()

# Function to open the registration window
def open_registration_window():
    registration_window = tk.Toplevel(root)
    registration_window.title("Register New User")

    # Create and place widgets for registration
    reg_username_label = tk.Label(registration_window, text="New Username:")
    reg_username_label.pack()
    reg_username_entry = tk.Entry(registration_window)
    reg_username_entry.pack()

    reg_password_label = tk.Label(registration_window, text="New Password:")
    reg_password_label.pack()
    reg_password_entry = tk.Entry(registration_window, show="*")
    reg_password_entry.pack()

    reg_register_button = ttk.Button(
        registration_window, text="Register", command=lambda: register_user(reg_username_entry.get(), reg_password_entry.get(), registration_window)
    )
    reg_register_button.pack()

# Function to register a new user
def register_user(new_username, new_password, registration_window):
    if not new_username or not new_password:
        messagebox.showerror("Registration Failed", "Username and password cannot be empty.")
        return

    if new_username in user_database:
        messagebox.showerror("Registration Failed", "Username already exists.")
        return

    user_database[new_username] = new_password
    messagebox.showinfo("Registration Successful", "User registered successfully.")
    registration_window.destroy()

# Function to download the video
def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        status_label.config(text="Download completed!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place the login widgets
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = ttk.Button(root, text="Login", command=check_login)
login_button.pack()

# Create and place the registration button
register_button = ttk.Button(root, text="Register", command=open_registration_window)
register_button.pack()

# Create and place the video downloader widgets (these are initially hidden)
url_label = tk.Label(root, text="Enter YouTube URL:")
url_entry = tk.Entry(root)
download_button = ttk.Button(root, text="Download", command=download_video)

# Create and place the status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
