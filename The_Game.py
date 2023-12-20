import tkinter as tk

class MainGame:
    def __init__(self, ai_level):
        self.root = tk.Tk()
        self.root.title("Connect 4 - Main Game")

        # Set AI level based on user choice
        if ai_level == "Beginner":
            from Heuristic_F1 import custom_heuristic_move, custom_heuristic_score
            self.ai_algorithm = custom_heuristic_move(), custom_heuristic_score()
        elif ai_level == "Intermediate":
            from Heuristic_F2 import heuristic_move
            self.ai_algorithm = heuristic_move()
        elif ai_level == "Expert":
            from MiniMax import minimax
            self.ai_algorithm = minimax()
        elif ai_level == "Master":
            from MM_AlphaBeta import minimax_ab
            self.ai_algorithm = minimax_ab()
        else:
            raise ValueError("Invalid Difficulty level")

    def play(self):
        pass

if __name__ == "__main__":
    main_game = MainGame("Beginner")
    main_game.play()