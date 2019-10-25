# decorator function
def show_and_add_vectors(adder_func):
    def wrapper_func(**kwargs):
        for vector in kwargs:  # for each key (i.e. named 'vector') in the dictionary kwargs
            print(f'  {vector}={kwargs[vector]}')
        print('+')
        print('-------------------------')
        result = adder_func(**kwargs)  # adder_func(vector_one=[1, 1, 1], vector_two=[2, 2, 2], vector_three=[3, 3, 3])
        print(f'             {result}')
    return wrapper_func

# add_many_vectors = show_and_add_vectors(add_many_vectors)
@show_and_add_vectors
def add_many_vectors(**kwargs):
    # i.e. kwargs
    # {vector_one:[1, 1, 1], vector_two:[2, 2, 2], vector_three:[3, 3, 3]}
    # make sure that all the vectors have the same length, otherwise we cannot add them
    # if not, throw an error
    vector_length = None
    for vector_key in kwargs:  # for each key (i.e. named 'vector') in the dictionary kwargs
        if vector_length is None:  # if it is the first vector
            vector_length = len(kwargs[vector_key])
        elif vector_length != len(kwargs[vector_key]):
            raise AssertionError  # vectors passed cannot have different lengths for addition purposes

    # if we get to here, that means we have vectors having equal length
    # we can add them via map function
    if vector_length is not None:
        total = [0]*vector_length  # i.e. [0, 0, 0] --> itself a vector
        for vector_key in kwargs:  # for each key (i.e. named as vector) in kwargs
                total = list(map(lambda x,y: x+y, total, kwargs[vector_key]))
    else:  # kwargs did not contain any vectors
        total = []

    return total


if __name__ == '__main__':
    add_many_vectors(vector_one=[1, 1, 1], vector_two=[2, 2, 2], vector_three=[3, 3, 3])
