module: python

namespace: top_level

srcs:
- ptpython/validator.py
- ptpython/key_bindings.py
- ptpython/prompt_style.py
- ptpython/style.py
- ptpython/layout.py
- ptpython/repl.py
- ptpython/__init__.py
- ptpython/eventloop.py
- ptpython/completer.py
- ptpython/contrib/__init__.py
- ptpython/contrib/asyncssh_repl.py
- ptpython/ipython.py
- ptpython/utils.py
- ptpython/lexer.py
- ptpython/history_browser.py
- ptpython/entry_points/__init__.py
- ptpython/entry_points/run_ptipython.py
- ptpython/entry_points/run_ptpython.py
- ptpython/__main__.py
- ptpython/filters.py
- ptpython/python_input.py

depends:
- tp/libs/prompt_toolkit
- tp/libs/pygments
- tp/libs/jedi
