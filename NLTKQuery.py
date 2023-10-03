import sys
from .utils import _classNLTKQuery #This module defines a new class that when instantiated and
#used properly will allow access to NLTK methods in a controlled manner
from .utils import _NLTKQuery #This module provides support functions for the NLTKQuery main program loop, mainly to handle user input and menu display


# Serves as the main program loop for interfacing with NLTK

print("Welcome to the Natural Language ToolKit\n")
print("Please wait while the system loads")

import sys
import _NLTKQuery
print("Welcome to the NLTK Query Experimentation")
print("Please wait loading NLTK . . . ")
import _classNLTKQuery
oNLTK = _classNLTKQuery.classNLTKQuery()
print()
print("Input full path name where intended corpus file or files are stored")
print("Note: you must enter a quoted string e.g. c:\\simpson\\ ")
print()
userSpecifiedPath = input("Path: ")

# Attempt to create a text Corpus
result = oNLTK.textCorpusInit(userSpecifiedPath)
if result == "Success":
    menuSelection = -1

while menuSelection != 0:
    if menuSelection != -1:
        print()
        s = input('Press Enter to continue. . .')
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
        oNLTK.generateSimiliarities()
    elif menuSelection == 9:
        oNLTK.printWordIndex()
    elif menuSelection == 10:
        oNLTK.printVocabulary()
    elif menuSelection == 0:
        print("Goodbye")
        print()
    elif menuSelection == -1:
        continue
    else:
        print("unexpected error condition")
        menuSelection = 0

print("Closing NLTK Query Experimentation")
