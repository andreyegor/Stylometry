# Stylometry
Этот проект предназначен для проведения стилометрического анализа
## Работа
### Запуск
Для запуска  скачайте исполняемый файл для windows из [releases](https://github.com/andreyegor/Stylometry/releases) или используйте файл Start.py, предваритеьно установив библиотеки nltk, string, matplotlib
Во время первого запуска введите $download, так вы установите компоненты NLTK
Введите $help, для того, чтобы посмотреть возможные команды, которые продублированы здесь
### Возможности
##### Функции
$help - помощь
$download - установить компоненты nltk
$analysis m - проанализировать 1 файл
$analysis p - проанализировать 1 файл по частям
$analysis f - проанализировать все файлы в папке
$analysis pf - проанализировать все файлы в папке по частям
##### Вас могут попросить ввести дополнительную информацию, например путь к файлу, или выбрать модификаторы
###### Propertys:
Можно ничего не вводить
'-f' - сохранить в файл (analysis m или analysis f)
'-s - изменить коичество предожений в блоке (analysis p или analysis pf)
###### Analyzed propertys(analysis p или analysis pf):
Если ничего не вводить, будет выбрано '-ld'
'-ld' - lexical divercity (лексическое разнообразие)
'-mw' - mean word len (средня длинна слова)
'-ms' - mean sentence len (средняя длинна предложения)
'-cs' - commas per symbols (количество запятых на 1000 символов)


## textanalyzerlib
Это небольшая библиотека для стилометрического анализа текста
Для работы требуется NLTK и string
punkt_download() - Просто скачивает компоненты NLTK
### Класс analys
n = analys(ваш текст, quantity_symbols=количество символов в блоке, full_analyze = True)
full_analyze - анализирует текст по всем параметрам, если True
full_parse - анализирует текст по всем параметрам (не нужен, если full_analyze == True)
##### Получают соответствующие параметры
get_tokens()
get_sentences()
get_lexical_devercity()
get_mean_word_len()
get_mean_sentence_len()
get_commas_per_symbols()
get_all()





