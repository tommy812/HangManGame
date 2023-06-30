import random

class Match:
    def __init__(self,difficulty):
        self.difficulty = difficulty
        #get random world lenght when creating new match 
        self.wordLength = random.randint(4,12)
        self.__importDictionary()
        self.numberGuesses = 0
    

    def __importDictionary(self):
        my_file = open("Dictionary.txt", "r")
        data = my_file.read()
        self.dictionary = data.split("\n")

    def getWordLength(self):
        print("World Length is: "+ str(self.wordLength))
        print("\nGuesses available: "+str(self.wordLength*2))
        return self.wordLength 
    
    


class WordGuess:
    def __init__(self, length):
        self.length = length
        self.lifes = length*2
        self.usedLetters = []

    def game(self):
        self.__printGuessLeft()
        self.__printUsedLetters()
        self.__printDWord()
        self.__getGuess()
        

        
    def __printGuessLeft(self):
        print(f"You have {self.lifes} guesses left")

    def __printUsedLetters(self):
        print("Used Letters: ")
        print(self.usedLetters)


    #print dashed word 
    def __printDWord(self):
        self.dashedList = []
        for i in range(self.length):
            self.dashedList.append("_")

        #convert in list
        #self.dashedWord = list("")

        print(" ".join(self.dashedList))
        
    def __getGuess(self):

        validChar = False
        while not (validChar ==True):
            guess = input("Guess a letter:\n")
            if len(guess) == 1 and guess.isalpha():
                self.usedLetters.append(guess)
                self.lifes -= 1

                #TODO check if the letter is in the word
                
                validChar = True
            elif guess in self.usedLetters:
                print("You already used this letter, Try again:")
            else:
                print("Input not valid, Try again:")


    
        






difficulty = 0
    
while(difficulty != 1 and difficulty !=2):
    difficulty = int(input("hello, choose difficulty: 1- Easy / 2- Difficult \n"))

engine = Match(difficulty)
length = engine.getWordLength()
word= WordGuess(length)
word.game()
