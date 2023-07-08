import random 
import string
from dataclasses import dataclass,field

def importDictionary():
        my_file = open("Dictionary.txt", "r")
        data = my_file.read()
        return data.split("\n")

@dataclass
class Dictionary:
    length: int 
    dictionary: list[str] = field(default_factory=list)
    dictionary_copy: list[str] = field(default_factory=list)
    pos: list[int] = field(default_factory = list)
    tempWord: str = ""
    guessCounter = 0

    def __post_init__(self):
        self.dictionary = importDictionary()
        self.dict2 = self.dictionary



    #filter dictionary by word length
    def refineDictionary(self):
        self.dictionary = [word for word in self.dictionary if len(word) == self.length]


    def refineDictionaryCopy(self):
        self.dict2 = [word for word in self.dict2 if len(word) == self.length]

    def check_Letter_easy(self, letter):
        word_groups = {}
        # Keep track of words with no occurrences of the letter
        no_letter_words = []

        #print(self.dictionary)

        #TODO check frequency / make a matrix [nword][positions] / id positions == then add to counter 
        self.refineDictionary()

        for word in self.dictionary:
            positions = [i for i, char in enumerate(word) if char == letter] 

            key = tuple(positions)

            if positions:
                key = tuple(positions)
                if key in word_groups:
                    word_groups[key].append(word)
                else:
                    word_groups[key] = [word]
            else:
                no_letter_words.append(word)

        largest_group = []

        #print(word_groups.items())

        for positions, words in word_groups.items():
            if len(words) > len(largest_group):
                largest_group = words
                self.pos = positions

        # Check if the group of words without the letter is the largest
        if len(no_letter_words) > len(largest_group):
            largest_group = no_letter_words
            self.dictionary = largest_group
            self.tempWord = largest_group[0]
            self.pos = None
            return False
        else:
            self.dictionary = largest_group
            self.tempWord = largest_group[0]
            return True

    def check_Letter_hard(self, letter):
        self.getLetterProbabilities(self.dictionary)
        return True


            
    def possible_letters(self, letterUsed):
        alphabet=list(string.ascii_lowercase)   
        moves = [x for x in alphabet if x not in letterUsed]

        return moves





















    def evaluate(self):
        return (self.length - self.guessCounter) / len(self.dictionary)
        #when guessesLeft + le
    def getLetterProbabilities(self, dictionary):
        alphabet = list(string.ascii_lowercase)
        probabilities = {letter: 0 for letter in alphabet}
        total_letters = 0

        for word in dictionary:
            for letter in word:
                if letter in alphabet:
                    probabilities[letter] += 1
                    total_letters += 1

        for letter in probabilities:
            probabilities[letter] /= total_letters

        highest_value = max(probabilities.values())
        highest_letter = [letter for letter, probability in probabilities.items() if probability == highest_value]

        print(f"The letter(s) with the highest probability value is/are: {', '.join(highest_letter)}")

        return probabilities

    # now we have the letter frequencies




    def check_Letter_har(self,letter, usedLetters):
        score = (self.length - self.guessCounter) / len(self.dictionary)
        availableLetters = self.possible_letters(usedLetters)
        position = self.getLetterProbabilities(availableLetters)

        #position? how many moves, . ,. ,is the 
        print(self.minimax(position, 3, float('-inf'), float('+inf'), True ))



        return False



    def minimax(self, position, depth, alpha, beta, maximizingPlayer):
        if depth == 0:
            return position
        
        if maximizingPlayer:
            maxEval = float('-inf')
            for child in position:
                evaluation = self.minimax(child,depth -1, alpha, beta,False)
                maxEval = max(maxEval, evaluation)
                alpha = max(alpha,evaluation)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = float('+inf')
            for child in position:
                evaluation = self.minimax(child,depth -1, alpha, beta,True)
                minEval = min(minEval, evaluation)
                beta = min(beta,evaluation)

                if beta <= alpha:
                    break
            return minEval



    # def minimax(availableLetters, score,lifes, depth, max_player, game):
    #     choice == True
    #     if depth == 0 or score == 0:
    #         return choice

    #     if max_player:
    #         maxEval = float('-inf')
    #         best_move = None
    #         for letters in availableLetters









    