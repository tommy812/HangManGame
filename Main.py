from Match import *
from WordGuess import *

def main():
    difficulty = 0
    finished= False
    
    while(difficulty != 1 and difficulty !=2):
        difficulty = int(input("hello, choose difficulty: 1- Easy / 2- Difficult \n"))


    #print(words)
    while not finished:
        match = Match(difficulty)
        finished = match.start()


if __name__ == '__main__':
    main()


