def gencomp2(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:  # no StopIteration error
            if item > 3:
                yield item


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    gencomp = (item for item in my_list if item > 3) # gencomp2 is what happens in the background
    for item in gencomp:
        print(item)

    for item in gencomp2(my_list):
        print(item)