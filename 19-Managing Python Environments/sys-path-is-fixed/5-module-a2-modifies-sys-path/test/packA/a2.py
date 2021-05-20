print('------------ a2.py begins --------------------------')
import sys, os, inspect
print(f'a2.py: with __name__: {__name__}')   # __name__ is '__main__' (if executed) or 'a2' (if imported)
print(f'a2.py: with sys.path (shared across all imported modules, before modification): {sys.path}')

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))  # path to test/
sys.path.insert(0, parent_dir)
print(f'a2.py: with sys.path (shared across all imported modules, after modification): {sys.path}')

from packA.subA import sa2  # absolute import rooted at test/ folder
print('------------ a2.py ends --------------------------')