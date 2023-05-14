import random

class Player:
    def __init__(self,id,mode):
        self.score = 0
        self.idx = id
        self.mode = mode
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    
    def decision(self,history):
        if self.mode == "TFT":
            if len(history) == 0:
                return -1
            return history[-1][1]
        
        elif self.mode == "D-TFT":
            if len(history) == 0:
                return 1
            return history[-1][1]
        
        elif self.mode == "ALL-C":
            return -1
        
        elif self.mode == "":
            pass
            
            

    def get_score(self):
        return self.score


def play_game(num_rounds):
    def Str(x):
        if x == -1:
            return "C"
        return "D"
    
    def noize(x):
        return -x
        
    player1 = Player(0,"TFT")
    player2 = Player(1,"D-TFT")
    history1 = [ ]
    history2 = [ ]

    for i in range(num_rounds):
        # C,Dどちらを出すか判断する
        move1 = player1.decision(history1)
        move2 = player2.decision(history2)
        
        rand = random.random()
        if rand <= 0.2:
            move1 = noize(move1)
        rand = random.random() 
        if rand <= 0.2:
            move2 = noize(move2) 
            
            
            
        
        # 自分と相手の手を履歴データに追加する
        history1.append([move1,move2])
        history2.append([move2,move1])  
         
        # 利得の計算を行う
        # Determine each player's move
        if  Str(move1) == 'C' and Str(move2) == 'C':
            player1.score += 4
            player2.score += 4
                        
        elif Str(move1) == 'C' and Str(move2) == 'D':
            player1.score += -1
            player2.score += 6
            
        elif Str(move1) == 'D' and Str(move2) == 'C':
            player1.score += 6
            player2.score += -1
            
        else:
            player1.score += 0
            player2.score += 0

        # Add moves to each player's history
        player1.add_move(move1)
        player2.add_move(move2)

    # Print final scores
    history1_str = []
    for a,b in history1:
        history1_str.append([Str(a),Str(b)])
        
    print(history1_str)
    print(f"Player 1 mode:{player1.mode} score:", player1.get_score())
    print(f"Player 2 mode:{player2.mode} score:", player2.get_score())


play_game(int(input("繰り返しの数：")))