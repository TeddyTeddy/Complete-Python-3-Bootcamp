print('------------ a2.py begins --------------------------')
import sys
print(f'a2.py: with __name__: {__name__}')   # __name__ is '__main__' (if executed) or 'a2' (if imported)
print(f'a2.py: with sys.path (shared across all imported modules): {sys.path}')
from .subA import sa2
print('------------ a2.py ends --------------------------')