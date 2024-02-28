import nltk  # Importing the Natural Language Toolkit library
from nltk.corpus import stopwords  # Importing the stopwords corpus from NLTK
from nltk.tokenize import word_tokenize, sent_tokenize  # Importing tokenize functions from NLTK

class NLU:
    def __init__(self):
        # Downloading the required NLTK packages (punkt and stopwords)
        nltk.download('punkt')
        nltk.download('stopwords')

        # Initializing the stop_words set with English stopwords
        self.stop_words = set(stopwords.words('english'))

    def understand(self, text):
        # Tokenizing the input text into sentences
        tokenized = sent_tokenize(text)

        # Iterating through each sentence
        for sentence in tokenized:
            # Tokenizing the sentence into words
            words = nltk.word_tokenize(sentence)

            # Removing stopwords from the list of words
            words = [word for word in words if not word in self.stop_words]

            # Tagging each word with its part of speech
            tagged = nltk.pos_tag(words)

            # Returning the tagged list of words
            return tagged
