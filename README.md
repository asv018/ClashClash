ClashClash
A terminal-based version of Clash Of Clans using Python and OOPs principles. Here's a glimpse of the gameplay:



The game starts with the user selecting which hero he/she wants to use (King or Queen)

Controls:

Spawning at spawn point 1:

z - Spawns a barbarian
1 - Spawns the hero
v - Spawns an archer
4 - Spawns a balloon

Spawning at spawn point 2:

x - Spawns a barbarian
2 - Spawns the hero
b - Spawns an archer
5 - Spawns a balloon

Spawning at spawn point 3:

c - Spawns a barbarian
3 - Spawns the hero
n - Spawns an archer
6 - Spawns a balloon

Controlling the movement of Hero:

w - Move one cell up
a - Move one cell left
s - Move one cell down
d - Move one cell right

Spells:

r - Activate the rage spell, which doubles the speed and damage done by the troops
h - Activate the heal spell, which can heal a troop upto 1.5 times its current health.

Attack using King:

i - Attack one cell up
j - Attack one cell left
k - Attack one cell down
l - Attack one cell right

Attack using Queen:

space: Normal attack
m: Archer Queen’s eagle arrow attack

OOPs concepts used:
Inheritance:
Generic classes for game objects and all the objects inheriting these classes. Basic character and building classes are inherited by all other classes specific to different types of game objects.

Polymorphism:
Multiple functions with the same name but a varying number of arguments used.

Encapsulation:
Class and object-based approach for all the functionality implemented.

Abstraction:
Intuitive functionality like move(), attack(), etc, showing away inner details from the end user.

Setup
colorama is required for the app to run. To install colorama,
pip3 install colorama
To run the game,
python3 game.py
To view replays,
python3 replay.py
