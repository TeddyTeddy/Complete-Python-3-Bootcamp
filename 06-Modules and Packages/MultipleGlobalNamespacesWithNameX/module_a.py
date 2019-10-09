# x is local to module_a
x = 'a'


def print_x():
    print(f'In module_a, x is {x}')


if __name__ == 'module_a':  # if module_a is imported by main_program.py
    print_x()