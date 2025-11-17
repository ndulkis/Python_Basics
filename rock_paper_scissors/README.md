#  Rock, Paper, Scissors – Console Game

A simple program that simulates a game of **Rock, Paper, Scissors** between the player and the computer. The player enters their choice (`r`, `p`, or `s`), the computer randomly selects its choice, and the program determines the winner.

---

##  Features

* Player input using `r`, `p`, or `s`
* Random computer selection
* Emojis displayed for moves:

  * 🪨 Rock
  * 📄 Paper
  * ✂️ Scissors
* Automatic winner determination
* Input validation for invalid entries

---

##  Game Rules

| Player      | Computer    | Result        |
| ----------- | ----------- | ------------- |
| Rock 🪨     | Scissors ✂️ | Player Wins   |
| Rock 🪨     | Paper 📄    | Computer Wins |
| Paper 📄    | Rock 🪨     | Player Wins   |
| Paper 📄    | Scissors ✂️ | Computer Wins |
| Scissors ✂️ | Paper 📄    | Player Wins   |
| Scissors ✂️ | Rock 🪨     | Computer Wins |
| Same choice | Same choice | Tie           |

---

##  How to Play

1. Run the program.
2. Enter one of the following when prompted:

   * `r` → Rock 🪨
   * `p` → Paper 📄
   * `s` → Scissors ✂️
3. The computer will randomly choose its move.
4. Both choices are displayed.
5. The winner is announced.

## Running the Program

```bash
python main.py
```

