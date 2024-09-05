import tkinter as tk
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def on_button_click(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("rock"), width=20)
rock_button.pack(padx=20,pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("paper"), width=20)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("scissors"), width=20)
scissors_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Verdana', 14))
result_label.pack(pady=20)

root.mainloop()
