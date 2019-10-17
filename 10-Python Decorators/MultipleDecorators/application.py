import multiple_decorators

# app_func = multiple_decorators.decorator_two(app_func)
@multiple_decorators.decorator_two
def app_func(*args, **kwargs):
    print(f'I am a function from main app. I need decorating. My args: {args}, my kwargs: {kwargs}')


if __name__ == '__main__':
    app_func(1, 2, fruit='banana', juice='Orange juice')
