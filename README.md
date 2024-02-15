# AI-Mancala-Player

Welcome to the AI Mancala player README! This project implements an AI player for the game of Kalah, utilizing the Minimax algorithm for decision-making. Below, you'll find a brief overview of the game, the Minimax algorithm, an explanation of the provided code, and the heuristics used for move evaluation.

## Game Description

Kalah is a traditional board game played between two players. Each player has six pits (holes) containing six stones each, and an additional larger pit known as the Kalah, which acts as a score tracker. Players take turns to pick up stones from one of their pits and distribute them counterclockwise into subsequent pits, including their Kalah but not the opponent's. The game continues until one player has captured more than 36 stones, at which point the player with the most stones wins.

## Minimax Algorithm

The Minimax algorithm is a decision-making algorithm commonly used in two-player games. It evaluates possible moves by recursively exploring the game tree, assuming that the opponent plays optimally. The algorithm alternates between maximizing the score for the AI player and minimizing the score for the opponent, ultimately selecting the move that leads to the best possible outcome for the AI player.

For a detailed explanation of how the Minimax algorithm works and its implementation in the AI Mancala player, please refer to the [Minimax Algorithm Guide](link-to-your-minimax-guide-page) page.

## Heuristics

The AI player uses heuristic functions to evaluate the desirability of different game states. Here are the heuristics used:

- **Total Points**: Maximizes the difference in total points between the player and the opponent.
- **Total Stones**: Evaluates the difference between the total number of stones on each player's side, giving more weight to stones closer to the Kalah.
- **Double Turns**: Rewards the player for achieving a double turn, where the last stone lands in the player's Kalah.
- **Increase Multiplier**: Increases the weight of the Total Points heuristic to prioritize scoring over other factors.

## Usage

To utilize the AI Mancala player, you'll need access to the UI code, which is not provided here. However, the AI Mancala player code itself functions independently of any specific UI implementation. Given a game state, it can be easily integrated with any UI components to facilitate gameplay.

The `ai` class provides the functionality for move generation and evaluation, while the `state` class represents the current state of the game. You can integrate these components into your existing UI code to create a seamless Mancala gaming experience.

Here's a brief overview of how to integrate the AI Mancala player with your UI:

1. **Instantiate AI**: Create an instance of the `ai` class to access its methods for move generation and evaluation.

   ```python
   # Example usage
   player_ai = ai()
   ```

2. **Get Game State**: Obtain the current game state from your UI components. This includes the number of stones in each pit and the Kalah for both players.

3. **Call AI Method**: Use the `move` method of the AI player to calculate the next move based on the current game state.

   ```python
   # Example usage
   chosen_move = player_ai.move(a, b, a_fin, b_fin, depth)
   ```

4. **Integrate with UI**: Incorporate the chosen move into your UI logic to update the game state and display the changes to the players.

By integrating the AI Mancala player code with your UI, you can provide players with an intelligent opponent for the game of Kalah. If you encounter any issues or have questions about integration, feel free to reach out for assistance!
