import functions


def inputs():
    way_to_file = input('Please write way to file: ').lower()
    propertys = input('Please write propertys: ').lower().split()
    return(way_to_file, propertys)


def ReturnAnalysisView():
    way_to_file, propertys = inputs()
    kwargs = {'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    if '-f' in propertys:
        kwargs['in_file'] = True
        if '-n' in propertys:
            kwargs['new'] = True
        file_name = input('Please write file name: ')
        if '.' not in file_name:
            file_name = file_name + '.csv'
    functions.ReturnAnalysis(way_to_file, **kwargs)


def ReturnAnalysisPartsView():
    way_to_file, propertys = inputs()
    kwargs = {'sentences_in_block': 150}
    if '-s' in propertys:
        kwargs['sentences_in_block'] = int(input(
            'Please write number of sentences in block: '))
    functions.ReturnAnalysisParts(way_to_file, **kwargs)


def ReturnAnalysisFolderView():
    way_to_file, propertys = inputs()
    kwargs = {'check_author': False,
              'author': ['name', 'surname'],
              'in_file': False,
              'file_name': 'default.csv',
              'new': True}
    if '-f' in propertys:
        kwargs['in_file'] = True
        if '-n' in propertys:
            kwargs['new'] = True
        file_name = input('Please write file name: ')
        if '.' not in file_name:
            file_name = file_name + '.csv'
    if '-c' in propertys:
        kwargs['check_author'] = True
        kwargs['author'][0] = input('Please write author name: ')
        kwargs['author'][1] = input('Please write author surname: ')
    functions.ReturnAnalysisFolder(way_to_file, **kwargs)


def ReturnAnalysisPartsFolderView():
    way_to_file, propertys = inputs()
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
    if '-s' in propertys:
        kwargs['sentences_in_block'] = int(input(
            'Please write number of sentences in block: '))
    if '-f' in propertys:
        kwargs['in_file'] = True
        if '-n' in propertys:
            kwargs['new'] = True
        file_name = input('Please write file name: ')
        if '.' not in file_name:
            file_name = file_name + '.csv'
    if '-c' in propertys:
        kwargs['check_author'] = True
        kwargs['author'][0] = input('Please write author name: ')
        kwargs['author'][1] = input('Please write author surname: ')
    for t in propertys:
        if t in props.keys():
            kwargs['prop'] = props[t]
    functions.ReturnAnalysisPartsFolder(way_to_file, **kwargs)


COMMANDS_FUNCTIONS = {
    'analysis m': ReturnAnalysisView,
    'analysis p': ReturnAnalysisPartsView,
    'analysis f': ReturnAnalysisFolderView,
    'analysis pf': ReturnAnalysisPartsFolderView
}
