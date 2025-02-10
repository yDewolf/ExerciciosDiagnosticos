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
        pass


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


jogo = Game()
jogo.start()