import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.config(bg="#282c34")

# Global variables for score tracking
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update labels
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Reset the game (play again)
def reset_game():
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    result_label.config(text="Make your move!")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), fg="white", bg="#282c34")
title_label.pack(pady=10)

# Labels for showing results
user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 14), fg="white", bg="#282c34")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 14), fg="white", bg="#282c34")
computer_choice_label.pack()

result_label = tk.Label(root, text="Make your move!", font=("Arial", 16, "bold"), fg="#ffcc00", bg="#282c34")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), fg="white", bg="#282c34")
score_label.pack()

# Buttons for user choices
button_frame = tk.Frame(root, bg="#282c34")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, bg="#4CAF50", fg="white",
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, bg="#2196F3", fg="white",
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, bg="#f44336", fg="white",
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Play Again button
reset_btn = tk.Button(root, text="Play Again", font=("Arial", 12), bg="#9C27B0", fg="white", command=reset_game)
reset_btn.pack(pady=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), bg="#555", fg="white", command=root.destroy)
exit_btn.pack()

# Run the main loop
root.mainloop()
