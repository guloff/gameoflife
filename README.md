# Conway's Game of Life Simulation

This is a Python implementation of **Conway's Game of Life** using the PyGame library. The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game consists of a grid of cells that evolve over time according to simple rules.

## Features

- The grid size is 1600x900 pixels with each cell measuring 20x20 pixels.
- The simulation follows the classic Game of Life rules:
  - Any live cell with fewer than two live neighbors dies (underpopulation).
  - Any live cell with two or three live neighbors lives on to the next generation.
  - Any live cell with more than three live neighbors dies (overpopulation).
  - Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
- You can manually activate or deactivate cells by clicking with the mouse:
  - Left-click to activate a cell.
  - Right-click to deactivate a cell.
- The simulation can be paused and resumed by pressing the `SPACE` key.
- Press `q` to quit the simulation.

## Installation

### Prerequisites
Make sure you have Python 3 installed on your system. You will also need to install the following libraries:

- `pygame`
- `numpy`

You can install the necessary dependencies by running:

```bash
pip install pygame numpy
```

### Virtual Environment (Optional but Recommended)
To avoid conflicts with other projects, it's a good idea to use a virtual environment:

```bash
python3 -m venv life_env
source life_env/bin/activate  # On Windows use: life_env\Scripts\activate
pip install pygame numpy
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/guloff/gameoflife.git
cd gameoflife
```

2. Run the game:

```bash
python3 game_of_life.py
```

## Controls

- `SPACE`: Pause/Resume the simulation.
- `Left-click`: Activate a cell.
- `Right-click`: Deactivate a cell.
- `q`: Quit the simulation.

## License

This project is licensed under the MIT License.
