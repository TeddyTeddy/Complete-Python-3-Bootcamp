print('------------ sa2.py begins --------------------------')
import sys
print(f'packA.subA.sa2.py: with __name__: {__name__}')   # __name__ is 'sa2'
print(f'packA.subA.sa2.py: with sys.path (shared across all imported modules): {sys.path}')
print('------------ sa2.py ends --------------------------')