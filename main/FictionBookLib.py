import xml.dom.minidom


class FB2:
    author = [None, None]
    main_text = None
    book_title = None

    def __init__(self, way_to_document, full_parse=True):
        """
        Сlass for get main information for a document. "Parse" functions are needed to parse some document properties. "Get" functions are needed to get this propertiers. 

        Args:
            way_to_document (string): Way to you fb2 document
            full_parse (bool, optional): True for full document parsing, False for manual parsing. Defaults to True.
        """

        self.way_to_document = way_to_document
        self.parsed_document = xml.dom.minidom.parse(self.way_to_document)
        self.parsed_document.normalize()
        if full_parse:
            self.ParseDocument()

    def ParseDocument(self):
        """This is a function to full document parse"""
        self.ParseAuthor()
        self.ParseBookTitle()
        self.ParseMainText()
        self.ParseMainText()

    def ParseAuthor(self):
        out = [None, None]
        out[0] = self.parsed_document.getElementsByTagName(
            "first-name")[0].childNodes[0].nodeValue
        out[1] = self.parsed_document.getElementsByTagName(
            "last-name")[0].childNodes[0].nodeValue
        self.author = out
        return out

    def ParseBookTitle(self):
        out = self.parsed_document.getElementsByTagName(
            "book-title")[0].childNodes[0].nodeValue
        self.book_title = out
        return out

    def ParseMainText(self):
        p_nodes = self.parsed_document.getElementsByTagName("p")
        out = ""
        for i in range(len(p_nodes)):
            sentence = str(p_nodes[i].childNodes[0].nodeValue)
            if sentence != "None":
                out += sentence + " "
        self.main_text = out
        return out

    def GetMainText(self):
        """ None, if you don't parse main text"""
        return self.main_text

    def GetAuthor(self):
        """ [None, None], if you don't parse author"""
        return self.author

    def GetBookTitle(self):
        """ None, if you don't parse book title"""
        return self.book_title
