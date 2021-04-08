# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

word_list=load_words()

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word

def get_word_score(word,n):
    word_sum=0
    copy_word=word.lower()
    for char in copy_word:
        if char in SCRABBLE_LETTER_VALUES:
            word_sum = SCRABBLE_LETTER_VALUES[char]+word_sum
    length_sum= ((7*len(word))-(3*(n-len(word))))
    if length_sum<1:
        length_sum=1
    else:
        length_sum=length_sum
    sum = length_sum*word_sum
    return sum

def display_hand(hand):

    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    x = '*'
    hand[x] = hand.get(x, 0) + 1
    
    return hand
#
# Problem #2: Update a hand by removing letters
#
hand=deal_hand(HAND_SIZE)

def update_hand(hand, word):
    copy_hand=hand.copy()
    for char in word.lower():
        if copy_hand[char]>0:
            copy_hand[char] -= 1
    return copy_hand

def is_valid_word(word, hand, word_list):

    def check_wildcard(word):
        index_list=[]
        for vowel in VOWELS:
            find_wildcard=word.find('*')
            new_word=word[0:find_wildcard]+vowel
            if find_wildcard<len(word)-1:
                new_word=new_word+word[find_wildcard+1:]
            index_list.append(new_word.lower())
        return index_list

    if '*' in word:
        wildcard=check_wildcard(word)
        no_word_in_dict=True

        for w in wildcard:
            if w.lower() in word_list:
                no_word_in_dict=False
        if no_word_in_dict:
            return False
    elif word.lower() not in word_list:
        return False

    hand_copy = hand.copy()
    for char in word.lower():
        if char not in hand_copy.keys():
            return False
        else:
            hand_copy[char] -= 1
            if hand_copy[char] < 0:
                return False

    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    handsum=sum(hand.values())
    return handsum

def play_hand(hand, word_list):
    total_score=0
    calc_hand=calculate_handlen(hand)
    print("current hand: ", end='')
    display_hand(hand)
    while calculate_handlen(hand)>0:
        word = input("Enter word, or !! to indicate that you are finished: ")
        if word == '!!':
            break
        else:
            valid_word = is_valid_word(word, hand, word_list)
            if valid_word:
                get_score=get_word_score(word,calc_hand)
                total_score +=get_score
                print('"{}" earned {} points. Total: {} points'.format(word, get_score, total_score ))

            if not valid_word:
                print("That is not a valid word. Please choose another word.")
            hand=update_hand(hand,word)
            print("current hand: ", end='')
            display_hand(hand)

    if calculate_handlen(hand)<=0:
        print("Ran out of letters. Total score: ",total_score)
    return total_score





def substitute_hand(hand, letter):
    hand_copy=hand.copy()

    if letter not in hand_copy.keys() or not letter.isalpha():
        print("letter not in hand")
        return hand_copy

    if letter in VOWELS:
        list_to_get_from = VOWELS
    else:
        list_to_get_from = CONSONANTS

    while True:
        new_letter = random.choice(list_to_get_from)
        if new_letter not in hand.keys():
            hand_copy[new_letter] = hand_copy.pop(letter)
            break

    return hand_copy
       
    
def play_game(word_list):
    total_score=0
    hand_count=int(input("Enter total number of hands: "))
    replay='no'
    for x in range(hand_count):
        if x>0:
            replay=input("Would you like to replay this hand? ")
        if replay=='no':
            hand=deal_hand(HAND_SIZE)
            print("current hand: ", end='')
            display_hand(hand)
        sub_letter = input("Would you like to substitute a letter? ")
        if sub_letter=='yes':
            letter= input("Input which letter you would like to substitute: ")
            hand=substitute_hand(hand,letter)

        total_score +=play_hand(hand,word_list)
        print("------------")
        print('Total score over all hands: {}'.format(total_score))




#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
