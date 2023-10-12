utils._languageQuery import _languageQuery

class NLTKQueryExperiment:
    def __init__(self):
        print("Welcome to the NLTK Query Experimentation")
        print("Please wait loading NLTK . . .")
        self.oNLTK = _languageQuery.classNLTKQuery()

    def input_corpus_path(self):
        print("Input full path name where intended corpus file or files are stored")
        print("Note: you must enter a quoted string e.g. c:\\simpson\\")
        user_specified_path = raw_input("Path: ")
        return user_specified_path

    def run(self):
        user_specified_path = self.input_corpus_path()
        result = self.oNLTK.textCorpusInit(user_specified_path)
        
        if result != "Success":
            menu_selection = -1
        
        while menu_selection != 0:
            if menu_selection != -1:
                s = raw_input('Press Enter to continue. . .')
                menu_selection = _languageQuery.getUserSelection()

                if menu_selection == 1:
                    self.oNLTK.printCorpusLength()
                elif menu_selection == 2:
                    self.oNLTK.printTokensFound()
                elif menu_selection == 3:
                    self.oNLTK.printVocabSize()
                elif menu_selection == 4:
                    self.oNLTK.printSortedVocab()
                elif menu_selection == 5:
                    self.oNLTK.printCollocation()
                elif menu_selection == 6:
                    self.oNLTK.searchWordOccurrence()
                elif menu_selection == 7:
                    self.oNLTK.generateConcordance()
                elif menu_selection == 8:
                    self.oNLTK.generateSimilarities()
                elif menu_selection == 9:
                    self.oNLTK.printWordIndex()
                elif menu_selection == 10:
                    self.oNLTK.printVocabulary()
                elif menu_selection == 0:
                    print("Goodbye")
                elif menu_selection == -1:
                    continue
                else:
                    print("unexpected error condition")
                    menu_selection = 0
        print("Closing NLTK Query Experimentation")

if __name__ == '__main__':
    nltk_query_experiment = NLTKQueryExperiment()
    nltk_query_experiment.run()
