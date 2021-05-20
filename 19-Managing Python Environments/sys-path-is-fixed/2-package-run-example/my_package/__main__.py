import my_package.a as a
import my_package.b as b
import sys
print(f'my-package __main__.py: with __name__: {__name__}')  # __name__ = my_package
print(f'my-package __main__.py: with sys.path (shared across all imported modules): {sys.path}')
print('--------------------------------------')

package_variable = 'package variable text'
def package_function():
	print('package function got called')
	a.module_a_function()
	b.module_b_function()

if __name__ == '__main__':
	print(package_variable)
	package_function()