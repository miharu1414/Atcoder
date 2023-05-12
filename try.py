import random

class Player:
    def __init__(self):
        self.score = 0
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    def get_last_move(self):
        if len(self.moves) > 0:
            return self.moves[-1]
        else:
            return None

    def get_score(self):
        return self.score


def play_game(num_rounds):
    player1 = Player()
    player2 = Player()

    for i in range(num_rounds):
        # Get last move of each player
        last_move1 = player1.get_last_move()
        last_move2 = player2.get_last_move()

        # Determine each player's move
        if last_move1 == 'C' and last_move2 == 'C':
            move1 = 'C'
            move2 = 'C'
            player1.score += 3
            player2.score += 3
        elif last_move1 == 'C' and last_move2 == 'D':
            move1 = 'D'
            move2 = 'C'
            player1.score += 0
            player2.score += 5
        elif last_move1 == 'D' and last_move2 == 'C':
            move1 = 'C'
            move2 = 'D'
            player1.score += 5
            player2.score += 0
        else:
            move1 = 'D'
            move2 = 'D'
            player1.score += 1
            player2.score += 1

        # Add moves to each player's history
        player1.add_move(move1)
        player2.add_move(move2)

    # Print final scores
    print("Player 1 score:", player1.get_score())
    print("Player 2 score:", player2.get_score())


play_game(10)