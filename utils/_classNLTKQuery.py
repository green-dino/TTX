import os
import sys
import nltk
from nltk.corpus import PlaintextCorpusReader

# NLTK Query Class
class classNLTKQuery:
    def textCorpusInit(self, thePath):
        if not os.path.isdir(thePath):
            return "Path is not a Directory"
        # validate path is readable
        if not os.access(thePath, os.R_OK):
            return "Directory is not readable"
        # attempt to create corpus with .txt files
        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print("Processing Files:")
            print(self.Corpus.fileids())
            print("Please wait...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
        except:
            return "Creation failed"
        self.ActiveTextCorpus = True
        return "Success"

    def printCorpusLength(self):
        print("Corpus Text Length:", len(self.rawText))

    def printTokensFound(self):
        print("Tokens Found:", len(self.tokens))

    def printVocabSize(self):
        print("Calculating...")
        vocabularyUsed = set(self.TextCorpus)
        vocabularySize = len(vocabularyUsed)
        print("Vocabulary Size:", vocabularySize)

    def printSortedVocab(self):
        print("Compiling...")
        print("Sorted Vocabulary:", sorted(set(self.TextCorpus)))

    def printCollocation(self):
        print("Compiling Collocations...")
        self.TextCorpus.collocations()

    def searchWordOccurrence(self):
        myWord = input("Enter Search Word: ")
        if myWord:
            wordCount = self.TextCorpus.count(myWord)
            print(myWord + " occurred:", wordCount, "times")
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
            myWord = input("Enter word to find its index: ")
            if myWord:
                wordIndex = self.TextCorpus.index(myWord)
                print("First Occurrence of " + myWord + " is at offset:", wordIndex)
            else:
                print("Word Entry is Invalid")

    def printVocabulary(self):
        print("Compiling Vocabulary Frequencies")
        vocabFreqList = self.TextCorpus.vocab()
        print(vocabFreqList.items())

if __name__ == "__main__":
    oNLTK = classNLTKQuery()
    print("Welcome to the NLTK Query Experimentation")
    print("Please wait while loading NLTK...")
    
    userSpecifiedPath = input("Enter the full path where the corpus file(s) are stored (e.g., 'c:\\simpson\\'): ")
    
    # Attempt to create a text Corpus
    result = oNLTK.textCorpusInit(userSpecifiedPath)
    
    if result == "Success":
        menuSelection = -1
        while menuSelection != 0:
            if menuSelection != -1:
                s = input('Press Enter to continue...')
            menuSelection = int(input("Select an option:\n"
                                      "1. Print Corpus Length\n"
                                      "2. Print Tokens Found\n"
                                      "3. Print Vocabulary Size\n"
                                      "4. Print Sorted Vocabulary\n"
                                      "5. Print Collocation\n"
                                      "6. Search for Word Occurrence\n"
                                      "7. Generate Concordance\n"
                                      "8. Generate Similarities\n"
                                      "9. Print Word Index\n"
                                      "10. Print Vocabulary\n"
                                      "0. Exit\n"
                                      "Enter your choice: "))
            if menuSelection == 1:
                oNLTK.printCorpusLength()
            elif menuSelection == 2:
                oNLTK.printTokensFound()
            elif menuSelection == 3:
                oNLTK.printVocabSize()
            elif menuSelection == 4:
                oNLTK.printSortedVocab()
            elif menuSelection == 5:
                oNLTK.printCollocation()
            elif menuSelection == 6:
                oNLTK.searchWordOccurrence()
            elif menuSelection == 7:
                oNLTK.generateConcordance()
            elif menuSelection == 8:
                oNLTK.generateSimilarities()
            elif menuSelection == 9:
                oNLTK.printWordIndex()
            elif menuSelection == 10:
                oNLTK.printVocabulary()
            elif menuSelection == 0:
                print("Goodbye")
            elif menuSelection == -1:
                continue
            else:
                print("Unexpected error condition")
                menuSelection = 0
    
    print("Closing NLTK Query Experimentation")
