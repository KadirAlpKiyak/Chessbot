import chess
import random

# Satranç tahtasını oluştur
board = chess.Board()

def ruy_lopez_opening(board):
    # Ruy Lopez açılış hamleleri
    opening_moves = [
        "e2e4",  # 1. e4
        "g1f3",  # 2. Nf3
        "f1b5"   # 3. Bb5
    ]
    
    move_number = len(board.move_stack)
    if move_number < len(opening_moves):
        move = chess.Move.from_uci(opening_moves[move_number])
        if board.is_legal(move):
            return move
    return None

def random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def print_game_status(board):
    move_number = len(board.move_stack)
    print(f"Hamle: {move_number + 1}")
    print(board)
    print("\n")

# Botun hamlesini yap
while not board.is_game_over():
    if board.turn == chess.WHITE:
        move = ruy_lopez_opening(board)
        if move is None:
            move = random_move(board)
    else:
        move = random_move(board)

    board.push(move)
    print_game_status(board)

# Oyun bittiğinde sonucu belirt
result = board.result()
if result == "1-0":
    winner = "White"
elif result == "0-1":
    winner = "Black"
else:
    winner = "Draw"

print(f"Oyun bitti: {winner} kazandı!")
print(f"Sonuç: {result}")
