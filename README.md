# Stylometry
Этот проект предназначен для проведения стилометрического анализа.
## Работа
### Запуск
Для запуска  скачайте исполняемый файл для windows из [releases](https://github.com/andreyegor/Stylometry/releases) или используйте файл Start.py, предваритеьно установив библиотеки nltk, string, matplotlib.
Во время первого запуска введите $download, так вы установите компоненты NLTK.
Введите $help, для того, чтобы посмотреть возможные команды, которые продублированы здесь.
### Возможности
#### Функции
- help - помощь
- download - установить компоненты nltk
- analysis m - проанализировать 1 файл
- analysis p - проанализировать 1 файл по частям
- analysis f - проанализировать все файлы в папке
- analysis pf - проанализировать все файлы в папке по частям
#### Вас могут попросить ввести дополнительную информацию, например путь к файлу, или выбрать модификаторы
##### Propertys
Можно ничего не вводить
- '-f' - сохранить в файл (analysis m или analysis f)
- '-s - изменить коичество предожений в блоке (analysis p или analysis pf)
##### Analyzed propertys(analysis p или analysis pf)
Если ничего не вводить, будет выбрано '-ld'
- '-ld' - lexical divercity (лексическое разнообразие)\n
- '-mw' - mean word len (средня длинна слова)
- '-ms' - mean sentence len (средняя длинна предложения)
- '-cs' - commas per symbols (количество запятых на 1000 символов)


## textanalyzerlib
Это небольшая библиотека для стилометрического анализа текста.
Для работы требуется NLTK и string.
<punkt_download() # Просто скачивает компоненты NLTK>
### Класс analys
    n = textanalyzerlib.analys('ваш текст', quantity_symbols=1000, full_analyze = True)
- quantity_symbols - количество символов в блоке
- full_analyze - анализирует текст по всем параметрам, если True\
#### Методы
- full_parse() - анализирует текст по всем параметрам (не нужен, если full_analyze == True)
- parse_lexical_divercity() - анализирует текст по лексическому разнообразию
- parse_mean_word_len() - анализирует по средней длинне слова
- parse_mean_sentence_len() - анализирует по средней длинне предложения
- elements_per_characters(element, qwantity) - анализирует частоту использования элемента (element) на количество (qwantity) символов
- parse_commas_per_characters() - анализирует частоту использования запятых на количество (quantity_symbols) символов

##### Просто получают соответствующие параметры
- get_tokens()
- get_sentences()
- get_lexical_devercity()
- get_mean_word_len()
- get_mean_sentence_len()
- get_commas_per_symbols()
- get_all()

## fictionbooklib
Это небольшая библиотека для работы с форматом FB2.
### Класс FB2
    n = fictionbooklib.FB2(way_to_document, full_parse=True)
- way_to_document - путь к вашему файлу .fb2
- full_parse - если True, то полностью парсит докуиент
#### Методы
- parse_author() - получает информацию о авторе (в разработке)
- parse_book_title() - получает  название
- parse_main_text() - получает основной текст
##### Просто получают соответствующие параметры
- get_main_text()
- get_author()
- get_book_title()





