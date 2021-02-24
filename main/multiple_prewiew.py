from os import listdir
import csv

import FictionBookLib
import TextAnalyzerLib
author = ['Аркадий']
compare_author = False
way_to_file = "main/example/output/book.csv"
way_to_folder = r'main/example/multiple_example'
columns_names = ['Author', 'Title',
                 'Lexical diversity', 'Mean word len', 'Mean sentence len', 'Commas per 1000 symbols']
if __name__ == '__main__':
    list_of_files = listdir(way_to_folder)
    out_file = open(way_to_file, 'w', encoding='utf-8')
    writer = csv.writer(out_file)
    writer.writerow(columns_names)
    for i in list_of_files:
        book = FictionBookLib.FB2(way_to_folder+'\\'+i)
        if book.GetAuthor() == author or compare_author == False:
            Analysed = TextAnalyzerLib.Analys(book.GetMainText())
            out = book.GetBookTitle()
            print(list(Analysed.GetAll().values()))
            writer.writerow([book.GetAuthor()[0]+' ' + book.GetAuthor()
                             [1], book.GetBookTitle()]+list(Analysed.GetAll().values()))
    out_file.close()
