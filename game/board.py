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
        
        self.start_players()
        
    def start_players(self):
        self.players = np.array(["O", "X"], ndmin=1);
        self.opponent_player_value = random.choice([0,1]);
        self.human_player_value = int(not self.opponent_player_value)
        self.current_player = self.human_player_value
        self.opponent = Player_AI(self.opponent_player_value, self.human_player_value, self)
        print(self.opponent_player_value)
        print(self.human_player_value)
        
    def createBoard(self):
        self.board = np.array([['','',''],
                              ['','',''],
                              ['','','']])
        self.button_arr = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype=Button)
        
        for x in range(3):
            for y in range(3):
                self.button_arr[x][y] = Button(self.frame, text="", width=23, height=10, command=lambda row=x, col=y: self.player_move(row, col))
                self.button_arr[x][y].grid(row=x, column=y)
    
    def player_move(self,row, col):  
        player_played = False       
        if self.board[row][col] == '' and self.current_player == self.human_player_value and not self.check_win(self.board):
            self.board[row][col] = self.players[self.human_player_value]
            self.button_arr[row][col]['text'] = self.board[row][col]
            player_played = True
        
        if(player_played):
            if self.check_win(self.board) == 1:
                self.stop_game()
                print('X won')
            elif self.check_win(self.board) == -1:
                self.stop_game()
                print('O won')
            elif self.full_board(self.board):
                self.stop_game()
                print('Tied')     
            else:
                self.current_player = not self.current_player
                self.ai_move()
            
        
        
        
    def ai_move(self):
        initial_move = True
        if len(self.board[self.board == self.players[self.opponent_player_value]]) != 0: initial_move = False
        
        if not initial_move:
            next_state = self.opponent.run_ai()
            self.board = next_state
        else:
            random_spot_array = np.where(self.board == '')
            random_spot = [random.choice(x) for x in random_spot_array]
            self.board[random_spot[0], random_spot[1]] = self.players[self.opponent_player_value]
            
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
        else:
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
            
        for val in range(3):
            if board[0][2] != board[val][ (val - 2) * -1]:
                break
        else:
            player_who_won = board[0][2]
                
                
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
                self.button_arr[x][y]['text'] = ''
                if self.button_arr[x][y]['state'] == 'disabled':
                    self.button_arr[x][y]['state'] = 'normal'
        
        self.start_players()
        
    def full_board(self, board):
        game_end = True
        for x in range(3):
            for y in range(3):
                if board[x][y] == '':
                    game_end = False
                    return game_end
        return game_end
    
    def is_game_over(self, board):
        return self.check_win(board) != 0 or self.full_board(board)