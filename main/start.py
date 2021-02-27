import functions

commands = {
    'analysis': functions.ReturnAnalysis,
    'analysis -p': functions.ReturnAnalysisParts,
    'analysis -p -f' or 'analysis -p -f': functions.ReturnAnalysisPartsFolder
}
try:
    commands[input()](input())
except:
    print('err')
