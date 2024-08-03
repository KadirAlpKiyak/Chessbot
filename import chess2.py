import chess
import random

# Satranç tahtasını oluştur
board = chess.Board()

def closed_game_opening(board):
    # Closed Game açılış hamleleri
    opening_moves = [
        "d2d4",  # 1. d4
        "d7d5"   # 1... d5
    ]
    
    # İlk iki hamlede açılış hamlelerini yap
    move_number = len(board.move_stack)
    if move_number < len(opening_moves):
        move = chess.Move.from_uci(opening_moves[move_number])
        if board.is_legal(move):
            return move
    # Daha sonra rastgele hamleler yap
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
        move = closed_game_opening(board)
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
