def print_x():
    return x


if __name__ == 'module_a':  # if module_a is imported
    if 'x' in globals():
        x += 1  # if module_a is imported multiple times, would this code be run from 2.nd importing onwards?
    else:  # x is not in globals()
        x = 1  # module_a is loaded for the first time, initialize it to 1

