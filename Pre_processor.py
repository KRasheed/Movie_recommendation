import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    @staticmethod
    def remove_punctuation(text):
        s = re.sub(r'[^a-zA-Z]', ' ', text)
        return s.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def to_lowercase(text):
        return text.lower()

    def remove_stopwords(self, text):
        words = text.split()
        text = ' '.join(word for word in words if word not in self.stop_words)
        return text

    @staticmethod
    def remove_duplicate(text):
        words = text.split()
        seen = set()
        unique_words = []

        for word in words:
            if word.lower() not in seen:
                unique_words.append(word)
                seen.add(word.lower())
        return ' '.join(unique_words)

    def lemmatize_words(self, text):
        words = text.split()
        return ' '.join(self.lemmatizer.lemmatize(word) for word in words)

    def pre_processor(self, text):
        text1 = self.remove_punctuation(text)
        text2 = self.to_lowercase(text1)
        text3 = self.remove_stopwords(text2)
        text4 = self.remove_duplicate(text3)
        text5 = self.lemmatize_words(text4)
        return text5
