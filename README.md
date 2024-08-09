# Tic-Tac-Toe Game

This is a simple command-line Tic-Tac-Toe game implemented in Python. The game allows two players to play against each other, choosing their names and symbols, and taking turns to mark their symbol on a 3x3 grid.

## Features

- **Two Players**: Each player can choose their name and a single-letter symbol.
- **Simple Menu**: The game features a main menu and an end-game menu to start, restart, or quit the game.
- **Board Display**: The current state of the game board is displayed after each turn.
- **Win/Draw Detection**: The game checks for win conditions after each turn and declares the winner or a draw when applicable.
- **Replayability**: After the game ends, players can choose to restart the game or quit.

## How to Play

1. **Start the Game**: Run the game in your Python environment. You'll be greeted with the main menu.
2. **Choose Players**: Enter the details for two players (names and symbols). Symbols should be a single letter.
3. **Play the Game**: Players take turns to choose a cell on the 3x3 grid to place their symbol. The game board will update after each move.
4. **Winning**: The first player to align three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
5. **Draw**: If all cells are filled without any player winning, the game is declared a draw.
6. **End Game**: After the game ends, you can choose to restart or quit the game.

## Code Structure

- `Player`: A class representing a player in the game. Handles choosing names and symbols.
- `Menu`: A class representing the game menus. Displays the main and end-game menus.
- `Board`: A class representing the game board. Handles displaying the board, updating it with player moves, and checking for valid moves.
- `Game`: The main class controlling the game logic. Manages player turns, win/draw checks, and game flow.

## Running the Game

To run the game, ensure you have Python installed. Save the code to a file named `tic_tac_toe.py` and run the file using:

```bash
python tic_tac_toe.py
```

Follow the on-screen instructions to play the game.

## Example

Here's a simple gameplay example:

```
Welcome to X-O game
1. Start game
2. Quit game
Please choose your number: 1
--------------------
Player 1, enter your details
Enter your name (letters only): Alice
--------------------
Alice, choose your symbol (a single letter): X
--------------------
Player 2, enter your details
Enter your name (letters only): Bob
--------------------
Bob, choose your symbol (a single letter): O
--------------------
1|2|3
------
4|5|6
------
7|8|9
Alice's turn (X)
--------------------
Choose a cell (1-9): 1
...
```

## Contributions

Feel free to fork this repository and submit pull requests if you'd like to improve the game or add new features!

## License

This project is open-source and available
