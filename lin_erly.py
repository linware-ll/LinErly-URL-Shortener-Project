import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Initialize the Shortener object (replace with your preferred service)
shortener = pyshorteners.Shortener()

def shorten_url():
    """Shortens the URL entered in the text field and displays the shortened URL.

    Raises a message box if the URL is empty or shortening fails.

    Also adds functionality to copy the shortened URL to the clipboard.
    """
    long_url = entry.get()
    if not long_url:
        messagebox.showerror("Error", "Please enter a URL to shorten.")
        return

    try:
        # Shorten the URL and display it
        short_url = shortener.tinyurl.short(long_url)
        result_label.config(text=f"Shortened URL: {short_url}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while shortening the URL: {e}")


def copy_url():
    """Copies the shortened URL from the result label to the clipboard."""
    short_url = result_label["text"].split(": ")[-1]  # Extract shortened URL from label text
    root.clipboard_append(short_url)
    messagebox.showinfo("Copied!", "Shortened URL copied to clipboard.")


def new_button():
    """Clears the entry field and result label, effectively refreshing the app."""
    entry.delete(0, tk.END)  # Delete all text from entry field
    result_label.config(text="")  # Set result label text to empty string


# Create the main window with a larger size
root = tk.Tk()
root.title("LinErly ")
root.geometry("500x250")  # Set width and height

# Style configuration (optional)
background_color = "#333"
text_color = "#000"
button_color = "#4584b6"

root.config(bg=background_color)  # Set background color

head_color = "#ffd343"

label = tk.Label(
    root, text="Enter URL:", font=("Arial", 14), fg=head_color, bg=background_color
)
label.pack(pady=20, padx=20)

# Text field for entering the URL with increased width
entry = tk.Entry(root, width=70, font=("Consolas", 14), fg=text_color, bg="#ddd")
entry.pack(pady=10, padx=20)

# Button to trigger URL shortening with styling
shorten_button = tk.Button(
    root,
    text="Shorten",
    font=("Arial", 14),
    fg=text_color,
    bg=button_color,
    command=shorten_url,
)
shorten_button.pack(pady=10, padx=20)

# Label to display the shortened URL with increased width and font size
result_label = tk.Label(
    root, font=("Arial", 16, "bold"), fg=head_color, bg=background_color
)
result_label.pack(pady=10, padx=20)

# Button to copy the shortened URL with styling
copy_button = tk.Button(
    root,
    text="Copy URL",
    font=("Arial", 14),
    fg=text_color,
    bg=button_color,
    command=copy_url,
)
copy_button.pack(pady=10, padx=20)

# Button to refresh the app with styling
new_button = tk.Button(
    root,
    text="New",
    font=("Arial", 14),
    fg=text_color,
    bg=button_color,
    command=new_button,
)
new_button.pack(pady=10, padx=20)

# Run the main event loop
root.mainloop()
