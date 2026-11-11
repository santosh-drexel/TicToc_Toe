# Tic-Tac-Toe Game (Python)

A command-line **human vs. computer Tic-Tac-Toe** project written in Python using object-oriented programming. The human plays **X** and the computer plays **O**. The board has nine numbered positions, and the computer currently selects moves randomly rather than using a strategy algorithm.

> **Project status:** This README describes the uploaded code as it currently exists. The files pass Python syntax compilation, but the game has known runtime/gameplay issues listed below. A full interactive game run has not been verified.

## Project files

| File | Purpose |
| --- | --- |
| `game.py` | Defines `TicTocToeGame`, runs the turn loop, announces results, and asks about replay. **This is the game entry point.** |
| `board1.py` | Defines `Board`, displays the board, places markers, checks rows/columns/diagonals for wins, detects ties, and resets the board. |
| `Player.py` | Defines `Player`, human/computer markers, input handling, and random computer move selection. |
| `move.py` | Defines `Move`, validates a position from 1–9, and converts it to a row and column. |

## Requirements

- Python 3.9 or newer (recommended)
- `numpy`
- `tabulate`

The game also uses Python's built-in `random` module, which does not need installation. **FastAPI and psycopg2 are not required for the game**; they are imported only by the unrelated `main.py`.

## Installation and running

1. Place `game.py`, `board1.py`, `Player.py`, and `move.py` in the **same directory**. Preserve the filenames and capitalization, especially on case-sensitive systems.
2. Open a terminal in that directory.
3. (Optional) Create and activate a virtual environment:

   **Windows PowerShell:**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install numpy tabulate
   ```
5. Start the console game:
   ```bash
   python game.py
   ```

In VS Code, open the project folder, select the Python interpreter, and run `game.py` in the integrated terminal.

## How to play

The game displays a numbered 3 × 3 reference grid:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

- The **human (X)** enters a number from **1 to 9** to select a square.
- The **computer (O)** chooses a square at random.
- The first player to make three matching markers in a row, column, or diagonal wins.
- If all nine squares are occupied without a winner, the round is a tie.
- At the end of a round, the game prompts for `x` to play again or `o` to quit. **Replay is not currently reliable; see Known issues.**

## Object-oriented design

| Class | Selected methods / responsibilities |
| --- | --- |
| `Move` | `is_valid()`, `get_row()`, `get_column()`; translates positions 1–9 into zero-based coordinates. |
| `Player` | `get_move()`, `get_human_move()`, `get_computer_move()`, `validate_move()`; distinguishes human and computer players. |
| `Board` | `submit_move()`, `print_board()`, `check_game_over()`, `check_is_tie()`, `reset_board()`; stores the 3 × 3 game state. |
| `TicTocToeGame` | `game_start()`, `start_new_round()`; coordinates gameplay and replay prompts. |

This separation demonstrates **classes, encapsulation, properties, object collaboration, input validation, and control flow**.

## Known issues in the uploaded version

1. **Occupied-square tracking is not shared correctly.** `Player` creates independent available-position lists, and `validate_move()` operates on a temporary set. Consequently, a square may be selected again, and `Board.submit_move()` can reject it without prompting for a valid replacement.
2. **Computer-win handling does not end the inner turn loop.** In `game.py`, the computer-win branch prints a message but has no `break`.
3. **Replay calls a nonexistent method.** Selecting `x` invokes `self.start()`, but `TicTocToeGame` defines no `start()` method, so this can raise `AttributeError`.
4. **Invalid input may raise errors.** The code converts input directly with `int(...)`, so nonnumeric entries can raise `ValueError`. Some invalid/occupied moves may also cause exceptions in `validate_move()`.
5. **A full game execution has not been tested.** Successful syntax compilation does not establish that gameplay is correct.

These are observations, **not code changes**. The uploaded Python files have been left untouched.

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `ModuleNotFoundError: No module named 'tabulate'` | Run `python -m pip install tabulate`. |
| `ModuleNotFoundError: No module named 'numpy'` | Run `python -m pip install numpy`. |
| `ModuleNotFoundError` for a project module | Run from the directory containing all four game files; check filename capitalization. |
| `ValueError` after entering a move | Enter a whole number between 1 and 9; input validation needs improvement. |
| Game crashes after choosing replay | See the `self.start()` issue above. |
| Occupied position or turn behavior seems incorrect | See the shared-position tracking issue above. |

## Technical Summary

> I built a command-line Tic-Tac-Toe game in Python using an object-oriented design. The `Move` class translates user choices into board coordinates, `Player` handles human and random computer moves, `Board` maintains game state and checks win/tie conditions, and `TicTocToeGame` coordinates the rounds. The project demonstrates class responsibilities and encapsulation. My next improvements are centralized legal-move validation, reliable game termination, and replay handling.

## Future improvements

- Keep a single source of truth for available squares in `Board`.
- Re-prompt for invalid or occupied positions without losing a turn unexpectedly.
- Stop immediately when either player wins or a tie is reached.
- Fix replay by resetting all round state and restarting the existing game loop.
- Add automated tests for horizontal, vertical, diagonal, tie, and invalid-move cases.
- Optionally implement a stronger computer opponent using minimax.

---
