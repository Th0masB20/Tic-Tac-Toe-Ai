from tkinter import *
import numpy as np
import random

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        game_window = Tk()
        game_window.geometry(f"{width}x{height}")
        self.game_window = game_window
        self.frame = Frame()
        self.frame.pack()
        self.createBoard();
        self.players = np.array(['X', "O"]);
        self.current_player = random.choice([0,1])

        
    def createBoard(self):
        self.board = np.array([[0,0,0],
                              [0,0,0],
                              [0,0,0]], dtype=Button)
        
        for x in range(3):
            for y in range(3):
                self.board[x][y] = Button(self.frame, text="", width=23, height=10, command=lambda row=x, col=y: self.set_play(row,col))
                self.board[x][y].grid(row=x, column=y)
    
    def set_play(self,row, col):
        if self.board[row][col]['text'] == '' and self.current_player == 0:
            self.board[row][col]['text'] = 'X'
        elif self.board[row][col]['text'] == '' and self.current_player == 1:
            self.board[row][col]['text'] = 'O'
        
        self.current_player = not self.current_player
