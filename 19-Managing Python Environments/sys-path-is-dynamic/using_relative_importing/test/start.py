print('-------------- start.py begins ------------------------')
import sys
print(f'start.py: with __name__: {__name__}')   # __name__ is main
print(f'start.py: with sys.path (shared across all imported modules): {sys.path}')
from packA import a2
print('--------------- start.py ends -------------------------')