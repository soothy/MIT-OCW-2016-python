import random
import string

WORDLIST_FILENAME = "../../../../Desktop/ps2/ps2/words.txt"
myList = []
strl = " "
guesses = 6
checklist=[]

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):

    random.choice(wordlist)
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """

    return random.choice(wordlist)

secret_word=choose_word(wordlist)
for i in range(len(secret_word)):
    myList.append('_')
print(secret_word)

def is_word_guessed(secret_word, letters_guessed):

    set_letters_guessed = set(letters_guessed)
    for word in secret_word:
        intersection = set_letters_guessed.intersection(secret_word)
        if intersection ==  set_letters_guessed:
            return False
        else:
            return True

def get_guessed_word(secret_word, letters_guessed):
    for char in secret_word:
        if char in letters_guessed:
            for n in range(len(secret_word)):
                if secret_word[n] == letters_guessed:
                    myList[n] = letters_guessed
    guess_word = strl.join(myList)
    guessed_word = guess_word.replace(" ","")

    return guessed_word

def boolean_guess(secret_word, letters_guessed):

    for char in letters_guessed:
        if char in secret_word:
            return True
        else:
            return False

s = list(string.ascii_lowercase)


def get_available_letters(s,letters_guessed):
    for char in letters_guessed:
        if char in s:
            s.remove(char)

    return s
def boolean_available_letters(s,letters_guessed):
    for char in letters_guessed:
        if char not in s:
            return True
        else:
            return False

def check_vowel(letters_guessed):
    if letters_guessed =='a' or letters_guessed=='e' or letters_guessed =='i' or letters_guessed =='o' or letters_guessed=='u':
        return True
    else:
        return False

tries=3
print("Welcome to hangman!")
print("I am thinking of a word that is ",len(secret_word),"letters long")
print("You have",guesses, "guesses left")
print("Available letters: ",strl.join(s))
while guesses !=0:
    while True:
        letters_guessed = input("input letter: ")
        if (letters_guessed.isalpha() == 0 or len(letters_guessed) != 1 or boolean_available_letters(s,letters_guessed)==1):
            tries=tries-1
            print("You have ",tries,"remaining")
            if tries == 0:
                if guesses !=1:
                    guesses -= 1
                    print("You have ",guesses,"guesses left")
                    tries =3
                else:
                    exit()
            continue
        else:
            break
    is_guessed=is_word_guessed(secret_word,letters_guessed)
    boolean=boolean_guess(secret_word,letters_guessed)
    getguessedword=get_guessed_word(secret_word,letters_guessed)
    if (boolean == False and check_vowel(letters_guessed)==True):
        guesses-= 2
        print(get_available_letters(s,letters_guessed))
        print ("you have ",guesses,"guesses remaining")
    elif(boolean==False):
        guesses-=1
        print(get_available_letters(s, letters_guessed))
        print("you have ", guesses, "guesses remaining")
    else:
        print(get_available_letters(s, letters_guessed))
        print(getguessedword)
    if getguessedword == secret_word:
        print("You have completed hangman!")
        break

lenlist=[word for word in wordlist if len(word)==len(secret_word)]

def match_with_gaps(getguessedword, other_word):

    letters_guessed = []

    for i in range(len(getguessedword)):
        current_letter = getguessedword[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            if current_letter != other_letter:
                return False
        else:
            if current_letter == '_' and other_letter in letters_guessed:
                return False

    return True



def show_possible_matches(getguessedword):
        matchlist = []
        for word in lenlist:
            if match_with_gaps(getguessedword, word) == True:
                matchlist.append(word)
        if len(matchlist) == 0:
            print("no matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
