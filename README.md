# Conway's Game Of Life

The goal of this project is to recreate Conway's Game of Life using python with the help of pygame. The premise of this game follows simple survival rules of life as such:

1) Birth rule: An empty, or “dead,” cell with precisely three “live” neighbors (full cells) becomes live.

2) Death rule: A live cell with zero or one neighbors dies of isolation; a live cell with four or more neighbors dies of overcrowding.

3) Survival rule: A live cell with two or three neighbors remains alive.

## Set Up

### Create Virtual Enviroment

```
python -m venv env
source env/bin/activate
```

### Installation

```
pip install -r requirements.txt
```

## Usage

```
python src/main.py
```

### Keys

```
g = Generate Random Tile Set
space = Play/Pause Conway's Game
c = Clear Grid
q = Quit
```