# Galactic Odyssey

Galactic Odyssey is an interactive command-line game exploring space as an astronaut and making choices that shape your mission's outcome.

### Runnig the game

Run the game by executing 'main.py' or 'python main.py'

### Gameplay

1. **Start the Game:**  
   Enter your astronaut name to begin your mission. Choose a spaceship—each with unique attributes.

2. **Explore & Decide:**  
   Navigate destinations like the Red Planet or Comet Arcand make key decisions that impact your journey.

3. **Outcomes:**  
   Your choices lead to various outcomes, from discovering alien artifacts to facing mission failures. If you fail, you can restart and try different paths.

## How the Program Works

The game is structured into three main Python files:

### 1. `main.py`

**Main Function:**  
Serves as the entry point of the game:

- **Setup:** Prompts the player for their astronaut name and creates a `Player` object.
- **Start Game:** Instantiates the `Game` class and starts the adventure by calling `start_adventure()`.

### 2. `player.py`

**Player Class:**  
Defines the `Player` class which represents the player in the game:

- **Attributes:** The player's name and their alive status (`True` or `False`).

- **Methods:**
  - `reset()`: Resets the player's alive status to `True` for a new game.
  - Getter and setter methods for the player's name and alive status.

### 3. `game.py`

**Game Class:**  
The core of the game logic lives in this class:

- **Initialization:** The game is initialized with a `Player` object.
- **Adventure Flow:**
  - `start_adventure()`: Begins the game by welcoming the player and guiding them through their first choices.
  - **Decision-Making:** Methods like `choose_spaceship()`, `explore_destination()`, and `analyze_artifact()` guide the player through different game scenarios based on their choices.
- **Outcomes:**
  - `game_over(reason)`: Displays the game-over message and allows the player to restart or exit the game.
  - `ask_to_play_again()`: Prompts the player to decide whether to restart the game or exit.

**Helper Methods:**

- `get_decision(prompt, valid_choices)`: Continuously prompts the player until they make a valid choice.
