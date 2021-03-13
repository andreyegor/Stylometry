import matplotlib.pyplot as plt

from os import listdir
import csv

import FictionBookLib
import TextAnalyzerLib

COLUMNS = ['Book', 'Lexical diversity', 'Mean word len',
           'Mean sentence len', 'Commas per 1000 symbols']
# supporting functions


def Graph(x_list, y_list, label_list, title="undefended"):
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


def MergeList(tlist):
    out = ''
    for val in tlist:
        out += val + ' '
    return out


# analyse functions


def Analysis(way_to_document):
    book = FictionBookLib.FB2(way_to_document)
    Analysed = TextAnalyzerLib.Analys(book.GetMainText())
    return Analysed, book


def AnalysisParts(way_to_document, sentences_in_block=100):
    book = FictionBookLib.FB2(way_to_document)
    analysed = TextAnalyzerLib.Analys(book.GetMainText(), full_analyze=False)
    sentences = analysed.GetSentences()
    qwantity_sentences = len(sentences)
    sentences_blocks = sentences[0:qwantity_sentences //
                                 sentences_in_block * sentences_in_block]
    properties = [[], [], [], []]
    for i in range((len(sentences_blocks)//sentences_in_block)-1):
        analysed_block = TextAnalyzerLib.Analys(
            MergeList(
                sentences_blocks[sentences_in_block*i:sentences_in_block*(i+1)]))
        properties[0].append(analysed_block.GetLexicalDevercity()*100)
        properties[1].append(analysed_block.GetMeanWordLen())
        properties[2].append(analysed_block.GetMeanSentenceLen())
        properties[3].append(analysed_block.GetCommasPerSymbols())
    return(properties, book)


def AnalysisFolder(way_to_folder, check_author=False, author=['name', 'surname']):
    books = []
    propertys = []
    list_of_files = listdir(way_to_folder)
    for file in list_of_files:
        analysed, book = AnalysisParts(way_to_folder+'\\'+file)
        if check_author:
            if book.GetAuthor() == author:
                books.append(book)
                propertys.append(analysed)

        else:
            books.append(book)
            propertys.append(analysed)
    return propertys, books


def AnalysisPartsFolder(way_to_folder, sentences_in_block=100, check_author=False, author=['name', 'surname']):
    books = []
    propertys = []
    list_of_files = listdir(way_to_folder)
    for tfile in list_of_files:
        a, b = AnalysisParts(way_to_folder+'/'+tfile, sentences_in_block)
        if check_author:
            if b.GetAuthor() == author:
                books.append(b.GetBookTitle() +
                             ', (' + MergeList(b.GetAuthor())+')')
                propertys.append(a)

        else:
            books.append(b.GetBookTitle() +
                         ', (' + MergeList(b.GetAuthor())+')')
            propertys.append(a)

    return propertys, books

# return functions


def ReturnAnalysis(way_to_document, in_file=False, file_name='default.csv', new=True):
    global COLUMNS
    Analysed, book = Analysis(way_to_document)
    if in_file:
        row = [book.GetAuthor()[0]+' ' + book.GetAuthor()
               [1], book.GetBookTitle()]+list(Analysed.GetAll().values())
        if new:
            f = open(file_name, 'w', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(COLUMNS)
            writer.writerow(row)
        else:
            f = open(file_name, 'a', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(row)
        f.close()
    else:
        print(str(Analysed.GetLexicalDevercity()*100) + "% - " + COLUMNS[1])
        print(str(Analysed.GetMeanWordLen()) + " - "+COLUMNS[2])
        print(str(Analysed.GetMeanSentenceLen()) +
              " - "+COLUMNS[3])
        print(str(Analysed.GetCommasPerSymbols()) +
              " - "+COLUMNS[4])


def ReturnAnalysisParts(way_to_file, sentences_in_block=150):
    global COLUMNS
    y_list, book = AnalysisParts(way_to_file, sentences_in_block)
    x_list = []
    title = book.GetBookTitle() + ', (' + MergeList(book.GetAuthor())+')'
    for i in range(4):
        x_list.append(list(range(len(y_list[i]))))
    label_list = COLUMNS[1:]
    Graph(x_list, y_list, label_list, title)


def ReturnAnalysisFolder(way_to_folder, check_author=False, author=['name', 'surname'], in_file=False, file_name='default.csv', new=True):
    global COLUMNS
    propertys, books = AnalysisFolder(way_to_folder, check_author, author)
    if in_file:
        out_file = open(file_name, 'w', encoding='utf-8')
        writer = csv.writer(out_file)
        writer.writerow(COLUMNS)
        for i in range(len(books)):
            writer.writerow([books[i]+propertys[i]])
            out_file.close()
    else:
        for i in range(len(books)):
            print([books[i]+propertys[i]])


def ReturnAnalysisPartsFolder(way_to_folder, sentences_in_block=150, check_author=False, author=['name', 'surname'], prop=0):
    global COLUMNS
    y_list = []
    x_list = []
    propertys, books = AnalysisPartsFolder(
        way_to_folder, sentences_in_block=sentences_in_block, check_author=check_author, author=author)
    for p in propertys:
        y_list.append(p[prop])
    for i in range(len(y_list)):
        x_list.append(list(range(len(y_list[i]))))
    Graph(x_list, y_list, books, title=COLUMNS[prop+1])


ReturnAnalysisParts('main/example/ex2.fb2')
