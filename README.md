# Pokémon Legends: Z-A Team Planner

![Tests](https://github.com/CrabGab/IS4010-Final-PokemonTeamAnalyzer/actions/workflows/tests.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)

This is a command-line tool to help you plan your Pokémon team for the upcoming game, Pokémon Legends: Z-A.

## Features

*   **Pokémon Availability:** Check which of your favorite Pokémon have been confirmed for the game.
*   **Team Defensive Analysis:** Analyze your team's defensive strengths and weaknesses.
*   **Boss Battle Simulations:** See how your team stacks up against the boss battles in the game.

## Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/CrabGab/IS4010-Final-PokemonTeamAnalyzer.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd IS4010-Final-PokemonTeamAnalyzer
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the team planner, run the `main.py` script with the names of the Pokémon you want to analyze.

```bash
python main.py <pokemon_name_1> <pokemon_name_2> ...
```

### Example

```bash
python main.py pikachu charizard blastoise
```