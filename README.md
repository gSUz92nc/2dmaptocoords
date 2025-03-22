# 2D Map to Coordinates

A simple tool that allows you to click on a 2D image map and get the corresponding coordinates in both pixel space and game-space.

## Description

This utility helps you convert positions on a 2D map image into game coordinates. It's particularly useful for:
- Game development - mapping image locations to game world positions
- Level design - placing objects in a game world based on a map
- Finding exact coordinates on maps for navigation or reference

## Features

- Load any image as a map reference
- Click anywhere on the image to get coordinates
- Displays both pixel coordinates and scaled game map coordinates
- Simple and easy to use interface

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/2dmaptocoords.git
cd 2dmaptocoords
```

2. Install required dependencies:
   
   Either install Pygame directly:
```
pip install pygame
```

   Or use the requirements.txt file:
```
pip install -r requirements.txt
```

## Usage

1. Replace `image.png` with your own map image or use the provided sample.
2. Run the script:
```
python click_coordinates.py
```
3. Click anywhere on the map to see the coordinates in the console.
4. Press the window's close button to exit.

## Configuration

You can adjust the game map dimensions by modifying these variables in the script:
```python
GAME_MAP_WIDTH = 15000  # Width of your game map units
GAME_MAP_HEIGHT = 15000  # Height of your game map units
```

Set these values to match the coordinate system of your game or application.

## How It Works

The tool performs a simple linear scaling from pixel coordinates to game coordinates:
- Pixel coordinates range from (0,0) at the top-left to (width,height) at the bottom-right
- Game coordinates are scaled proportionally based on the defined GAME_MAP dimensions