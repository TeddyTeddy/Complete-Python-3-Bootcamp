"""
Let’s recap the order in which Python searches for modules to import:

1) built-in modules from the Python Standard Library (e.g. sys, time)
2) modules or packages in a directory specified by sys.path:
   a) If the Python interpreter is run interactively, sys.path[0] is the empty string ''.
   This tells Python to search the current working directory from which you launched the interpreter,
   i.e., the output of pwd on Unix systems.

   b) If we run a script with python <script>.py, sys.path[0] is the path to <script>.py.

   c) directories in the PYTHONPATH environment variable
   d) default sys.path locations, including remaining Python Standard Library modules which are not built-in
   f) Virtual environment path
"""

print('Case 1: sys.path is fixed/known ahead of time')
print('In this example, only start.py needs to be invoked via python -m start (The other modules are only imported but not invoked)')
print('sys.path will always include the path to start.py in its search path')
print('Therefore, all of the import statements can be written relative to the start.py s path')
print('--------------------------------------')
import sys
print(f'start.py: with __name__: {__name__}')   # __name__ is main
print(f'start.py: with sys.path (shared across all imported modules): {sys.path}')
print('--------------------------------------')
import my_package   # equivalent to import my_package.__init__
print(my_package.package_variable)
my_package.package_function()

