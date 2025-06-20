import tkinter as tk
from tkinter import messagebox
import random

# List of choices
choices = ["Rock", "Paper", "Scissors"]

# Logic for determining winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Draw"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Event when button is clicked
def play(choice):
    comp_choice = random.choice(choices)
    result = determine_winner(choice, comp_choice)
    result_label.config(text=f"Computer chose: {comp_choice}\n{result}")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Rock ✊ Paper ✋ Scissors ✌️", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=20)

# Exit Button
exit_btn = tk.Button(root, text="Exit Game", command=root.destroy)
exit_btn.pack(pady=10)

# Run the app
root.mainloop()
