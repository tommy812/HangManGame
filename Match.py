import random 
from WordGuess import *
from dataclasses import dataclass,field

@dataclass
class Match:
    difficulty: int 
    playAgain: bool = field(default = True)
    wordLength: int = random.randint(4,12)
    lifes: int = field(default= 0)
    words: object = WordGuess(wordLength)  
    

    def __post_init__(self):
        self.lifes = self.wordLength*2
  
   
    def start(self):
        while not (self.words.isGuessed() == True):
            if self.getLifes() > 0:
                self.printLifes()
                self.words.game(self.difficulty)
                self.lifes -= 1
                
                if self.words.isGuessed():
                    print(f"Congratulations!!\nThe word was: {self.words.dictionary.tempWord}.")
                    break
            else:
                print(f"Sorry you run out of guesses.\nThe word was: {self.words.dictionary.tempWord}.")
                break
    
        choice = input("play again? 1 = Restart / 2 = End")
        if choice == "1":
            return False
        else:
            return True



    def getLifes(self):
        return self.lifes

    def printLifes(self):
        print(f"\nYou have {self.lifes} guesses left.")

    