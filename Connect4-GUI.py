import tkinter as tk
from tkinter import messagebox

class Connect4GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect 4")

        self.label = tk.Label(self.root, text="Choose Difficulty Level:")
        self.label.pack()

        self.level_var = tk.StringVar()
        self.level_var.set("Beginner")  # Default level

        levels = ["Beginner", "Intermediate", "Expert", "Master"]
        for level in levels:
            tk.Radiobutton(self.root, text=level, variable=self.level_var, value=level).pack()

        self.start_button = tk.Button(self.root, text="Play", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        self.root.destroy()  # Close the Connect 4 GUI
        self.play_game()

    def play_game(self):
        from The_Game import MainGame
        main_game = MainGame(self.level_var.get())
        main_game.play()

        # Create a "Play Again" button
        play_again_button = tk.Button(self.root, text="Play Again", command=self.restart_game)
        play_again_button.pack()

        # After the game ends, ask the player if they want a rematch
        play_again = messagebox.askyesno("Play Again", "Do you want a rematch?")
        if play_again:

            self.restart_game()
        else:
            self.root.destroy()

    def restart_game(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Re-create the introduction GUI components
        self.create_intro_components()

    def restart_game(self):

        self.level_var.set("Beginner")

        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    intro_gui = Connect4GUI()
    intro_gui.root.mainloop()
