# Asteroids Game (Python and Pygame)

A clone of the classic arcade game Asteroids, built with Python and Pygame. Fly a spaceship, shoot incoming asteroids, and avoid collisions.

This is a guided project from the [Build Asteroids using Python and Pygame](https://www.boot.dev/courses/build-asteroids-python) course on Boot.dev.

## Features

- **Player ship** that rotates, moves, and shoots
- **Asteroids** that spawn at the edges of the screen and drift across it
- **Splitting asteroids:** shooting a large asteroid breaks it into smaller ones
- **Collision detection** between the ship, shots, and asteroids
- **Game over** when the ship hits an asteroid
- **Frame-rate independent movement** using delta time

## Tech stack

- Python
- Pygame
- Object-oriented programming (classes and inheritance)

## Getting started

### Prerequisites

- Python 3
- Pygame

### Installation

```bash
git clone https://github.com/SumitRatnaTamrakar/Asteroids-game-project.git
cd Asteroids-game-project
pip install pygame
```

### Run the game

```bash
python main.py
```

<!-- VERIFY: if you use uv or a requirements file, update the install and run commands -->

## Controls

| Key | Action |
| --- | --- |
| W / S | Move forward / backward |
| A / D | Rotate left / right |
| Space | Shoot |

<!-- VERIFY: confirm these controls match your code -->

## How it works

- A base class holds the position, velocity, and radius shared by every game object.
- The player, asteroids, and shots all inherit from it and implement their own drawing and update logic.
- Pygame sprite groups keep updatable and drawable objects organized.
- The main game loop handles input, updates every object, checks collisions, and redraws the screen each frame.
- An asteroid spawner adds new asteroids at the edges of the screen at regular intervals.
- When a shot hits an asteroid, the asteroid splits into two smaller ones until it is too small to split.

## Project structure

```
.
├── main.py              # Game loop
├── player.py            # Player ship
├── asteroid.py          # Asteroid behavior and splitting
├── asteroidfield.py     # Spawns new asteroids
├── shot.py              # Bullets
├── circleshape.py       # Base class for game objects
└── constants.py         # Screen size, speeds, and other settings
```

<!-- VERIFY: adjust file names to match your repository -->

## What I learned

- Building a game loop and handling keyboard input in Pygame
- Using classes and inheritance to model game objects
- Vector math for movement and rotation
- Circle-based collision detection
- Managing game state with sprite groups

## Acknowledgments

Built by following the guided project on [Boot.dev](https://www.boot.dev/courses/build-asteroids-python).

## Author

**Sumit Ratna Tamrakar**, Computer Engineer focused on AI and machine learning.
[LinkedIn](https://www.linkedin.com/in/sumit-tamrakar) | [GitHub](https://github.com/SumitRatnaTamrakar)
