import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice_handler(choice):
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)

    user_choice_label.config(text=f'You chose: {choice}')
    computer_choice_label.config(text=f'Computer chose: {computer_choice}')
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

user_choice_label = tk.Label(root, text="")
user_choice_label.pack()
computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: user_choice_handler('rock'))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice_handler('paper'))
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice_handler('scissors'))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

root.mainloop()
