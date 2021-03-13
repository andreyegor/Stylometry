import functions


def inputs(way_to='file'):
    way_to_file = str(input('Please write way to ' + way_to + ' : ')).lower()
    propertys = str(input('Please write propertys: ')).lower().split()
    return(way_to_file, propertys)


def helpme():
    pass


def AnalysisPropertys(propertys, kwargs):
    kwargs = kwargs
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


def ReturnAnalysisView():
    way_to_file, propertys = inputs()
    kwargs = {'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    AnalysisPropertys(propertys, kwargs)
    functions.ReturnAnalysis(way_to_file, **kwargs)


def ReturnAnalysisPartsView():
    way_to_file, propertys = inputs()
    kwargs = {'sentences_in_block': 150}
    AnalysisPropertys(propertys, kwargs)
    functions.ReturnAnalysisParts(way_to_file, **kwargs)


def ReturnAnalysisFolderView():
    way_to_file, propertys = inputs(way_to='folder')
    kwargs = {'check_author': False,
              'author': ['name', 'surname'],
              'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    AnalysisPropertys(propertys, kwargs)
    functions.ReturnAnalysisFolder(way_to_file, **kwargs)


def ReturnAnalysisPartsFolderView():
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
    for t in propertys:
        if t in props.keys():
            kwargs['prop'] = props[t]
    AnalysisPropertys(propertys, kwargs)
    functions.ReturnAnalysisPartsFolder(way_to_file, **kwargs)


COMMANDS = {
    'analysis m': ReturnAnalysisView,
    'analysis p': ReturnAnalysisPartsView,
    'analysis f': ReturnAnalysisFolderView,
    'analysis pf': ReturnAnalysisPartsFolderView,
    'help': helpme
}

while True:
    command = input()
    if command in COMMANDS.keys():
        try:
            COMMANDS[command]()
            print('Success!')
        except:
            print('Failed!')
    elif command.lower() == 'exit':
        break
    else:
        print('No such command')
