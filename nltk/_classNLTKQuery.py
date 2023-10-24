import os
import nltk
import PyPDF2
from nltk.corpus import PlaintextCorpusReader

class NLTKQuery:
    def __init__(self):
        self.active_text_corpus = None
        self.raw_text = None
        self.tokens = None

    # Function to extract text from a PDF file
    def extract_text_from_pdf(self, file_path):
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
    def add_pdf_files_to_corpus(self, corpus, pdf_directory):
        for pdf_file in os.listdir(pdf_directory):
            if pdf_file.endswith(".pdf"):
                pdf_file_path = os.path.join(pdf_directory, pdf_file)
                pdf_text = self.extract_text_from_pdf(pdf_file_path)
                corpus.raw_data += pdf_text
        return corpus

    def text_corpus_init(self, the_path):
        if not os.path.isdir(the_path):
            return "Path is not a Directory"
        if not os.access(the_path, os.R_OK):
            return "Directory is not readable"

        self.corpus = PlaintextCorpusReader(the_path, '.*')
        print("Processing Text Files:")
        print(self.corpus.fileids())
        print("Please wait...")

        # Initialize the raw data
        self.raw_text = ''
        
        # Add text from PDF files
        self.corpus = self.add_pdf_files_to_corpus(self.corpus, the_path)

        self.raw_text += self.corpus.raw()
        self.tokens = nltk.word_tokenize(self.raw_text)
        self.active_text_corpus = True
        return "Success"

    def print_corpus_length(self):
        if self.active_text_corpus:
            print("Corpus Text Length:", len(self.raw_text))
        else:
            print("No active text corpus.")

    def print_tokens_found(self):
        if self.active_text_corpus:
            print("Tokens Found:", len(self.tokens))
        else:
            print("No active text corpus.")

    def print_vocab_size(self):
        if self.active_text_corpus:
            print("Calculating...")
            vocabulary_used = set(self.tokens)
            vocabulary_size = len(vocabulary_used)
            print("Vocabulary Size:", vocabulary_size)
        else:
            print("No active text corpus.")

    def print_sorted_vocab(self):
        if self.active_text_corpus:
            print("Compiling...")
            print("Sorted Vocabulary:", sorted(set(self.tokens)))
        else:
            print("No active text corpus.")

    def print_collocation(self):
        if self.active_text_corpus:
            print("Compiling Collocations...")
            nltk.Text(self.tokens).collocations()
        else:
            print("No active text corpus.")

    def search_word_occurrence(self):
        if self.active_text_corpus:
            my_word = input("Enter Search Word: ")
            if my_word:
                word_count = self.tokens.count(my_word)
                print(my_word + " occurred:", word_count, "times")
            else:
                print("Word Entry is Invalid")
        else:
            print("No active text corpus.")

if __name__ == "__main__":
    nltk_query = NLTKQuery()
    print("Welcome to the NLTK Query Experimentation")
    print("Please wait while loading NLTK...")

    user_specified_path = input("Enter the full path where the corpus file(s) are stored (e.g., 'user/dir\\'): ")

    result = nltk_query.text_corpus_init(user_specified_path)

    if result == "Success":
        menu_selection = -1
        while menu_selection != 0:
            if menu_selection != -1:
                input('Press Enter to exit...')
            menu_selection = int(input("Select an option:\n"
                                      "1. Print Corpus Length\n"
                                      "2. Print Tokens Found\n"
                                      "3. Print Vocabulary Size\n"
                                      "4. Print Sorted Vocabulary\n"
                                      "5. Print Collocation\n"
                                      "6. Search for Word Occurrence\n"
                                      "0. Exit\n"
                                      "Enter your choice: "))
            if menu_selection == 1:
                nltk_query.print_corpus_length()
            elif menu_selection == 2:
                nltk_query.print_tokens_found()
            elif menu_selection == 3:
                nltk_query.print_vocab_size()
            elif menu_selection == 4:
                nltk_query.print_sorted_vocab()
            elif menu_selection == 5:
                nltk_query.print_collocation()
            elif menu_selection == 6:
                nltk_query.search_word_occurrence()
            elif menu_selection == 0:
                print("Goodbye")
            elif menu_selection == -1:
                continue
            else:
                print("Unexpected error condition")

    print("Closing NLTK Query Experimentation")
