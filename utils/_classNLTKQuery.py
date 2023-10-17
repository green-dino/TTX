import os
import sys
import nltk
from nltk.corpus import PlaintextCorpusReader
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    text = ''
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
    except Exception as e:
        print("Error while extracting text from PDF:", e)
    return text

# Function to add text from PDF files to the corpus
def add_pdf_files_to_corpus(corpus, pdf_directory):
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith(".pdf"):
            pdf_file_path = os.path.join(pdf_directory, pdf_file)
            pdf_text = extract_text_from_pdf(pdf_file_path)
            corpus.raw_data += pdf_text
    return corpus

def textCorpusInit(self, thePath):
    if not os.path.isdir(thePath):
        return "Path is not a Directory"
    if not os.access(thePath, os.R_OK):
        return "Directory is not readable"
    
    self.Corpus = PlaintextCorpusReader(thePath, '.*')
    print("Processing Text Files:")
    print(self.Corpus.fileids())
    print("Please wait...")
    
    # Initialize the raw data
    self.rawText = ''
    
    # Add text from PDF files
    self.Corpus = add_pdf_files_to_corpus(self.Corpus, thePath)
    
    self.rawText += self.Corpus.raw()
    self.tokens = nltk.word_tokenize(self.rawText)
    self.TextCorpus = nltk.Text(self.tokens)
    
    self.ActiveTextCorpus = True
    return "Success"


# Function to print the menu options for query
def printMenu():
    print("============NLTK Options=============")
    print("[1] Print Length of Corpus")
    print("[2] Print Number of Tokens Found")
    print("[3] Print Vocabulary Size")
    print("[4] Print Sorted Vocabulary")
    print("[5] Print Collocation")
    print("[6] Search for Word Occurrence")
    print("[7] Generate Concordance")
    print("[8] Generate Similarities")
    print("[9] Print Word Index")
    print("[10] Print Vocabulary")
    print("[0] Exit")

# Function to obtain user selection
def getUserSelection():
    printMenu()

    try:
        menuSelection = int(input('Enter Selection 0-10: '))
    except ValueError:
        print("Invalid input, enter 0-10")
        return -1
    if not menuSelection in range(0, 11):
        print("Invalid input")
        return -1
    return menuSelection

# NLTK Query Class
class classNLTKQuery:
    def textCorpusInit(self, thePath):
        if not os.path.isdir(thePath):
            return "Path is not a Directory"
        # Validate that the path is readable
        if not os.access(thePath, os.R_OK):
            return "Directory is not readable"
        # Attempt to create a corpus with .txt files
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
