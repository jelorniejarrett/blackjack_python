# Python Blackjack (Command Line Game)

A simple **command-line Blackjack game written in Python**.
This project simulates a basic version of the Blackjack card game where a player competes against a dealer.

The program demonstrates fundamental programming concepts such as loops, functions, lists, and randomization.


## Features

* Standard Blackjack gameplay against a dealer
* Random card drawing from a generated deck
* Player options to **Hit** or **Stand**
* Dealer follows the rule of drawing until reaching **17**
* Automatic win/loss/tie detection
* Option to replay the game after each round


## How the Game Works

1. A deck of cards is generated.
2. Both the **player** and **dealer** receive two cards.
3. The player chooses to:

   * **Hit** – draw another card
   * **Stand** – end their turn
4. If the player exceeds **21**, they **bust** and lose.
5. The dealer then draws cards until their total is **17 or higher**.
6. The final hand values are compared to determine the winner.


## Technologies Used

* Python 3
* random module (for card selection)


## How to Run the Program

###1. Install Python 3

###2. Clone the repository
https://github.com/jelorniejarrett/blackjack_python

###3. Run the program
python blackjack.py

---

## Example Gameplay

```
--- Blackjack ---

Your hand: [10, 7] Total: 17
Dealer shows: 6
Hit or Stand (h/s): h

Your hand: [10, 7, 3] Total: 20
Dealer shows: 6
Hit or Stand (h/s): s

Dealer hand: [6, 10, 5] Total: 21
Your hand: [10, 7, 3] Total: 20
Dealer wins.
```

---

## Concepts Demonstrated

This project demonstrates several core programming concepts:

* Functions
* Loops
* Conditional logic
* List manipulation
* Random number generation
* Game state management

---

## Future Improvements

Possible enhancements for this project include:

* Implementing full Blackjack rules for **Ace values (1 or 11)**
* Adding **betting mechanics**
* Creating a **graphical user interface**
* Supporting **multiple players**
* Improving input validation

---

## Author

**Jelornie Jarrett**

Computer Science / Programming Student
Project created as a learning exercise in Python programming.

---
