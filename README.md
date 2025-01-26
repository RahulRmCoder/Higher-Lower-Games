# Higher-Lower-Games
# Higher-Lower Instagram Followers Game

This project implements an interactive Python game that challenges players to guess which account has more followers on Instagram. It uses a simple text-based interface to display comparisons and keeps track of the player's score until they make an incorrect guess.

---

## Table of Contents
- [Game Description](#game-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Game Data](#game-data)
- [Acknowledgements](#acknowledgements)

---

## Game Description
The Higher-Lower Instagram Followers Game allows players to test their knowledge of popular Instagram accounts by guessing which account has more followers. Players are presented with two accounts, their descriptions, and countries, and they have to choose "A" or "B" as the account with more followers.

---

## Features
1. **Dynamic Comparisons**: Randomly selects Instagram accounts for comparison from a pre-defined dataset.
2. **Score Tracking**: Tracks the player’s score until they make an incorrect guess.
3. **Text-based Interface**: Provides a clean and simple output with ASCII art visuals.
4. **Randomized Account Selection**: Ensures that comparisons are unique and do not repeat consecutively.

---

## Technologies Used
- **Python**: Core programming language for logic and execution.
- **ASCII Art**: Visual enhancements for a better user experience.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/RahulRmCoder/Higher-Lower-Game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Higher-Lower-Game
   ```
3. Ensure Python 3.x is installed on your system.
4. Run the game script:
   ```bash
   python game.py
   ```

---

## Usage
1. Start the game by running the script.
2. Follow the prompts to make your guesses.
3. The game will display your score and terminate once you make an incorrect guess.

---

## Gameplay
1. **Start the Game**:
   - The game begins by displaying the first account comparison.
   - Players are prompted to choose "A" or "B" based on their guess of which account has more Instagram followers.

2. **Account Information**:
   - Each account displays:
     - Name
     - Description
     - Country

3. **Scoring**:
   - Correct guesses increase the score.
   - The game continues until the player makes a wrong guess.

4. **End of Game**:
   - If the player guesses incorrectly, the game ends and displays the final score.

---

## Game Data
The game uses a dataset of Instagram accounts, each containing:
- **Name**: The account's name.
- **Follower Count**: Total followers in millions.
- **Description**: A short description of the account.
- **Country**: The account's origin country.

---

## Example Output
```plaintext
  __  ___       __             
 / / / (_)___ _/ /_  ___  _____
/ /_/ / / __ `/ __ \/ _ \/ ___/
/ __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
 / /  /____/_      _____  _____
/ /   / __ \ | /| / / _ \/ ___/
/ /___/ /_/ / |/ |/ /  __/ /    
/_____\____/|__/|__/\___/_/     

Compare A: Cristiano Ronaldo, Footballer, Portugal
 _    __    
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Against B: Kylie Jenner, Reality TV personality and businesswoman, United States
Who has more followers on Instagram? Type 'A' or 'B':
```

---

## Acknowledgements
- ASCII Art generated using [patorjk.com](https://patorjk.com/software/taag/).
- Instagram follower data is simulated and may not reflect real-time values.

