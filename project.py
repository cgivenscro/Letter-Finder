import os
from os import system
system("clear")

import random

words = ['ignoramus', 'nonplussed', 'quirky', 'scatterbrain', 'sesquipedalian', 'lackadaisical', 'gadzooks', 'cryptozoology', 'antimacassar', 'frangipani', 'hullabaloo', 'windbag', 'ziggurat', 'wallflower', 'supercilious', 'splendiferous', 'bamboozle', 'cornucopia', 'demitasse', 'doppelganger', 'ersatz', 'festooned', 'gizmo', 'heyday', 'interrobang', 'jalopy', 'juggernaut', 'lummox', 'mnemonic', 'razzmatazz']

hint = ['Fancy word for stupid', 'Surprised and confused so much that they are unsure how to react', 'Characterized by peculiar or unexpected traits', 'Person who tends to be disorganized and lacking in concentration.', 'Characterized by long words', 'Lacking enthusiasm and determination or carelessly lazy', 'An exclamation of surprise or annoyance', 'The search for and study of animals whose existence or survival is disputed or unsubstantiated', 'a piece of cloth put over the back of a chair to protect it from grease and dirt or as an ornament', 'a tropical American tree or shrub', 'A commotion', 'a person who talks at length but says little of value', 'a rectangular stepped tower', 'a person who has no one to dance with or who feels shy, awkward, excluded at a party or a flower', 'behaving or looking as though one thinks one is superior to others', 'splendid', 'fool or cheat', "an ornamental container shaped like a goat's horn", 'a small coffee cup', 'an apparition or double of a living person.', 'not real or genuine', 'a place with ribbons, garlands, or other decorations', 'a gadget', "the period of a person's or thing's greatest success, popularity, or vigor", 'a non-standard punctuation mark indicating a question expressed in an exclamatory manner', 'an old car in a dilapidated condition', 'a huge, powerful, and overwhelming force or institution', 'a clumsy, stupid person', 'aiding or designed to aid the memory', 'another term for razzle-dazzle']

dash = []

l = ['Try again!', 'Take another stab!', 'Give it one more try!', 'Keep trying!', 'One more time!']
lose = random.choice(l)
w = ['Congratulations!', 'Nice Job!', 'Good Work!', 'Fantastic!', 'Well Done!']
win = random.choice(w)


randWord = random.choice(words)
chances = len(randWord) + 3




word = [*randWord]


for num in randWord:
    dash.append('-')

h = words.index(randWord)
print('Hint - ' + hint[h])

print(' '.join(dash))
# print(word)
# print(chances)


x = 1
lo = chances - 1

print('You have ' + str(lo) + ' chances left')

while x < chances:
    x = x + 1
    lo -= 1
    if '-' in dash:
        letter = input('Please type a letter: ')
        if letter in word:
            for num in range(len(word)):
                system('clear')
                if word[num] == letter:
                    dash[num] = letter
            print('Hint - ' + hint[h])
            print('The letter ' + letter + ' was in the word!')
            print(' '.join(dash))
            print('You have ' + str(lo) + ' chances left')
        else:
            system('clear')
            print('Hint - ' + hint[h])
            print('The letter '+letter+' was not in the word.')
            print(' '.join(dash))
            print('You have ' + str(lo) + ' chances left')
    else:
        break

print('The word was ' + randWord)
if x == chances and '-' in dash:
    print('You Lose.')
    print(''.join(lose))
else:
    print('You Win!')
    print(''.join(win))