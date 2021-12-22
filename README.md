# word-guessing-game

A random word is chosen from a full dictionary list. A player starts with 7 guesses.
On each turn, a player can guess a letter or guess the full word. If the player guesses a letter that is in the word, the computer will show the player the position of each instance of that letter.

For example: Take the word "Mississippi" If the player chooses "i", the computer will print "_ i _ _ i _ _ i _ _ i " If the player then chooses, "o", the player will lose a 1 guess and now has 6 guesses.

When the player has 0 guesses, the game is over and the player has lost. If the player guesses the word correctly, the game is over and the player has won. If the player guesses the word incorrectly and the total guesses left is greater then 2, they lose 1 guess. If they guess the word incorrectly and the total guesses they have left is 1, they lose the game.

Ask the user if the player would like to play again. Keep a running total of wins and losses and ensure no word from Part 3 is ever picked twice for one session of the game.
