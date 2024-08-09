# Class representing a player in the game
class Player:
    def __init__(self):
        # Initialize player with an empty name and symbol
        self.name = ""
        self.symbol = ""

    # Method for the player to choose their name
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():  # Ensure the name contains only letters
                self.name = name
                break
            else:
                print("Invalid name. Please use letters only.")

    # Method for the player to choose their symbol (X or O)
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (a single letter): ")
            if symbol.isalpha() and len(symbol) == 1:  # Ensure the symbol is a single letter
                self.symbol = symbol.upper()  # Convert the symbol to uppercase
                break
            else:
                print("Invalid symbol. Please use a single letter.")

# Class representing the game menu
class Menu:
    # Method to display the main menu
    def display_main_menu(self):
        print("Welcome to X-O game")
        print('1. Start game')
        print('2. Quit game')
        choice = input("Please choose your number: ")
        print("-" * 20)
        return choice

    # Method to display the end game menu
    def display_end_menu(self):
        print('1. Restart game')
        print('2. Quit game')
        print("-" * 20)
        choice = input("Please choose your number: ")
        return choice

# Class representing the game board
class Board:
    def __init__(self):
        # Initialize the board with numbers 1-9
        self.board = [str(i) for i in range(1, 10)]

    # Method to display the board
    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))  # Print the board in a 3x3 format
            if i < 6:
                print("-" * 6)

    # Method to update the board with a player's symbol
    def update_board(self, choice, symbol):
        if self.is_valid_movement(choice):  # Check if the move is valid
            self.board[choice - 1] = symbol  # Update the board
            return True
        return False

    # Method to check if a move is valid
    def is_valid_movement(self, choice):
        return self.board[choice - 1].isdigit()  # Valid if the cell is still a digit

    # Method to reset the board for a new game
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

# Class representing the overall game logic
class Game:
    def __init__(self):
        # Initialize the game with two players, a board, and a menu
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0  # Keep track of the current player

    # Method to start the game
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()  # Set up player names and symbols
            self.play_game()  # Start the game loop
        else:
            self.quit_game()

    # Method to set up the players
    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details")
            player.choose_name()
            print("-" * 20)
            player.choose_symbol()
            print("-" * 20)

    # Method to play the game
    def play_game(self):
        while True:
            self.play_turn()  # Play a single turn
            if self.check_win():  # Check if the current player has won
                print(f"{self.players[self.current_player_index].name} wins!")
                print('-' * 20)
                choice = self.menu.display_end_menu()
                if choice == "1":
                    self.restart_game()  # Restart the game
                else:
                    self.quit_game()
                    break
            elif self.check_draw():  # Check if the game is a draw
                print("It's a draw!")
                print('-' * 20)
                choice = self.menu.display_end_menu()
                if choice == "1":
                    self.restart_game()  # Restart the game
                else:
                    self.quit_game()
                    break

    # Method to check if the game is a draw
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)  # A draw if no digits are left

    # Method to check if a player has won
    def check_win(self):
        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],
                            [0, 4, 8], [2, 4, 6]]  # Possible win combinations
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True  # Return True if a win combination is found
        return False

    # Method to play a single turn
    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        print('-' * 20)
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break  # Break loop if the move is valid
                else:
                    print('Invalid move. Try again.')
            except ValueError:
                print('Please enter a number between 1 and 9.')
        self.switch_player()  # Switch to the other player

    # Method to switch the current player
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    # Method to restart the game
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0  # Reset the current player index
        self.play_game()

    # Method to quit the game
    def quit_game(self):
        print("Thank you for playing!")
        exit()

# Create a Game instance and start the game
game = Game()
game.start_game()
