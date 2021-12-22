# Generate a random English word
import random # Python's built-in module for all things random
f = open("words_alpha.txt","r") # open and read from the text file
word_list = f.readlines() # read the file line by line into a list
raw_word = random.choice(word_list) # return a random element from word_list
word_list.remove(raw_word) #remove the chosen word from the list to ensure it is not used again
word = raw_word.rstrip("\n") # remove "\n" characters from the right side of the word (aka from the end)
f.close() # close the text file

guess_count = 0
gameplay_count = 0
win_count = 0
loss_count = gameplay_count - win_count
onscreen = list("_" * len(word))
print(onscreen)

def play_again():
    yes_or_no = str(input("Play again? Type 'yes' or 'no': ")).lower().strip() # turn the input into a lowercase string
    if yes_or_no.isalpha() == True and yes_or_no == "yes":
        return True
    elif yes_or_no.isalpha() == True and yes_or_no == "no":
        return False
    else:
        print("Error: you did not follow directions.")
        return False

while guess_count <= 7:
    letter_list = list(word) # turn the letters into a list
    guess = str(input("Enter a letter or word: ")).lower().strip() # turn the input into a lowercase string
    if guess == word: # if the word is guessed
        print("Correct. You win.")
        gameplay_count += 1
        win_count += 1
        print("Won  {w}/{t} games \nLost {l}/{t} games".format(w=win_count,t=gameplay_count,l=loss_count))
        if play_again():
            guess_count = 0
            # function to get and display new random word
        else:
            guess_count = 8
    elif guess.isalpha() == True and guess in letter_list: # guess is a correct letter
        for i in range(0,len(word)): # for the entire length of the word
            if guess == word[i]: # guessed letter is in the correct index
                onscreen[i] = guess # displays correctly guessed letters
                if onscreen == letter_list: # if the entire word is guessed via letters
                    print("Correct. You win.")
                    gameplay_count += 1
                    win_count += 1
                    print("Won  {w}/{t} games \nLost {l}/{t} games".format(w=win_count,t=gameplay_count,l=loss_count))
                    if play_again():
                        guess_count = 0
                        # function to get and display new random word
                    else:
                        guess_count = 8
        print(onscreen)
    elif guess.isalpha() == True and (guess not in letter_list or guess != word): # guess is an incorrect letter or an incorrect word
        print("Incorrect. That was guess {guess_count_display}/7. \nYou are responsible for keeping track of which letters you've already guessed.".format(guess_count_display=guess_count+1))
        guess_count += 1
        if guess_count == 7:
            print("You lose. The word was: {a}".format(a=word))
            gameplay_count += 1
            loss_count += 1
            print("Won  {w}/{t} games \nLost {l}/{t} games".format(w=win_count,t=gameplay_count,l=loss_count))
            if play_again():
                guess_count = 0
                # function to get and display new random word
            else:
                guess_count = 8
    elif guess.isalpha() == False: # guess is a special character or number or letters with spaces in between them
        print("Error: you did not follow directions. Try again.")