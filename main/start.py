import re

import functions


def inputs(way_to='file'):
    way_to_file = str(input('Please write path to ' + way_to + ' : ')).lower()
    propertys = str(input('Please write propertys: ')).lower().split()
    return(way_to_file, propertys)


def help_me():
    help_text = """If you are using this for the first time use the $download
Functions:
    $analysis m - analysis one file
    $analysis p - analysis many parts from one file
    $analysis f - analysis files in folder
    $analysis pf - analysis many parts from files in folder
Propertys:
    '-f' - save in file (analysis m or analysis f)
    '-s - chainge sentences in part (analysis p or analysis pf)
Analyzed propertys(analysis p or analysis pf):
    '-ld' - lexical divercity
    '-mw' - mean word len
    '-ms' - mean sentence len
    '-cs' - commas per symbols
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
    print('Please wait...')
    functions.return_analysis_parts(way_to_file, **kwargs)


def return_analysis_folder_view():
    way_to_file, propertys = inputs(way_to='folder')
    kwargs = {'check_author': False,
              'author': ['name', 'surname'],
              'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    analysis_propertys(propertys, kwargs)
    print('Please wait...')
    functions.return_analysis_folder(way_to_file, **kwargs)


def return_analysis_parts_folder_view():
    way_to_file, propertys = inputs(way_to='folder')
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
    print('Please wait...')
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
    print("You can use $help")
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
            print('No such command')
