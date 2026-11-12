# RPG Battle Game

A simple text-based RPG game built with Python. The player takes on the role of a hero who travels through different story events, encounters enemies, takes damage, and finds healing along the way. The goal is to survive each encounter while managing your health.

## Features

- **Hero Class:** Uses object-oriented programming to manage the player's name, health, and maximum health.
- **Health Management:** Players can take damage and restore health throughout the game.
- **Randomized Events:** Damage and healing amounts are randomly generated using Python's `random` module.
- **Health Validation:** Prevents invalid health values and ensures health never exceeds the maximum or falls below zero.
- **Story Progression:** Players move through a sequence of events using loops and conditional statements.
- **Game Over System:** The game ends when the player's health reaches zero.

## Technologies Used

- Python 3
- Random module
- Object-Oriented Programming (OOP)

## Project Structure

```text
RPG-Game/
│
├── Hero.py
├── Enemy.py
└── README.md
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/kyne2005-dot/rpg-battle.git
```

2. Navigate into the project folder:

```bash
cd RPG-Game
```

3. Run the game:

```bash
python3 main.py
```

## Concepts Practiced

This project helped me practice and apply several Python programming concepts:

- Creating classes and objects
- Constructors (`__init__`)
- Encapsulation and private attributes
- Properties and getters
- Methods and object behavior
- Input validation and `ValueError`
- Loops and conditional statements
- Importing classes between Python files
- Random number generation

## Future Improvements

- Add different enemy types and boss battles.
- Implement an attack system for the player.
- Create an inventory system with healing items.
- Add player choices that affect the story.
- Introduce different difficulty levels.

## Author

Kyne Pinckney

Computer Science Student | Georgia State University
