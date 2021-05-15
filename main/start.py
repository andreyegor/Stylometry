import re

import functions


def inputs(path_to='файлу'):
    way_to_file = str(
        input('Пожалуйста введите путь к ' + path_to + ' : ')).lower()
    propertys = str(input('Please write propertys: ')).lower().split()
    return(way_to_file, propertys)


def help_me():
    help_text = """Если вы используете это впервые, введите $download
Функции:
    $help - помощь
    $download - установить компоненты nltk
    $analysis m - проанализировать 1 файл
    $analysis p - проанализировать 1 файл по частям
    $analysis f - проанализировать все файлы в папке
    $analysis pf - проанализировать все файлы в папке по частям
Вас могут попросить ввести дополнительную информацию, например путь к файлу, или выбрать модификаторы.
Свойства:
    '-f' - сохранить в файл (analysis m или analysis f)
    '-s - изменить коичество предожений в блоке (analysis p или analysis pf)
Анализируемые свойства (analysis p или analysis pf):
    '-ld' - lexical divercity (лексическое разнообразие)
    '-mw' - mean word len (средня длинна слова)
    '-ms' - mean sentence len (средняя длинна предложения)
    '-cs' - commas per symbols (количество запятых на 1000 символов)
"""
    print(help_text)
    pass


def analysis_propertys(propertys, kwargs):
    if '-f' in propertys and 'in_file' in kwargs.keys():
        kwargs['in_file'] = True
        if '-n' in propertys and 'new' in kwargs.keys():
            kwargs['new'] = True
        if 'file_name' in kwargs.keys():
            file_name = str(input('Please write file name: '))
            if '.' not in file_name:
                file_name = file_name + '.csv'
            kwargs['file_name'] = file_name
    if '-s' in propertys and 'sentences_in_block' in kwargs.keys():
        kwargs['sentences_in_block'] = int(input(
            'Please write number of sentences in block: '))
    if '-c' in propertys and 'check_author' in kwargs.keys() and 'author' in kwargs.keys():
        kwargs['check_author'] = True
        kwargs['author'][0] = str(input('Please write author name: '))
        kwargs['author'][1] = str(input('Please write author surname: '))


def return_analysis_view():
    way_to_file, propertys = inputs()
    kwargs = {'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    analysis_propertys(propertys, kwargs)
    print('Please wait...')
    functions.return_analysis(way_to_file, **kwargs)


def return_analysis_parts_view():
    way_to_file, propertys = inputs()
    kwargs = {'sentences_in_block': 150}
    analysis_propertys(propertys, kwargs)
    print('Наберитесь терпения...')
    functions.return_analysis_parts(way_to_file, **kwargs)


def return_analysis_folder_view():
    way_to_file, propertys = inputs(path_to='folder')
    kwargs = {'check_author': False,
              'author': ['name', 'surname'],
              'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    analysis_propertys(propertys, kwargs)
    print('Подождите...')
    functions.return_analysis_folder(way_to_file, **kwargs)


def return_analysis_parts_folder_view():
    way_to_file, propertys = inputs(path_to='folder')
    kwargs = {
        'sentences_in_block': 150,
        'check_author': False,
        'author': ['name', 'surname'],
        'prop': 0
    }
    props = {'-ld': 0,
             '-mw': 1,
             '-ms': 2,
             '-cs': 3}
    analysis_propertys(propertys, kwargs)
    p = input('Please analyzed property: ')
    if p in props.keys():
        kwargs['prop'] = props[p]
    print('Ceep calm...')
    functions.return_analysis_parts_folder(way_to_file, **kwargs)


COMMANDS = {
    'analysis m': return_analysis_view,
    'analysis p': return_analysis_parts_view,
    'analysis f': return_analysis_folder_view,
    'analysis pf': return_analysis_parts_folder_view,
    'help': help_me,
    'download': functions.textanalyzerlib.punkt_download
}

if __name__ == '__main__':
    help_me()
    while True:
        command = input()
        if command in COMMANDS.keys():
            try:
                COMMANDS[command]()
            except:
                print('FAILED')
        elif command.lower() == 'exit':
            break
        else:
            print('Такой команды пока что не существует')
