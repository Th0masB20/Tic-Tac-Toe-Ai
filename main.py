from tkinter import *
from game.board import Game
from game.player_ai import Player_AI

def run_game():
    game = Game(600,600);
    game.game_window.mainloop()
    
if __name__ == "__main__":
    run_game();