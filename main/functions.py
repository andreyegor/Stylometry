import matplotlib.pyplot as plt

from os import listdir
import csv

import fictionbooklib
import textanalyzerlib

COLUMNS = ['Book', 'Lexical diversity', 'Mean word len',
           'Mean sentence len', 'Commas per 1000 symbols']
# supporting functions


def graph(x_list, y_list, label_list, title="undefended"):
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


def merge_list(tlist):
    out = ''
    for val in tlist:
        out += val + ' '
    return out


# analyse functions


def analysis(way_to_document):
    book = fictionbooklib.FB2(way_to_document)
    Analysed = textanalyzerlib.analys(book.get_main_text())
    return Analysed, book


def analysis_parts(way_to_document, sentences_in_block=100):
    book = fictionbooklib.FB2(way_to_document)
    analysed = textanalyzerlib.analys(book.get_main_text(), full_analyze=False)
    sentences = analysed.get_sentences()
    qwantity_sentences = len(sentences)
    sentences_blocks = sentences[0:qwantity_sentences //
                                 sentences_in_block * sentences_in_block]
    properties = [[], [], [], []]
    for i in range((len(sentences_blocks)//sentences_in_block)-1):
        analysed_block = textanalyzerlib.analys(
            merge_list(
                sentences_blocks[sentences_in_block*i:sentences_in_block*(i+1)]))
        properties[0].append(analysed_block.get_lexical_devercity()*100)
        properties[1].append(analysed_block.get_mean_word_len())
        properties[2].append(analysed_block.get_mean_sentence_len())
        properties[3].append(analysed_block.get_commas_per_symbols())
    return(properties, book)


def analysis_folder(way_to_folder, check_author=False, author=['name', 'surname']):
    books = []
    propertys = []
    list_of_files = listdir(way_to_folder)
    for file in list_of_files:
        analysed, book = analysis(way_to_folder+'\\'+file)
        if check_author:
            if book.get_author() == author:
                books.append(book)
                propertys.append(analysed)

        else:
            books.append(book)
            propertys.append(analysed)
    return propertys, books


def analysis_parts_folder(way_to_folder, sentences_in_block=100, check_author=False, author=['name', 'surname']):
    books = []
    propertys = []
    list_of_files = listdir(way_to_folder)
    for tfile in list_of_files:
        a, b = analysis_parts(way_to_folder+'/'+tfile, sentences_in_block)
        if check_author:
            if b.get_author() == author:
                books.append(b.get_book_title() +
                             ', (' + merge_list(b.get_author())+')')
                propertys.append(a)

        else:
            books.append(b.get_book_title() +
                         ', (' + merge_list(b.get_author())+')')
            propertys.append(a)

    return propertys, books

# return functions


def return_analysis(way_to_document, in_file=False, file_name='default.csv', new=True):
    global COLUMNS
    Analysed, book = analysis(way_to_document)
    if in_file:
        row = [book.get_author()[0]+' ' + book.get_author()
               [1], book.get_book_title()]+list(Analysed.get_all().values())
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
        print(str(Analysed.get_lexical_devercity()*100) + "% - " + COLUMNS[1])
        print(str(Analysed.get_mean_word_len()) + " - "+COLUMNS[2])
        print(str(Analysed.get_mean_sentence_len()) +
              " - "+COLUMNS[3])
        print(str(Analysed.get_commas_per_symbols()) +
              " - "+COLUMNS[4])


def return_analysis_parts(way_to_file, sentences_in_block=150):
    global COLUMNS
    y_list, book = analysis_parts(way_to_file, sentences_in_block)
    x_list = []
    title = book.get_book_title() + ', (' + merge_list(book.get_author())+')'
    for i in range(4):
        x_list.append(list(range(len(y_list[i]))))
    label_list = COLUMNS[1:]
    graph(x_list, y_list, label_list, title)


def return_analysis_folder(way_to_folder, check_author=False, author=['name', 'surname'], in_file=False, file_name='default.csv', new=True):
    global COLUMNS
    propertys, books = analysis_folder(way_to_folder, check_author, author)
    if in_file:
        out_file = open(file_name, 'w', encoding='utf-8')
        writer = csv.writer(out_file)
        writer.writerow(COLUMNS)
        for i in range(len(books)):
            writer.writerow(
                [books[i].get_book_title()+str(propertys[i].GetAll())[1:-1]])
        out_file.close()
    else:
        for i in range(len(books)):
            print(books[i].get_book_title()+str(propertys[i].GetAll())[1:-1])


def return_analysis_parts_folder(way_to_folder, sentences_in_block=150, check_author=False, author=['name', 'surname'], prop=0):
    global COLUMNS
    y_list = []
    x_list = []
    propertys, books = analysis_parts_folder(
        way_to_folder, sentences_in_block=sentences_in_block, check_author=check_author, author=author)
    for p in propertys:
        y_list.append(p[prop])
    for i in range(len(y_list)):
        x_list.append(list(range(len(y_list[i]))))
    graph(x_list, y_list, books, title=COLUMNS[prop+1])
