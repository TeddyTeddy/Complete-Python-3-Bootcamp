import module_b
import module_a  # note that module_b has already imported module_a, x is already initialized to 1 there


if __name__ == '__main__':
    print(f'main.py has also imported module_a. The value of x in module_a is {module_a.print_x()}')
