# For '*' and '**' in function calls in decorators:
# https://www.ritchieng.com/python/decorators-kwargs-args/


def decorator_one(original_func):
    def wrapper_func(*args, **kwargs):
        print('Decorator one wrapper executed b4 the original function')
        # '*' in '*args' expands the positional arguments
        # '**' in '**kwargs' expands the keyworded arguments
        original_func(*args, **kwargs)
        print('Decorator one wrapper executed after the original function')
    return wrapper_func


def decorator_two(original_func):
    def wrapper_func(*args, **kwargs):
        print('Decorator two wrapper executed b4 the original function')
        original_func(*args, **kwargs)
        print('Decorator two wrapper executed after the original function')
    return wrapper_func


def decorator_three(original_func):
    def wrapper_func(*args, **kwargs):
        print('Decorator three wrapper executed b4 the original function')
        original_func(*args, **kwargs)
        print('Decorator three wrapper executed after the original function')
    return wrapper_func

# func_needs_decorating = decorator_one(func_needs_decorating)
@decorator_one  # change this to decorator_two or decorator_three
def func_needs_decorating(*args, **kwargs):
    print(f'I need decorating, my args: {args} my kwargs: {kwargs}')


if __name__ == '__main__':
    func_needs_decorating(1, 2, fruit='banana', juice='Orange juice')
