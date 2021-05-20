import my_package.a as a  # The first time that a package OR one of its modules is imported,
						  # Python will import the __init__.py file in the root folder of the package if the file exists (*)
import my_package.b as b
# from my_package import b
# (*) import my_package    # as if this one was here
import sys
print(f'my-package __main__.py: with __name__: {__name__}')  # __name__ = '__main__'
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