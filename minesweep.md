garbage

---
|1|
---

 ___
| 1 |
|___|

 -
|1|
 -

  1 2 3 4
1 * * * *
2 * * * *
3 * * * *
4 * * * *

  A B C D
A * * * *
B * * * *
C * * * *
D * * * *

AA

  A B C D
A 1 M 2 M
B 1 1 2 2
C 2 2 1 M
D M 2 1 1

[[1,M,2,M],[1,1,2,2],[2,2,1,M],[M,2,1,1]]

pseudocode

backend:
-----
make an empty 4x4 array - can eventually just choose size 

populate randomly with 4 mines 

for loop in the 3x3 square surrounding each square, if there is 
mine in that square, update the current square w +1 UNLESS that square is mine

userside:
----------
soo you start with a tally of how many flags you have - 4

a 4x4 array that has asterisks instead of mines or numbers

a user can choose ones of asterisks and reveal it, it then populates with
whatever is in the backend.
    if bomb, game ends
    if 1 or 2 reveal that

if user inputs F after the initial two letters, it is marked with a flag
    if you guess where all the mines are, you win the game
