
import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.pack(padx=10,pady=5)

        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.pack(padx=10,pady=5) 

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(padx=10,pady=10)

        self.password_entry = tk.Entry(self.root, width=50)
        self.password_entry.pack(padx=5,pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
        except ValueError:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Invalid length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
