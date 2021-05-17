import nltk
import string


def punkt_download():
    nltk.download('punkt')


class analys:
    properties = {}

    def __init__(self, text, quantity_symbols=1000, full_analyze=True):
        """Класс для стилометрического анализа текста. "Parse" функции нужны чтобы узнавать конкретные параметры текста. "Get" функции нужны для того, чтобы получать эти параметры.

        Args:
            text (string): Ваш текст
            quantity_symbols (int, optional): Длинна фрагментов текста, которые будут анализироваться некоторыми методами. По умолчанию 1000.
            full_analyze (bool, optional): True для полного анализа, False дла самостоятельного анализа. По умолчанию True.
        """
        self.text = text
        self.tokens = nltk.word_tokenize(text)
        self.sentences = nltk.sent_tokenize(text)
        self.quantity_symbols = quantity_symbols
        self.remove_punctuation()
        if full_analyze:
            self.full_parse()

    def full_parse(self):
        """Это функция для полного анализа текста"""
        self.parse_lexical_divercity()
        self.parse_mean_word_len()
        self.parse_mean_sentence_len()
        self.parse_commas_per_characters()

    def remove_punctuation(self):
        """Это функция для удаления пунктуации из токенов"""
        remove_punctuation = str.maketrans('', '', string.punctuation)
        out = []
        for token in self.tokens:
            translated = token.translate(remove_punctuation).lower()
            if translated != '':
                out.append(translated)
        self.tokens_without_punctuation = out

    def parse_lexical_divercity(self):
        out = (len(set(
            self.tokens_without_punctuation)) / len(self.tokens_without_punctuation))
        self.properties['lexical_diversity'] = out
        return out

    def parse_mean_word_len(self):
        word_char = []
        words = set(self.tokens_without_punctuation)
        for word in words:
            word_char.append(len(word))
        out = sum(word_char) / float(len(word_char))
        self.properties['mean_word_len'] = out
        return out

    def parse_mean_sentence_len(self):
        sentence_len = []
        for sentence in self.sentences:
            sentence_len.append(len(sentence))
        out = sum(sentence_len) / float(len(sentence_len))
        out = sum(sentence_len)/len(sentence_len)
        self.properties['mean_sentence_len'] = out
        return out

    def elements_per_characters(self, element):
        """Это функция для поиска количества елементов на символы

        Args:
            element (string): Ваш элемент
        """
        fdist = nltk.probability.FreqDist(nltk.Text(self.tokens))
        elements = (fdist[element] * self.quantity_symbols) / fdist.N()
        return elements

    def parse_commas_per_characters(self):
        out = self.elements_per_characters(',')
        self.properties['commas_per_symbols'] = out
        return out

    def get_tokens(self):
        return self.tokens

    def get_sentences(self):
        return self.sentences

    def get_lexical_devercity(self):
        return self.properties['lexical_diversity']

    def get_mean_word_len(self):
        return self.properties['mean_word_len']

    def get_mean_sentence_len(self):
        return self.properties['mean_sentence_len']

    def get_commas_per_symbols(self):
        return self.properties['commas_per_symbols']

    def get_all(self):
        return self.properties
