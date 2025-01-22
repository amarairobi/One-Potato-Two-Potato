# One Potato, Two Potato Game

This project simulates a counting-out elimination game where players are eliminated in a circular fashion based on a step count. The game continues until only one player remains.

## Requirements
- Python 3.x
- Tkinter

## How It Works
-- Players are numbered from `0` to `n-1`.

-- Starting at the first players (`0`), the counter moves `k` steps around the group.

-- The player where the count ends is eliminated.

-- The next round starts with the player immediately after the eliminated one.

-- The process repeats until one player is left.

### Example

Given:
- `n = 11` (11 players numbered 0 to 10)
- `k = 8` (8 steps per round)

-- The game starts at player `0`. After counting 8 steps, player `7` is eliminated.

-- The next round starts with player `8`. Counting 8 steps eliminates player `4`.

-- Continue until there's one player left.

**Output:**  
The function returns the number of the last remaining player.

---

## How to Run
```bash
git clone https://github.com/amarairobi/one-potato-two-potato.git
cd one-potato-two-potato
python potato_game.py




