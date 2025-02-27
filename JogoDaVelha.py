class Game:
    board: tuple[tuple]

    current_player: int = 0 # 0 ou 1
    winner: int = -1 # 0 -> player 0; 1 -> player 1; 2 -> Empate
    finished: bool = False

    def __init__(self):
        # -1 é quando ninguém colocou nada ali
        self.board = (
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1])

    def start(self):
        while not self.finished:
            self.handle()

    def handle(self):
        self.print_board()

        print(f"Vez do jogador {self.current_player + 1}!")
        empty_positions = self.get_possible_positions()

        decoded_pos = ()
        while decoded_pos == () or not empty_positions.__contains__(decoded_pos):
            pos = input("Selecione uma posição (Exemplo: A1 -> Esquerda em cima; C3 -> Direita embaixo): ")
            decoded_pos = Game.decode_pos(pos)

        self.board[decoded_pos[0]][decoded_pos[1]] = self.current_player # Set the position to the current player

        self.check_winner()
        self.print_board()
        self.current_player = int(not bool(self.current_player))

    def check_winner(self):
        winner = -1
        def check_rows():
            prev_value: int = 2

            for row in self.board:
                for value in row:
                    if prev_value == 2:
                        prev_value = value
                        continue

                    if value != prev_value:
                        return (False, value)
            
                return (True, prev_value)

        def check_columns():
            prev_value: int = 2

            for column in range(len(self.board[0])):
                for row in range(len(self.board)):
                    value = self.board[row][column]

                    if prev_value == 2:
                        prev_value = value
                        continue

                    if value != prev_value:
                        return (False, value)
            
                return (True, prev_value)

        def check_diagonals():
            diagonals = [
                [(0, 0), (1, 1), (2, 2)],
                [(2, 0), (1, 1), (0, 2)]
            ]

            for row in diagonals:
                prev_value = self.board[row[0][0]][row[0][1]]

                skip_row = False
                for pos in row:
                    if self.board[pos[0]][pos[1]] != prev_value:
                        skip_row = True
                
                if skip_row == False:
                    return (True, prev_value)
            
            return (False, 2)
            
        def check_tie():
            for x in self.board:
                for y in x:
                    if y == -1:
                        return False
            
            return True

        results: tuple
        for i in range(4):
            match i:
                case 0:
                    results = check_rows()

                case 1:
                    results = check_columns()
                
                case 2:
                    results = check_diagonals()

                case 3:
                    if check_tie():
                        winner = 2 # Tie

            if results[0]:
                winner = results[1]
                break

        if winner != -1:
            if winner != 2:
                print(f"Player {winner + 1} Won!")
            else:
                print(f"That's a Tie!")

            self.finished = True
            self.winner = winner


    def decode_pos(pos: str) -> tuple:
        valid_positions: list = [
            "a", "b", "c"
        ]

        if not valid_positions.__contains__(pos[0].lower()):
            return ()

        if len(pos) != 2:
            return ()
        
        return (valid_positions.index(pos[0].lower()), int(pos[1]) - 1)

    def get_possible_positions(self) -> list[tuple]:
        positions: list[tuple] = []
        for x in range(len(self.board)):

            for y in range(len(self.board[x])):
                if self.board[x][y] == -1: # Empty
                    positions.append((x, y))
        
        return positions


    def print_board(self):
        rows: list = [
            "a", "b", "c"
        ]

        board_str: str = "X | 1 2 3\n"
        for x in range(len(self.board)):
            row = rows[x].upper() + " | "
            for y in range(len(self.board[x])):
                match self.board[x][y]:
                    case 0:
                        row += "X"
                    case 1:
                        row += "O"

                    case _: 
                        row += "="

                row += " "
            
            board_str += row + "\n"
        
        print(board_str)

scoreboard: list[int] = [0, 0]

while True:
    jogo = Game()
    jogo.start()
    if jogo.winner < 2:
        scoreboard[jogo.winner] += 1
        
    print(f"Current Scoreboard: {scoreboard[0]} x {scoreboard[1]}")

    play_again: bool = bool(int(input("Play Again? (1 -> Yes; 0 -> No): ")))
    if not play_again:
        break