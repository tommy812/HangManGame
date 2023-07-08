from dataclasses import dataclass, field
from Dictionary import *

@dataclass
class WordGuess:
    length: int 
    usedLetters: list[int] = field(default_factory= list)
    dashedWord: list[str] = field(default_factory= list)
    guessed: bool = False
    letterGuessed: bool = False


    def __post_init__(self):
        self.dictionary = Dictionary(self.length) 
        self.initDWord()

    def isGuessed(self):
        return self.guessed


    def game(self,difficulty):
        #self.__printGuessLeft()
        #match.printGuessLeft()
        self.__printUsedLetters()
        self.printDWord()
        self.__getGuess(difficulty)
       
        
    def __printUsedLetters(self):
        print("Used Letters: ")
        print(self.usedLetters)

    def initDWord(self):
        self.dashedWord = []
        for i in range(self.length):
            self.dashedWord.append("_")

    #print dashed word 
    def printDWord(self):
        print(" ".join(self.dashedWord))

    #add guessed letter to hashed word 
    def __set_dWord(self,letter,position):
        
        for positions in position:
            self.dashedWord[positions] = letter
        #self.__printDWord()
        
    def __getGuess(self,difficulty):
        validChar = False
        while not (validChar ==True):
            guess = input("Guess a letter:\n")
            if guess in self.usedLetters:
                print("You already used this letter, Try again:")

            elif len(guess) == 1 and guess.isalpha():

                self.usedLetters.append(guess)
                
 
                #TODO check if the letter is in the word
                if difficulty == 1: 
                    self.letterGuessed = self.dictionary.check_Letter_easy(guess)
                else:
                    self.letterGuessed = self.dictionary.check_Letter_hard(guess)
                
                print(f"letter is {self.letterGuessed}")
                if self.letterGuessed:
                    self.__set_dWord(guess ,self.dictionary.pos)
                
                if "_" not in self.dashedWord:
                    self.guessed = True
                validChar = True
            else:
                print("Input not valid, Try again:")
            