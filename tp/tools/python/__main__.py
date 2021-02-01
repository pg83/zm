import code
from ptpython.repl import embed

def old():
    code.interact(local=locals())

embed(globals(), locals())
