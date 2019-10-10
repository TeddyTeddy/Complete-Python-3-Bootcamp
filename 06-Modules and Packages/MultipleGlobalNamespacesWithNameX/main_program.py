from math import pi  # pi is imported directly into main_program's global symbol table! Proof: line 20 and [3]
import module_a      # module_a is added to global symbol table of main_program.py
import module_b      # module_b is added to global symbol table of main_program.py
import module_c      # module_c is added to global symbol table of main_program.py

# x is local to main_program.py
x = 'main'


def print_x():
    print(f'In main_program, x is {x}')


print_x()           # prints: In main_program, x is main
module_a.print_x()  # prints: In module_a, x is a
module_b.print_x()  # prints: In module_b, x is b
module_c.print_x()  # prints: In module_c, x is c

print(pi)           # 3.141592653589793
print(globals())  # { ..., 'pi': 3.141592653589793, ...}
