#FurkanFilikci
# Oyun tahtasını oluşturmak için bir sözlük kullanabiliriz.
board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

current_player = 'X'  # Başlangıçta X oyuncusuyla başlayalım.
game_over = False

def display_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def check_winner(board):
    # Kazanma durumlarını kontrol edelim.
    winning_conditions = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Yatay
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Dikey
        ['1', '5', '9'], ['3', '5', '7']  # Çapraz
    ]

    for condition in winning_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True

    return False

def check_tie(board):
    # Tahta dolu olduğunda berabere biten bir oyun kontrol edelim.
    if ' ' not in board.values():
        return True
    return False

def play_game():
    global current_player, game_over

    while not game_over:
        display_board(board)

        position = input("Sıra " + current_player + ". Oyuncuda. Bir pozisyon seçin (1-9): ")

        if position not in board.keys() or board[position] != ' ':
            print("Geçersiz hamle. Lütfen boş bir pozisyon seçin.")
            continue

        # Seçilen pozisyona oyuncunun işaretini yerleştirelim.
        board[position] = current_player

        if check_winner(board):
            display_board(board)
            print("Tebrikler! Oyuncu " + current_player + " kazandı!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("Oyun berabere bitti!")
            game_over = True
        else:
            # Oyuncu değiştirme
            current_player = 'O' if current_player == 'X' else 'X'

play_game()
