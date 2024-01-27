# Advanced-Python-Scripting-Project

## Assumptions

* `data` directory contains many files and directories
* You are only interested in the games contained in this directory
* Each game is stored in a directory that contains the word `game`
* Each game directory contains a single `.go` file that must be compiled before it can be run

## Flow of the project

* Find all game directories from `/data`
* Create a new `games` directory
* Copy and remove the `game` suffix of all games into the `/games` directory
* Create a `.json` file with the info about the games
* Compile all of the game code
* Run all of the game code
