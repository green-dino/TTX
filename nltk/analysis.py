import os
#import _NLTKQuery  # Ensure this module exists in your project
#import _classNLTKQuery  # Ensure this module exists in your project

print("Welcome to the NLTK Query Experimentation")
print("Please wait, loading NLTK...")

oNLTK = _classNLTKQuery.classNLTKQuery()

print("Input the full path name where intended corpus file or files are stored")
print("Note: You must enter a quoted string, e.g., 'c:\\simpson\\'")

userSpecifiedPath = input("Path: ")

# Attempt to create a text Corpus
result = oNLTK.textCorpusInit(userSpecifiedPath)

if result == "Success":
    menuSelection = -1

while menuSelection != 0:
    if menuSelection != -1:
        s = input('Press Enter to continue...')
        menuSelection = _NLTKQuery.getUserSelection()

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
        else:
            print("Unexpected error condition")
            menuSelection = 0

print("Closing NLTK Query Experimentation")
