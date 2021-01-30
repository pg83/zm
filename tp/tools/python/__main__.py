def old():
    import code

    code.interact(local=locals())

from ptpython.repl import embed

embed(globals(), locals())
