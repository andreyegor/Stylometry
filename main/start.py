from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import matplotlib.pyplot as plt
import easygui

from os import listdir
import csv

import FictionBook
import TextAnalyzer

patch = ''


class StylometryApp(App):
    COLUMNS = ['Book', 'Lexical diversity', 'Mean word len',
               'Mean sentence len', 'Commas per 1000 symbols']

    def build(self):
        gl = GridLayout(cols=2)
        gl.add_widget(Button(
            text="Анализ папки по лексическому разнообразию", on_press=self.ReturnAnalysisPartsFolderLexicalDevercity))
        gl.add_widget(Button(text="Анализ папки по средней длинне слова",
                             on_press=self.ReturnAnalysisPartsFolderMeanWordLen))
        gl.add_widget(Button(text="Анализ папки по средней длинне предложения",
                             on_press=self.ReturnAnalysisPartsFolderMeanSentenceLen))
        gl.add_widget(Button(text="Анализ папки по количеству запятых на 1000 символов",
                             on_press=self.ReturnAnalysisPartsFolderCommasPerSymbols))

        return gl

    def IsTherePatch(self, function):
        if self.patch != '_none_':
            function()

    def OpenFile(self, patch):
        if patch[-4:] == '.fb2':
            book = FictionBook.FB2(patch())
            self.text = book.GetMainText()
            self.author = book.GetAuthor()
            self.book_title = book.GetBookTitle()
        else:
            f = open('text.txt', 'r')
            self.text = f.read()
            f.close()
            self.author = ''
            self.book_title = ''

    def GetPatch(self):
        self.patch = easygui.fileopenbox()

    def GetPatchFolder(self):
        self.patch_folder = easygui.diropenbox()

    def MergeList(self, tlist):
        out = ''
        for val in tlist:
            out += val + ' '
        return out

    def Graph(self, x_list, y_list, label_list, title):
        if len(y_list) == len(y_list) == len(label_list):
            ax = plt.subplots()[1]
            ax.grid()
            for i in range(len(y_list)):
                if len(y_list[i]) == len(y_list[i]):
                    ax.plot(x_list[i], y_list[i], label=label_list[i])
                else:
                    raise ValueError(label_list[i])
        ax.set_title(title)
        ax.legend()
        plt.show()

    def AnalysisParts(self, way_to_document, sentences_in_block=100):
        book = FictionBook.FB2(way_to_document)
        analysed = TextAnalyzer.Analys(book.GetMainText(), full_analyze=False)
        sentences = analysed.GetSentences()
        qwantity_sentences = len(sentences)
        sentences_blocks = sentences[0:qwantity_sentences //
                                     sentences_in_block * sentences_in_block]
        properties = [[], [], [], []]
        for i in range((len(sentences_blocks)//sentences_in_block)-1):
            analysed_block = TextAnalyzer.Analys(
                self.MergeList(
                    sentences_blocks[sentences_in_block*i:sentences_in_block*(i+1)]))
            properties[0].append(analysed_block.GetLexicalDevercity()*100)
            properties[1].append(analysed_block.GetMeanWordLen())
            properties[2].append(analysed_block.GetMeanSentenceLen())
            properties[3].append(analysed_block.GetCommasPerSymbols())
        return(properties, book)

    def AnalysisPartsFolder(self, way_to_folder, sentences_in_block=100, check_author=False, author=['name', 'surname']):
        books = []
        propertys = []
        list_of_files = listdir(way_to_folder)
        for tfile in list_of_files:
            a, b = self.AnalysisParts(
                way_to_folder+'/'+tfile, sentences_in_block)
            if check_author:
                if b.GetAuthor() == author:
                    books.append(b.GetBookTitle() +
                                 ', (' + self.MergeList(b.GetAuthor())+')')
                    propertys.append(a)

            else:
                books.append(b.GetBookTitle() +
                             ', (' + self.MergeList(b.GetAuthor())+')')
                propertys.append(a)

        return propertys, books

    def ReturnAnalysisPartsFolder(self, sentences_in_block=150, check_author=False, author=['name', 'surname'], prop=0):
        self.GetPatchFolder()
        y_list = []
        x_list = []
        propertys, books = self.AnalysisPartsFolder(
            self.patch_folder, sentences_in_block=sentences_in_block, check_author=check_author, author=author)
        for p in propertys:
            y_list.append(p[prop])
        for i in range(len(y_list)):
            x_list.append(list(range(len(y_list[i]))))
        self.Graph(x_list, y_list, books, self.COLUMNS[prop+1])

    def ReturnAnalysisPartsFolderLexicalDevercity(self, instance):
        self.ReturnAnalysisPartsFolder(prop=0)

    def ReturnAnalysisPartsFolderMeanWordLen(self, instance):
        self.ReturnAnalysisPartsFolder(prop=1)

    def ReturnAnalysisPartsFolderMeanSentenceLen(self, instance):
        self.ReturnAnalysisPartsFolder(prop=2)

    def ReturnAnalysisPartsFolderCommasPerSymbols(self, instance):
        self.ReturnAnalysisPartsFolder(prop=3)


if __name__ == '__main__':
    StylometryApp().run()
