import xml.dom.minidom


class FB2:
    author = [None, None]
    main_text = None
    book_title = None

    def __init__(self, way_to_document, full_parse=True):
        """
        Класс для получения основной информации о документе "Parse" функции нужны чтобы узнавать конкретные параметры документа "Get" функции нужны для получения этих параметров. 

        Args:
            way_to_document (string): Путь к вашему fb2
            full_parse (bool, optional): True для полного поиска, False для самостоятельного поиска. По умолчанию True.
        """

        self.way_to_document = way_to_document
        self.parsed_document = xml.dom.minidom.parse(self.way_to_document)
        self.parsed_document.normalize()
        if full_parse:
            self.parse_document()

    def parse_document(self):
        """Это функция для полного анализа документа"""
        self.parse_author()
        self.parse_book_title()
        self.parse_main_text()

    def parse_author(self):
        out = [None, None]
        out[0] = self.parsed_document.getElementsByTagName(
            "first-name")[0].childNodes[0].nodeValue
        out[1] = self.parsed_document.getElementsByTagName(
            "last-name")[0].childNodes[0].nodeValue
        self.author = out
        return out

    def parse_book_title(self):
        out = self.parsed_document.getElementsByTagName(
            "book-title")[0].childNodes[0].nodeValue
        self.book_title = out
        return out

    def parse_main_text(self):
        p_nodes = self.parsed_document.getElementsByTagName("p")
        out = ""
        for i in range(len(p_nodes)):
            sentence = str(p_nodes[i].childNodes[0].nodeValue)
            if sentence != "None":
                out += sentence + " "
        self.main_text = out
        return out

    def get_main_text(self):
        """ None, если вы не искали основной текст"""
        return self.main_text

    def get_author(self):
        """ [None, None], если вы не искали автора (в работе)"""
        return self.author

    def get_book_title(self):
        """ None, если вы не искали название книги"""
        return self.book_title
