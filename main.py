from tkinter import *
from game.board import Game

def run_game():
    game = Game(500,500);
    print(game.board)
    game.game_window.mainloop()
    
if __name__ == "__main__":
    run_game();