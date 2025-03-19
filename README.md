# Defeat the Evil Feibang Lord

A simple turn-based battle game where players choose a character class and fight against the powerful Feibang Lord. The game features different character classes, each with unique abilities.

## Features
- **Character Selection:** Choose from 4 unique character classes:
  - **Grunter** (Warrior)
  - **Mofa** (Mage)
  - **Geki** (Archer)
  - **Medic** (Support)
- **Turn-Based Combat:** Players can attack, use special abilities, heal, or view stats.
- **Enemy AI:** The Feibang Lord can attack, regenerate, and use special abilities.
- **Dynamic Abilities:** Each class has distinct abilities that impact battle outcomes.

## How to Play
1. Run the game using Python:
   ```sh
   python main.py
   ```
2. Choose your character class by entering the corresponding number.
3. Enter a name for your character.
4. Battle against the Feibang Lord by selecting actions each turn.
5. Defeat the enemy before your health reaches zero!

## Controls
During battle, you will be prompted to choose an action:
- `1` - **Attack**: Deal normal damage to the enemy.
- `2` - **Use Special Ability**: Perform a unique class-based ability.
- `3` - **Heal**: Recover some health.
- `4` - **View Stats**: Check your current health and attack power.

## Installation
Ensure you have Python installed (version 3.x recommended). Clone this repository and navigate to the project directory:
```sh
 git clone <repository-url>
 cd battle-game
```

## Project Structure
```
│── classes.py       # Contains all character class definitions
│── main.py          # Runs the game loop
│── README.md        # Game instructions and details
```

## Future Improvements
- Add more enemy types with different abilities.
- Implement multiple battles and character progression.
- Add an inventory system with potions and weapons.
