import os
import sys
import logging
import nltk
from nltk.corpus import PlaintextCorpusReader

# NLTK Query Class

class classNLTKQueery:
    def textCorpusInit(self.thePath):
        if not os.path.isdir(thePath):
            return "Path is not a Directory"
        # validate path is readable
        if not os.access(thePath, os.R_OK)
            return ("directory is not readable")
        # attempt to create corpus with .txt files
        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print("Processing Files:")
            print(self.Corpus.fileids())
            print("please wait")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
        except:
            return "Creation failed"
        self.ActiveTextCorpus = True
        return "success"
    
