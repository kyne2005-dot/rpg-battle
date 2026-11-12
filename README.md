RPG Battle Game

A simple text-based RPG built with Python. The player controls a hero who travels through a series of story events, fights enemies, takes damage, and finds healing along the way. The goal is to survive every encounter by managing your health.

Features
Hero class: Uses object-oriented programming to manage the hero's name, current health, and maximum health.
Health management: The hero can take damage and restore health during the game.
Randomized events: Damage and healing amounts are generated with Python's random module, so every run plays out differently.
Validation: Raises a ValueError for invalid values, and keeps health between 0 and the maximum.
Story progression: A loop moves the hero through a sequence of story events.
Game over: The game ends if the hero's health reaches zero.
Project Structure
rpg-battle/
├── Hero.py      # Hero class (health, damage, healing, validation)
├── main.py      # Main game script: story events and game loop
└── README.md
How to Run

Requires Python 3. No external libraries are needed.

git clone https://github.com/kyne2005-dot/rpg-battle.git
cd rpg-battle
python3 main.py
Sample Output
The Hero has 200/200 health left

You are traveling down the road when you are suddenly attacked by an enemy.
During the battle you take 77 damage. You need healing before the next battle.
The Hero has 123/200 health left

You are alive

After you defeat the enemy, you wander and find a chest with healing supplies.
You find healing and recover 20 health. Now you are ready for battle.
The Hero has 143/200 health left

You are alive
Concepts Practiced
Classes, objects, and constructors (__init__)
Encapsulation with private attributes and @property
Input validation with ValueError
Loops and conditionals
Splitting code across modules and importing a class
Future Improvements
Add multiple enemy types with different stats
Add a player attack system so the hero can fight back
Add an inventory with healing items
Add player choices that change the story
Add difficulty levels
Author

Kyne Pinckney, Computer Science student at Georgia State University
