# 🔫 Buckshot Roulette CLI

A small **Python CLI game** inspired by the Russian-roulette-style gameplay of *Buckshot Roulette*, built as a fun programming project and a practical exercise in Python fundamentals and game logic.

The game runs entirely in the terminal and uses randomized live and blank shells, health management, multiple rounds, and winner screens.

> ⚠️ This is a fan-made learning project and is not affiliated with the creators of the original Buckshot Roulette.

---

## 🎮 About the Game

**Buckshot Roulette CLI** is a single-player terminal game where you face a dealer across **3 rounds**.

Each round loads a randomized magazine containing:

* 🔴 Live shells
* ⚪ Blank shells

You must decide whether to:

```text
1. Shoot Dealer
2. Shoot Yourself
```

Your goal is to survive the rounds and finish with more round wins than the dealer.

---

## ✨ Features

* 🎮 Terminal / CLI-based gameplay
* 🔀 Randomized shell generation
* 🔴 Live and blank ammunition
* ❤️ Player and dealer health system
* 🏆 Round winner system
* 👑 Final game winner screen
* 🎨 ASCII-art title screens
* 🔢 Three-round progression
* ⚠️ Input validation for invalid choices
* 🧩 Function-based program structure
* 🐍 Built entirely with Python's standard library

---

## 🧠 Python Concepts Used

This project was also created as a practical way to work with fundamental Python concepts.

### Core Python

* Variables
* Conditional statements
* `if / elif / else`
* `while` loops
* `for`-style list operations
* Functions
* Function parameters and return values
* Lists
* List methods
* String formatting
* `try / except`
* `match / case`
* Boolean conditions

### Randomization

The game uses Python's built-in `random` module to:

* Generate the number of shells
* Determine live and blank shell counts
* Shuffle the magazine
* Randomize the title ASCII art

### Game Logic

The project demonstrates how different functions can work together as a simple processing pipeline:

```text
Game Start
    ↓
ASCII Title
    ↓
Game Engine
    ↓
Load Magazine
    ↓
Generate Live / Blank Shells
    ↓
Player Choice
    ↓
Process Shot
    ↓
Update Health
    ↓
Determine Round Winner
    ↓
Final Game Result
```

---

## 🕹️ How to Play

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/buckshot-roulette-cli.git
```

### 2. Enter the project directory

```bash
cd buckshot-roulette-cli
```

### 3. Run the game

```bash
python3 main.py
```

On some systems you can also use:

```bash
python main.py
```

---

## 💻 Example Gameplay

```text
===========================================
     <***    BUCKSHOOT ROULETTE   ***>     
===========================================

 --- ROUND : 1

 **** HEALTH SECTION ****

 DEALER : 6 ❤️
 USER : 6 ❤️

 LIVE SHELLS : 2
 BLANK SHELLS : 2
 Total shells present : 4

 1. Shoot Dealer
 2. Shoot Yourself

Enter the choice:
```

Choose your action and see whether the chamber contains a live or blank shell.

---

## 🏆 Round System

The game contains **3 rounds** with different starting health values.

| Round | Player Health | Dealer Health |
| ----: | ------------: | ------------: |
|     1 |             6 |             6 |
|     2 |             5 |             5 |
|     3 |             3 |             3 |

The game keeps track of your round wins and the dealer's round wins.

At the end of the third round, the game displays the final result:

```text
👑 GAME OVER — YOU WIN ! 👑
```

or

```text
💀 GAME OVER — DEALER WINS ! 💀
```

or

```text
🤝 GAME OVER — DRAW ! 🤝
```

---

## 📂 Project Structure

```text
buckshot-roulette-cli/
│
├── main.py       # Main game implementation
├── README.md     # Project documentation
├── LICENSE       # Project license
├── .gitignore    # Git ignored files

```

---

## 🔧 Technologies Used

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

![CLI](https://img.shields.io/badge/Interface-CLI-000000?style=for-the-badge\&logo=gnubash\&logoColor=white)

![Git](https://img.shields.io/badge/Version_Control-Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)

![GitHub](https://img.shields.io/badge/Platform-GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)

---

## 🚀 Future Improvements

Some ideas for future versions:

* 🤖 Add dealer AI
* 🎒 Add usable items
* 🔫 Add different weapons
* ❤️ Add more advanced health mechanics
* 🎯 Add difficulty levels
* 🎨 Improve terminal UI
* 🔊 Add sound effects
* 💾 Add game statistics
* 🏅 Add score tracking
* 🔄 Add replay option
* 🧱 Split the project into multiple Python modules
* 🎨 Add a graphical interface using Pygame

---

## 📚 Learning Purpose

This project was created primarily as a **fun programming project and Python logic exercise**.

The goal was to understand how individual functions can work together to create a complete program, while practicing data processing, randomization, conditional logic, loops, input handling, and state management.

---

## 👨‍💻 Author

**Jatin Kumar Senapati**

Built with 🐍 Python and a little bit of chaos.

---

## ⭐ Support

If you find the project interesting, consider giving the repository a ⭐ on GitHub!
