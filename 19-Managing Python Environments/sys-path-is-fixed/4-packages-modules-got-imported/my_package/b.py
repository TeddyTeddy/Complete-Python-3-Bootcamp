import sys
print(f'my-package b.py: with __name__: {__name__}')	# __name__ = mypackage.a
print(f'my-package b.py: with sys.path (shared across all imported modules): {sys.path}')
print('--------------------------------------')

def module_b_function():
	print('module_b_function() got called')