import nltk
import string


nltk.download('punkt')


class Analys:
    properties = {}

    def __init__(self, text, quantity_symbols=1000, full_analyze=True):
        """Class for stylometric text analysis. "Parse" functions are needed to parse some text properties. "Get" functions are needed to get this propertiers.

        Args:
            text (string): Your text
            quantity_symbols (int, optional): Length of the text fragment to be analyzed. Defaults to 1000.
            full_analyze (bool, optional): True for full text analysis, False for manual analysis. Defaults to True.
        """
        self.text = text
        self.tokens = nltk.word_tokenize(text)
        self.sentences = nltk.sent_tokenize(text)
        self.quantity_symbols = quantity_symbols
        self.RemovePunctuation()
        if full_analyze:
            self.FullParse()

    def FullParse(self):
        """This is a function to full text analysis"""
        self.ParseLexicalDivercity()
        self.ParseMeanWordLen()
        self.ParseMeanSentenceLen()
        self.ParseCommasPerСharacters()

    def RemovePunctuation(self):
        """This is a function to remove punctuation from tokens"""
        remove_punctuation = str.maketrans('', '', string.punctuation)
        out = []
        for token in self.tokens:
            translated = token.translate(remove_punctuation).lower()
            if translated != '':
                out.append(translated)
        self.tokens_without_punctuation = out

    def ParseLexicalDivercity(self):
        out = (len(set(
            self.tokens_without_punctuation)) / len(self.tokens_without_punctuation))
        self.properties['lexical_diversity'] = out
        return out

    def ParseMeanWordLen(self):
        word_char = []
        words = set(self.tokens_without_punctuation)
        for word in words:
            word_char.append(len(word))
        out = sum(word_char) / float(len(word_char))
        self.properties['mean_word_len'] = out
        return out

    def ParseMeanSentenceLen(self):
        sentence_len = []
        for sentence in self.sentences:
            sentence_len.append(len(sentence))
        out = sum(sentence_len) / float(len(sentence_len))
        out = sum(sentence_len)/len(sentence_len)
        self.properties['mean_sentence_len'] = out
        return out

    def ElementsPerСharacters(self, element, qwantity):
        """This function finds the number of elements per characters in the text

        Args:
            element ([type]): You element
            qwantity ([type]): number of symbols
        """
        fdist = nltk.probability.FreqDist(nltk.Text(self.tokens))
        elements = (fdist[element] * qwantity) / fdist.N()
        return elements

    def ParseCommasPerСharacters(self):
        out = self.ElementsPerСharacters(',', self.quantity_symbols)
        self.properties['commas_per_symbols'] = out
        return out

    def GetTokens(self):
        return self.tokens

    def GetSentences(self):
        return self.sentences

    def GetLexicalDevercity(self):
        return self.properties['lexical_diversity']

    def GetMeanWordLen(self):
        return self.properties['mean_word_len']

    def GetMeanSentenceLen(self):
        return self.properties['mean_sentence_len']

    def GetCommasPerSymbols(self):
        return self.properties['commas_per_symbols']

    def GetAll(self):
        return self.properties
