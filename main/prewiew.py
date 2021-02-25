import FictionBookLib
import TextAnalyzerLib

way_to_document = r"main/example/example.fb2"  # way to fb2 file

if __name__ == '__main__':
    book = FictionBookLib.FB2(way_to_document)
    Analysed = TextAnalyzerLib.Analys(
        book.main_text)  # заменить на Get функцию
    print(str(Analysed.GetLexicalDevercity()*100) + "% - уникальных слов")
    print(str(Analysed.GetMeanWordLen()) + " - средняя длинна слова")
    print(str(Analysed.GetMeanSentenceLen()) +
          " - средня длинна предложения")
    print(str(Analysed.GetCommasPerSymbols()) +
          " - запятых на 1000 символов")
