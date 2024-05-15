import numpy as np

class Player_AI():    
    def __init__(self, player_value, opponent_value, game):
        self.player_value = player_value
        self.opponent_value = opponent_value
        self.game = game
        
    
    def run_ai(self): 
        min_value = np.inf 
        max_value = -np.inf 

        if self.player_value == 0:
            for x in range(3):
                for y in range(3):
                    if self.game.board[x][y] == '':
                        next_state = self.game.board.copy()
                        next_state[x][y] = "O"   
                        
                        next_min_val = self.maximazing_function(next_state)
                        if next_min_val < min_value:
                            min_value = next_min_val
                            self.state = next_state
                                        
                    
                       
        elif self.player_value == 1:
            for x in range(3):
                for y in range(3):
                    if self.game.board[x][y] == '':
                        next_state = self.game.board.copy()
                        next_state[x][y] = "X"   
     
                        next_max_val = self.minimizing_funtion(next_state)
                        if next_max_val > max_value:
                            max_value = next_max_val
                            self.state = next_state  
        
        return self.state
                                    
    def minimizing_funtion(self, board_state): 
        min_value = np.inf 

        if self.game.is_game_over(board_state):
            return self.game.check_win(board_state)
                
        for x in range(3):
            for y in range(3):
                if board_state[x][y] == '':
                    new_state = board_state.copy()  
                    new_state[x][y] = 'O'
                                        
                    multiplier = len(new_state[new_state == ''])
                    min_value = min(self.maximazing_function(new_state), min_value * multiplier);
                    
        return min_value
                    
                    
    def maximazing_function(self, board_state):
        max_value = -np.inf 
        
        if self.game.is_game_over(board_state):
            return self.game.check_win(board_state)
                
        for x in range(3):
            for y in range(3):
                if board_state[x][y] == '':
                    new_state = board_state.copy()
                    new_state[x][y] = "X"
                    
                    multiplier = len(new_state[new_state == ''])
                    max_value = max(self.minimizing_funtion(new_state), max_value * multiplier);
                    
        return max_value
                    
