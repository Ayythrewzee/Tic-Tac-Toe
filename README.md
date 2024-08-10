# Tic-Tac-Toe with Q-Learning AI

This project implements a Tic-Tac-Toe game where you can play against an AI trained using Q-learning. The AI and the game interface are built using Python's `tkinter` library for the graphical user interface (GUI).

## Features

- **Q-Learning AI**: An AI that learns to play Tic-Tac-Toe through reinforcement learning using Q-learning.
- **GUI**: A user-friendly graphical interface using `tkinter` for interactive gameplay.
- **Training**: The AI is trained using Q-learning before playing against the user.

## Prerequisites

- Python 3.x
- NumPy (for numerical operations)
- Tkinter (for GUI)

You can install the necessary Python libraries using pip:

```sh
pip install numpy
```

Tkinter comes pre-installed with Python. If it's not installed, you might need to install it separately depending on your Python distribution.

## Getting Started

1. **Clone the Repository**: If you haven't already, clone this repository to your local machine.

    ```sh
    git clone https://github.com/yourusername/tic-tac-toe.git
    ```

2. **Navigate to the Project Directory**:

    ```sh
    cd tic-tac-toe
    ```

3. **Run the Game**: Execute the Python script to start the game.

    ```sh
    python tic_tac_toe_gui.py
    ```

## Code Overview

### 1. `TicTacToe` Class

This class defines the game environment for Tic-Tac-Toe.

- **Methods**:
  - `__init__()`: Initializes the board and the current player.
  - `reset()`: Resets the board and current player.
  - `get_state()`: Returns the current board state as a flattened array.
  - `is_winner(player)`: Checks if the specified player has won.
  - `is_draw()`: Checks if the game is a draw.
  - `make_move(row, col)`: Makes a move for the current player and returns the reward.
  - `get_available_actions()`: Returns a list of available actions (empty cells).

### 2. `QLearningAgent` Class

This class implements the Q-learning algorithm.

- **Methods**:
  - `__init__(alpha, gamma, epsilon)`: Initializes the Q-learning parameters.
  - `get_q_value(state, action)`: Returns the Q-value for a given state-action pair.
  - `update_q_value(state, action, reward, next_state)`: Updates the Q-value based on the reward and next state.
  - `choose_action(state, available_actions)`: Chooses an action based on the exploration-exploitation tradeoff.

### 3. `train_agent(episodes)`

Trains the Q-learning agent by simulating multiple games of Tic-Tac-Toe.

- **Parameters**:
  - `episodes`: Number of training episodes (games).

### 4. `TicTacToeGUI` Class

This class creates the GUI using Tkinter.

- **Methods**:
  - `__init__(root)`: Initializes the GUI and sets up the game and agent.
  - `create_widgets()`: Creates buttons for the Tic-Tac-Toe board.
  - `player_move(row, col)`: Handles moves made by the player.
  - `ai_move()`: Handles moves made by the AI.
  - `update_board()`: Updates the GUI to reflect the current game state.
  - `end_game(reward)`: Displays the game result and resets the game.
  - `reset_game()`: Resets the game state and board for a new round.

## Usage

- **Play the Game**: The game window will open with a 3x3 grid. Click on an empty cell to make a move. The AI will automatically make a move in response.
- **Game End**: A message box will appear when the game ends, indicating the result (win, draw, or AI win). The game will automatically reset for a new round.


## Future Improvements

- Enhance AI with more advanced algorithms or strategies.
- Add functionality for different difficulty levels.
- Implement a system to save and load game states.


## Contact

For any questions or suggestions, please reach out to [christian.deshong@gmail.com].
