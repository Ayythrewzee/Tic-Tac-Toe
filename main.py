import numpy as np
import random
import tkinter as tk
from tkinter import messagebox

# Constants
BOARD_SIZE = 3
BUTTON_SIZE = 100

# Game Environment
class TicTacToe:
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.current_player = 1

    def get_state(self):
        return self.board.flatten()

    def is_winner(self, player):
        win_conditions = [
            self.board[i, :] for i in range(BOARD_SIZE)
        ] + [
            self.board[:, i] for i in range(BOARD_SIZE)
        ] + [
            np.diag(self.board),
            np.diag(np.fliplr(self.board))
        ]
        return any(np.all(line == player) for line in win_conditions)

    def is_draw(self):
        return not np.any(self.board == 0) and not self.is_winner(1) and not self.is_winner(-1)

    def make_move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            if self.is_winner(self.current_player):
                return 1
            elif self.is_draw():
                return 0
            self.current_player *= -1
            return None
        else:
            raise ValueError("Invalid move")

    def get_available_actions(self):
        return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if self.board[r, c] == 0]

# Q-Learning Agent
class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        return self.q_table.get((tuple(state), action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        available_actions = [(r * BOARD_SIZE + c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)]
        best_next_action = max(
            available_actions,
            key=lambda a: self.get_q_value(next_state, a),
            default=None
        )
        td_target = reward + self.gamma * self.get_q_value(next_state, best_next_action)
        td_error = td_target - self.get_q_value(state, action)
        new_q_value = self.get_q_value(state, action) + self.alpha * td_error
        self.q_table[(tuple(state), action)] = new_q_value

    def choose_action(self, state, available_actions):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_actions)
        else:
            q_values = [self.get_q_value(state, a) for a in available_actions]
            max_q_value = max(q_values, default=0)
            best_actions = [a for a, q in zip(available_actions, q_values) if q == max_q_value]
            return random.choice(best_actions)

def train_agent(episodes):
    agent = QLearningAgent()
    game = TicTacToe()

    for _ in range(episodes):
        game.reset()
        state = game.get_state()
        done = False

        while not done:
            available_actions = game.get_available_actions()
            action = agent.choose_action(state, [r * BOARD_SIZE + c for r, c in available_actions])
            row, col = divmod(action, BOARD_SIZE)
            reward = game.make_move(row, col)
            next_state = game.get_state()

            if reward is not None:
                if reward == 1:
                    agent.update_q_value(state, action, 1, next_state)
                elif reward == 0:
                    agent.update_q_value(state, action, 0.5, next_state)
                done = True
            else:
                agent.update_q_value(state, action, 0, next_state)
                state = next_state

    return agent

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.game = TicTacToe()
        self.agent = train_agent(10000)
        self.buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        self.create_widgets()

    def create_widgets(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                button = tk.Button(self.root, text="", width=BUTTON_SIZE//20, height=BUTTON_SIZE//20, font=('Arial', 24),
                                   command=lambda row=r, col=c: self.player_move(row, col))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def player_move(self, row, col):
        if self.game.board[row, col] == 0 and self.game.current_player == 1:
            reward = self.game.make_move(row, col)
            self.update_board()
            if reward is not None:
                self.end_game(reward)
            else:
                self.ai_move()

    def ai_move(self):
        state = self.game.get_state()
        available_actions = self.game.get_available_actions()
        action = self.agent.choose_action(state, [r * BOARD_SIZE + c for r, c in available_actions])
        row, col = divmod(action, BOARD_SIZE)
        reward = self.game.make_move(row, col)
        self.update_board()
        if reward is not None:
            self.end_game(reward)

    def update_board(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                value = self.game.board[r, c]
                if value == 1:
                    self.buttons[r][c].config(text="X", disabledforeground="blue")
                elif value == -1:
                    self.buttons[r][c].config(text="O", disabledforeground="red")
                self.buttons[r][c].config(state="disabled" if value != 0 else "normal")

    def end_game(self, reward):
        if reward == 1:
            messagebox.showinfo("Game Over", "Player X wins!")
        elif reward == -1:
            messagebox.showinfo("Game Over", "AI O wins!")
        elif reward == 0:
            messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.game.reset()
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                self.buttons[r][c].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()