
# welcomes the user to the game
print('Welcome to hangman!')
import random
again = True

# loop if user wants to play again
while again == True:

    # list of words
    word_list = ['unicorn', 'cake', 'drive', 'square', 'mississippi', 'squirrels', 'grandchildren', 'flustering', 'incompatibility', 'backfire']
    
    # choose random word
    word = random.choice(word_list)

    # define values, arrays, integers, etc.
    letters = len(word)
    letter_word = []
    C_guess = []
    W_guess = []
    gaps = []
    correct = 0
    incorrect = 0
    guesses = 1
    a = False

    # make dict of the random word
    letter_dict = {}
    count = 0

    # fill dict with each letter of word as key 
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter].append(count)
        else:  
            letter_dict[letter] = [count]
        
        #fill list with _'s
        gaps.append('_')
        count = count + 1

    # Display how many letters are in the random word
    print("There are " + str(letters) + " letters in the word.")

    # loop until the user guesses the word or all of the letters
    while "_" in gaps and a == False:
        b = 0

        # user input
        guess = input("What is your guess? ")

        # if user guesses exact word then end loop
        if guess == word: 
            a = True
        else:

            # ensures user doesnt submit multiple of the same letter
            if guess in C_guess or guess in W_guess:
                print("you already guessed " + guess + "! Try again!")
            
            # make sure the user only guesses 1 letter at a time
            elif len(guess) != 1:
                print("Please only guess 1 letter at a time!")

            else:

                # if they correctly guessed a letter
                if guess in word:
                    print("Correct, " + guess + " is a letter in the word!")

                    # add their guess to a list of the rest of their correct guesses
                    C_guess.append(guess)
                    print("You have correctly guessed the letters: " + str(C_guess))
                    
                    # fills the gap with the letters and shows which ones are missing
                    indexes_guess = letter_dict[guess]
                    for index_guess in indexes_guess:
                        gaps[index_guess] = guess

                    # prints the _ formatted correctly
                    print(*gaps)
                    correct = correct + 1

                # If their guess was incorrect
                else: 
                    print("Incorrect " + guess + " is not a letter in the word!")
                    W_guess.append(guess)
                    print("You have incorrectly guessed the letters: " + str(W_guess))
                    incorrect = incorrect + 1
                
                # shows how many guesses the person has made accounting for only 1 guess 
                if guesses == 1:
                    print("You have made in total " + str(int(len(C_guess)) + int(len(W_guess))) +  " guess, " + str(len(C_guess)) + " of which are correct guesses and " + str(len(W_guess)) + " of which are incorrect!")
                else: 
                    print("You have made in total " + str(int(len(C_guess)) + int(len(W_guess))) +  " guesses, " + str(len(C_guess)) + " of which are correct guesses and " + str(len(W_guess)) + " of which are incorrect!")
                guesses += 1

    # When the word is guessed correctly
    print("Thats right! The word was " + word)

    # how many total guesses did it take
    print("It took you " + str(guesses) + " guesses to guess the word!")

    # ask the user if they want to play again
    redo = input("Do you want to play again? yes or no? ")
    if redo == 'yes':
        again = True
    else:
        print("Thank you for playing!")
        again = False