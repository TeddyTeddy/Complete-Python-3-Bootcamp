# (3) is a generator expression utilized
squares = (x * x for x in range(1, 10))  # a generator expression is a generator
print(type(squares))  # <class 'generator'>
print(list(squares))  # squares -> a generator -> is an iterator -> an iterable


# (4): how (3) can be implemented using a generator function
def squares():  # a generator function
    for x in range(1, 10):
        yield x * x
    pass  # when execution reaches this imaginary point, Python will raise a StopIteration error


print(type(squares))  # <class 'function'>
lst = []
for square in squares():
    lst.append(square)
print(lst)
