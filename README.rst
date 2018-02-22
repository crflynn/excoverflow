excoverflow
===========

This package adds links to google and stackoverflow search results to the end
of uncaught exceptions in Python.

To install:

.. code-block:: shell

    pip install excoverflow

To use, simply import the package in any project file for which you want
internet results pages printed after the exception.

.. code-block:: python

    import excoverflow

Unhandled exception output will be appended with links to google and
stackoverflow search results for python, the exception type, and the
exception message; e.g.

.. code-block:: shell

    Traceback (most recent call last):
      File "test.py", line 5, in <module>
        val = 5 / 0
    ZeroDivisionError: division by zero

    https://www.google.com/search?q=python+ZeroDivisionError+division+by+zero
    https://stackoverflow.com/search?q=%5Bpython%5D+%22ZeroDivisionError+division+by+zero%22
