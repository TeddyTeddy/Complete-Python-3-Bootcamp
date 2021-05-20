import sys
print(f'my-package a.py: with __name__: {__name__}')   # __name__ = mypackage.a
print(f'my-package a.py: with sys.path (shared across all imported modules): {sys.path}')
print('--------------------------------------')

def module_a_function():
	print('module_a_function() got called')