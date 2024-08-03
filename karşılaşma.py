import chess
import random

def white_bot(board):
    # Beyaz bot açılış hamleleri (1.e4, 2.Nf3, 3.Bb5 vs.)
    opening_moves = [
        "e2e4",  # 1. e4
        "g1f3",  # 2. Nf3
        "f1b5"   # 3. Bb5
    ]
    
    # İlk üç hamlede açılış hamlelerini yap
    move_number = len(board.move_stack)
    if move_number < len(opening_moves):
        move = chess.Move.from_uci(opening_moves[move_number])
        if board.is_legal(move):
            return move
    # Daha sonra rastgele hamleler yap
    return random_move(board)

def black_bot(board):
    # Siyah bot açılış hamleleri (1...e5, 2...Nc6, 3...Nf6 vs.)
    opening_moves = [
        "e7e5",  # 1... e5
        "g8f6",  # 2... Nf6
        "b8c6"   # 3... Nc6
    ]
    
    # İlk üç hamlede açılış hamlelerini yap
    move_number = len(board.move_stack)
    if move_number % 2 == 1 and (move_number // 2) < len(opening_moves):
        move = chess.Move.from_uci(opening_moves[move_number // 2])
        if board.is_legal(move):
            return move
    # Daha sonra rastgele hamleler yap
    return random_move(board)

def random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def print_game_status(board):
    move_number = len(board.move_stack)
    print(f"Hamle: {move_number + 1}")
    print(board)
    print("\n")

def play_game():
    # Satranç tahtasını oluştur
    board = chess.Board()

    # Botların karşılıklı oynadığı oyun
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = white_bot(board)
        else:
            move = black_bot(board)

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

    return result

# Ana döngü: Her oyun berabere bitiyorsa yeni bir oyun başlat
game_number = 1
total_games_played = 0

while True:
    print(f"Maç {game_number}")
    result = play_game()
    total_games_played += 1
    if result != "1/2-1/2":
        break
    game_number += 1
    print("Beraberlik, yeni maç başlıyor...\n")

print(f"Toplam oynanan oyun sayısı: {total_games_played}")
