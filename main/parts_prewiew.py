
import FictionBookLib
import TextAnalyzerLib

way_to_document = r'main/example/example.fb2'
sentences_in_block = 100


def MergeList(list):
    out = ''
    for val in list:
        out += val + ' '
    return out


if __name__ == '__main__':
    book = FictionBookLib.FB2(way_to_document)
    analysed = TextAnalyzerLib.Analys(book.GetMainText(), full_analyze=False)
    sentences = analysed.GetSentences()
    qwantity_sentences = len(sentences)
    sentences_blocks = sentences[0:qwantity_sentences //
                                 sentences_in_block * sentences_in_block]
    properties = []
    for i in range((len(sentences_blocks)//sentences_in_block)-1):

        analysed_block = TextAnalyzerLib.Analys(
            MergeList(
                sentences_blocks[sentences_in_block*i:sentences_in_block*(i+1)]))
        properties.append(analysed_block.GetAll())
        print('█', end='')
    print(properties)
