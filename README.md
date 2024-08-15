# Galactic Odyssey

"Galactic Odyssey" is an interactive command-line game where you explore space as an astronaut, making choices that shape your mission's outcome.

## How the Program Works

### Gameplay

1. **Start the Game:**  
   Enter your astronaut name to begin your mission. Choose a spaceship—each with unique attributes.

2. **Explore & Decide:**  
   Navigate destinations like the Red Planet or Comet Arc. Make key decisions that impact your journey—whether to explore ancient ruins, analyze alien technology, or venture into unknown sectors.

3. **Outcomes:**  
   Your choices lead to various outcomes, from discovering alien artifacts to facing mission failures. If you fail, you can restart and try different paths.

### Running the Game

Run the game by executing `main.py`:

```bash
python main.py

## How the Code Works

The "Galactic Odyssey" program is structured into three main Python files: `game.py`, `main.py`, and `player.py`. Each file serves a specific purpose in creating the game's functionality.

### 1. `player.py`
**Player Class:**
This file defines the `Player` class, which represents the player in the game. The class includes:
- **Attributes:** The player's name and their alive status (`True` or `False`).
- **Methods:**
  - `reset()`: Resets the player's alive status to `True` for a new game.
  - Getter and setter methods for the player's name and alive status.

### 2. `game.py`
**Game Class:**
The core of the game logic resides in this class. Key functionalities include:

- **Initialization:** The game is initialized with a `Player` object.
- **Adventure Flow:**
  - `start_adventure()`: Begins the game by welcoming the player and guiding them through their first choices.
  - **Decision-Making:** Several methods like `choose_spaceship()`, `explore_destination()`, and `analyze_artifact()` guide the player through different game scenarios based on their choices.
- **Outcomes:**
  - `game_over(reason)`: Displays the game-over message and allows the player to restart or exit the game.
  - `ask_to_play_again()`: Prompts the player to decide whether to restart the game or exit.

**Helper Methods:**

- `get_decision(prompt, valid_choices)`: Continuously prompts the player until they make a valid choice, ensuring smooth gameplay.

### 3. `main.py`
**Main Function:**
This file serves as the entry point of the game:
- **Setup:** Prompts the player for their astronaut name and creates a `Player` object.
- **Start Game:** Instantiates the `Game` class and starts the adventure by calling `start_adventure()`.
```
