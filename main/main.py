from os import listdir
import csv

import FictionBookLib
import TextAnalyzerLib

COLUMNS = ['Author', 'Title', 'Lexical diversity', 'Mean word len',
           'Mean sentence len', 'Commas per 1000 symbols']

# analyse block


def analysis(way_to_document):
    book = FictionBookLib.FB2(way_to_document)
    print('Please wait...')
    Analysed = TextAnalyzerLib.Analys(book.GetMainText())
    return Analysed, book


def MergeList(list):
    out = ''
    for val in list:
        out += val + ' '
    return out


def analysis_parts(way_to_document, sentences_in_block=100):
    book = FictionBookLib.FB2(way_to_document)
    analysed = TextAnalyzerLib.Analys(book.GetMainText(), full_analyze=False)
    sentences = analysed.GetSentences()
    qwantity_sentences = len(sentences)
    sentences_blocks = sentences[0:qwantity_sentences //
                                 sentences_in_block * sentences_in_block]
    properties = [[], [], [], []]
    print("Please wait...")
    for i in range((len(sentences_blocks)//sentences_in_block)-1):
        analysed_block = TextAnalyzerLib.Analys(
            MergeList(
                sentences_blocks[sentences_in_block*i:sentences_in_block*(i+1)]))
        properties[0].append(analysed_block.GetLexicalDevercity())
        properties[1].append(analysed_block.GetMeanWordLen())
        properties[2].append(analysed_block.GetMeanSentenceLen())
        properties[3].append(analysed_block.GetCommasPerSymbols())
        print(i, end=', ')
    return(properties, book)


def analysis_folder(way_to_folder, check_author=False, author=['name', 'surname']):
    books = []
    analysed = []
    list_of_files = listdir(way_to_folder)
    for file in list_of_files:
        book = FictionBookLib.FB2(way_to_folder+'\\'+file)
        if check_author:
            if book.GetAuthor() == author:
                analysed.append(TextAnalyzerLib.Analys(book.GetMainText()))
                books.append(book)
    return analysed, books

# return block


def return_analysis_one(way_to_document, in_file=False, new=True):
    global COLUMNS
    Analysed, book = analysis(way_to_document)
    if in_file:
        row = [book.GetAuthor()[0]+' ' + book.GetAuthor()
               [1], book.GetBookTitle()]+list(Analysed.GetAll().values())
        if new:
            f = open(in_file, 'w', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(COLUMNS)
            writer.writerow(row)
        else:
            f = open(in_file, 'a', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(row)
        f.close()
    else:
        print(str(Analysed.GetLexicalDevercity()*100) + r"% - lexical devercity")
        print(str(Analysed.GetMeanWordLen()) + " - mean word len")
        print(str(Analysed.GetMeanSentenceLen()) +
              " - mean sentence len")
        print(str(Analysed.GetCommasPerSymbols()) +
              " - commas per 1000 symbols")
    print("Success!")
