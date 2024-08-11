import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from string import punctuation
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
stop_words.update(punctuation)


class TextAnalysis:
    StopWord = []
    PositiveWords = []
    NegativeWords = []
    counter = 0

    def __init__(self, url, UrlId):
        self.set_counter()
        self.PositiveScore = None
        self.NegativeScore = None
        self.PolarityScore = None
        self.SubjectivityScore = None
        self.AvgSentLen = None
        self.CmpxWordsPercentage = None
        self.FogIndex = None
        self.AvgWordsPerSent = None
        self.CmpxWordsCount = None
        self.WordCount = None
        self.SyllablePerWord = None
        self.PersonalPronoun = None
        self.AvgWordLen = None
        self.Text = ''
        self.TextList = []
        self.CleanText = []
        self.UrlId = UrlId
        self.Url = url
        self.data_extraction()
        self.clean_text()

        self.calculate_word_count()   # 5
        self.calculate_personal_pronouns()   # 7
        self.calculate_complex_word_count()   # 4
        self.calculate_syllable_count_per_word()   # 6
        self.calculate_average_word_length()   # 8
        self.calculate_score()  # 1
        self.calculate_readability()  # 2
        self.calculate_average_no_of_words_per_sentence()  # 3

        self.get_counter()


    @classmethod
    def set_StopWord(cls):
        content = ""
        f = open('StopWords/StopWords_Auditor.txt', 'r', encoding='ISO-8859-1')
        content += f.read().lower()
        f.close()

        f = open('StopWords/StopWords_Currencies.txt', 'r', encoding='ISO-8859-1')
        content = f.read()
        f.close()

        f = open('StopWords/StopWords_DatesandNumbers.txt', 'r', encoding='ISO-8859-1')
        content += f.read().lower()
        f.close()

        f = open('StopWords/StopWords_Generic.txt', 'r', encoding='ISO-8859-1')
        content += f.read().lower()
        f.close()

        f = open('StopWords/StopWords_GenericLong.txt', 'r', encoding='ISO-8859-1')
        content += f.read().lower()
        f.close()

        f = open('StopWords/StopWords_Geographic.txt', 'r', encoding='ISO-8859-1')
        content += f.read().lower()
        f.close()

        f = open('StopWords/StopWords_Names.txt', 'r', encoding='ISO-8859-1')
        content += f.read().lower()
        f.close()

        cls.StopWord = content.split("\n")

    @classmethod
    def set_positive_words(cls):
        f = open('MasterDictionary/positive-words.txt', 'r', encoding='ISO-8859-1')
        content = f.read().lower()
        cls.PositiveWords = content.split("\n")
        f.close()

    @classmethod
    def set_negative_words(cls):
        f = open('MasterDictionary/negative-words.txt', 'r', encoding='ISO-8859-1')
        content = f.read().lower()
        cls.NegativeWords = content.split("\n")
        f.close()

    @classmethod
    def set_counter(cls):
        cls.counter += 1

    @classmethod
    def get_counter(cls):
        print(cls.counter)

    def data_extraction(self):
        page = requests.get(self.Url).text
        res = BeautifulSoup(page, "html.parser")
        title = res.find('title')
        out = title.string.extract()
        try:
            try:
                res2 = res.find(class_="td-post-content tagdiv-type")
                res2 = res2.findAll('p')
                for i in res2:
                    out += i.get_text()
                self.Text = out.lower()
                self.TextList = word_tokenize(self.Text)
            except:
                res1 = res.find(class_="td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type")
                res2 = res1.find(class_="tdb-block-inner td-fix-index")
                res2 = res2.findAll('p')
                for i in res2:
                    out += i.get_text()
                self.Text = out.lower()
                self.TextList = word_tokenize(self.Text)
        except:
            pass

    def clean_text(self):
        for w in self.TextList:
            if w not in stop_words and w not in self.StopWord:
                self.CleanText.append(w)

    def calculate_score(self):
        self.PositiveScore = 0
        self.NegativeScore = 0
        for w in self.CleanText:
            if w in self.PositiveWords:
                self.PositiveScore += 1
            if w in self.NegativeWords:
                self.NegativeScore += 1
        self.PolarityScore = (self.PositiveScore - self.NegativeScore) / (
                (self.PositiveScore + self.NegativeScore) + 0.000001)
        self.SubjectivityScore = (self.PositiveScore + self.NegativeScore) / (self.WordCount + 0.000001)

    def calculate_readability(self):
        try:
            self.AvgSentLen = len(self.CleanText) / len(sent_tokenize(self.Text))
            self.CmpxWordsPercentage = self.CmpxWordsCount / self.WordCount
            self.FogIndex = 0.4 * (self.AvgSentLen + self.CmpxWordsPercentage)
        except:
            pass

    def calculate_average_no_of_words_per_sentence(self):
        try:
            self.AvgWordsPerSent = round(len(self.TextList) / len(sent_tokenize(self.Text)))
        except:
            pass

    def calculate_word_count(self):
        self.WordCount = len(self.CleanText)

    def calculate_syllable(self, word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        ex = ['es', 'ed']
        count = 0
        pre = False
        for e in ex:
            if word.endswith(e):
                return 0
        for c in word:
            if c in vowels:
                if not pre:
                    count += 1
                pre = True
            else:
                pre = False
        return count

    def calculate_complex_word_count(self):
        count = 0
        for w in self.CleanText:
            if self.calculate_syllable(w) > 2:
                count += 1
        self.CmpxWordsCount = count

    def calculate_syllable_count_per_word(self):
        count = 0
        for w in self.CleanText:
            count += self.calculate_syllable(w)
        try:
            self.SyllablePerWord = round(count / self.WordCount)
        except:
            pass

    def calculate_personal_pronouns(self):
        list_of_words = ['i', 'we', 'my', 'our', 'us']
        count = 0
        for w in self.Text:
            if w in list_of_words:
                count += 1
        self.PersonalPronoun = count

    def calculate_average_word_length(self):
        count = 0
        for w in self.CleanText:
            for j in w:
                count += 1
        try:
            self.AvgWordLen = round(count / self.WordCount)
        except:
            pass


TextAnalysis.set_StopWord()
TextAnalysis.set_positive_words()
TextAnalysis.set_negative_words()

# df = pd.read_excel('Input.xlsx')
# url = df.to_numpy()
# print(url[0][1])
# t1 = TextAnalysis(url[35][1], url[35][0])

