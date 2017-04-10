# A simple cellular automaton in Python

## How do rules work?
A rule determines how cells evolve over time. Rules are expressed as integers ranging between 0 - 255 (8 bits). The evolution of the cells is easier to understand by looking at the binary representation.

## Example:

Let's look at **rule 30**. In binary this is:
```
30 = 0b00011110
```
Now each bit corresonds to a state for three adjacent cells and the value of that bit corresponds to what the next state in the evolution of the center cell is.

```
Bit         7   6   5   4   3   2   1   0
Previous: 111 110 101 100 011 010 001 000
Rule 30 : [0] [0] [0] [1] [1] [1] [1] [0]
```
So according to rule 30, 4 possible combinations of cells lead to a 1 in the center cell.

