import os
import sys
import logging
import nltk
from nltk.corpus import PlaintextCorpusReader

class NLTKQuery:
    def __init__(self):
        self.Corpus = None
        self.rawText = None
        self.tokens = None
        self.TextCorpus = None
        self.ActiveTextCorpus = False

    def textCorpusInit(self, thePath):
        if not os.path.isdir(thePath):
            return "Path is not a Directory"
        
        if not os.access(thePath, os.R_OK):
            return "Directory is not Readable"

        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print("Processing Files:")
            print(self.Corpus.fileids())
            print("Please wait...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
            self.ActiveTextCorpus = True
            return "Success"
        except Exception as e:
            return "Corpus Creation Failed: " + str(e)

    def printCorpusLength(self):
        print("Corpus Text Length: ", len(self.rawText))

    def printTokensFound(self):
        print("Tokens Found: ", len(self.tokens))

    def printVocabSize(self):
        print("Calculating...")
        vocabularyUsed = set(self.TextCorpus)
        vocabularySize = len(vocabularyUsed)
        print("Vocabulary Size: ", vocabularySize)

    def printSortedVocab(self):
        print("Compiling...")
        print("Sorted Vocabulary ", sorted(set(self.TextCorpus)))

    def printCollocation(self):
        print("Compiling Collocations...")
        self.TextCorpus.collocations()

    def searchWordOccurrence(self):
        myWord = input("Enter Search Word: ")
        if myWord:
            wordCount = self.TextCorpus.count(myWord)
            print(myWord + " occurred: ", wordCount, " times")
        else:
            print("Word Entry is Invalid")

    def generateConcordance(self):
        myWord = input("Enter word to Concord: ")
        if myWord:
            self.TextCorpus.concordance(myWord)
        else:
            print("Word Entry is Invalid")

    def generateSimilarities(self):
        myWord = input("Enter seed word: ")
        if myWord:
            self.TextCorpus.similar(myWord)
        else:
            wordIndex = self.TextCorpus.index(myWord)
            print("First Occurrence of: " + myWord + " is at offset: ", wordIndex)
            print("Word Entry is Invalid")

    def printVocabulary(self):
        print("Compiling Vocabulary Frequencies")
        vocabFreqList = self.TextCorpus.vocab()
        print(list(vocabFreqList.items()))

if __name__ == '__main__':
    nltk_query = NLTKQuery()
    print("Welcome to the NLTK Query Experimentation")
    print("Please wait loading NLTK . . .")
    userSpecifiedPath = input("Enter the path where the corpus files are stored: ")

    result = nltk_query.textCorpusInit(userSpecifiedPath)
    if result == "Success":
        menuSelection = -1

        while menuSelection != 0:
            if menuSelection != -1:
                s = input('Press Enter to continue...')
                menuSelection = int(input("Enter a menu option: "))
                if menuSelection == 1:
                    nltk_query.printCorpusLength()
                elif menuSelection == 2:
                    nltk_query.printTokensFound()
                elif menuSelection == 3:
                    nltk_query.printVocabSize()
                elif menuSelection == 4:
                    nltk_query.printSortedVocab()
                elif menuSelection == 5:
                    nltk_query.printCollocation()
                elif menuSelection == 6:
                    nltk_query.searchWordOccurrence()
                elif menuSelection == 7:
                    nltk_query.generateConcordance()
                elif menuSelection == 8:
                    nltk_query.generateSimilarities()
                elif menuSelection == 10:
                    nltk_query.printVocabulary()
                elif menuSelection == 0:
                    print("Goodbye")
                elif menuSelection == -1:
                    continue
                else:
                    print("Unexpected error condition")
                    menuSelection = 0

    print("Closing NLTK Query Experimentation")
