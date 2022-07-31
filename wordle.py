import json #To parse the json returned from word_of_the_day library
import enchant #To check whether a given word is in the English Dictionary
from random_word import RandomWords #To get word of the day
from colorama import Fore, Style #To implement colored print statements

r = RandomWords()
d = enchant.Dict("en_US")

word = r.word_of_the_day()
word = json.loads(word)['word']
print('There are '+str(len(word))+' letters in the word you need to guess. You have 6 attempts to guess the word of the day') #

guess = ''
attempts = 0
while guess != word and attempts < 6:
    guess = input('').lower()
    if d.check(guess): #Ensuring an English word as input
        attempts = attempts + 1
        if len(word) != len(guess): #Ensuring a guess of equal length as the word of the day
            print(Fore.RED+"Length of your guess does not match the length of the word of the day"+Style.RESET_ALL)
        else:
            for i in range(len(word)):
                if guess[i] == word[i]:
                    print(Fore.GREEN+guess[i]+Style.RESET_ALL,end='')
                    continue
                else:
                    if guess[i] in word:
                        print(guess[i],end='')
                    else:
                        print(Fore.RED+guess[i]+Style.RESET_ALL,end='')
    else:
        print(Fore.RED+"Not an English word"+Style.RESET_ALL)            