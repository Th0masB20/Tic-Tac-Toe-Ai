from tkinter import *
import numpy as np
import random

from game.player_ai import Player_AI

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        game_window = Tk()
        game_window.geometry(f"{width}x{height}")
        self.game_window = game_window
        self.restart_button = Button(text='Restart', width=10, height=2, command=self.restart_game)
        self.restart_button.pack();
        self.frame = Frame()
        self.frame.pack()
        self.createBoard();
        
        self.players = np.array(["O", "X"], ndmin=1);
        self.opponent_player_value = int(0);
        self.human_player_value = int(not self.opponent_player_value)
        self.current_player = self.human_player_value
        
        self.opponent = Player_AI(self.opponent_player_value, self.human_player_value, self)
        
    def createBoard(self):
        self.board = np.array([['','',''],
                              ['','',''],
                              ['','','']])
        self.button_arr = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype=Button)
        
        for x in range(3):
            for y in range(3):
                self.button_arr[x][y] = Button(self.frame, text="", width=23, height=10, command=lambda row=x, col=y: self.set_play(row,col))
                self.button_arr[x][y].grid(row=x, column=y)
    
    def set_play(self,row, col):           
        if self.board[row][col] == '' and self.current_player == self.human_player_value and not self.check_win(self.board):
            self.board[row][col] = self.players[self.human_player_value]
            self.button_arr[row][col]['text'] = self.board[row][col]
            
            next_state = self.opponent.run_ai()
            self.board = next_state
            for x in range(3):
                for y in range(3):
                    self.button_arr[x][y]['text'] = self.board[x][y]
        
        if self.check_win(self.board) == 1:
            self.stop_game()
            print('X won')
        elif self.check_win(self.board) == -1:
            self.stop_game()
            print('O won')
        elif self.full_board(self.board):
            self.stop_game()
            print('Tied')
            
        self.current_player = not self.current_player
                
    def check_win(self, board) -> int:
        player_who_won = ''
        
        for row in range(3):
            for col in range(3):
                if board[row][0] != board[row][col]:
                    break
            else:
                player_who_won = board[row][0]

            
        for col in range(3):
            for row in range(3):
                if board[0][col] != board[row][col]:
                    break
            else: 
                player_who_won = board[0][col]
            
        for val in range(3):
            if board[0][0] != board[val][val]:
                break
        else:
            player_who_won = board[0][0]
            
        for val in reversed(range(3)):
            for val_2 in range(3):
                if board[2][2] != board[val_2][val]:
                    break
            else:
                player_who_won = board[2][2]
                
        if player_who_won == self.players[1]: return 1
        elif player_who_won == self.players[0]: return -1
        else: return 0
        
    def stop_game(self):
        for x in range(3):
            for y in range(3):
                self.button_arr[x][y]['state'] = 'disabled'
    
    def restart_game(self):
        for x in range(3):
            for y in range(3):
                self.board[x][y] = ''
                self.button_arr[x][y]['text'] = self.board[x][y]
                self.button_arr[x][y]['state'] = 'normal'
                
    def full_board(self, board):
        game_end = True
        for x in range(3):
            for y in range(3):
                if board[x][y] == '':
                    game_end = False
                    return game_end
        return game_end