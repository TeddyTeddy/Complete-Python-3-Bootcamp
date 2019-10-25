class MyListIter:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def __iter__(self):  # an iterator always is a iterable
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            value = self.my_list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


class MyList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, item):  # to make MyList index-able
        return self.lst.__getitem__(item)

    def __iter__(self):
        return MyListIter(self)  # returns an iterator which has its own class


if __name__ == '__main__':
    my_list = MyList([1, 2, 3])  # an iterable
    iterator = iter(my_list)    # iterable returns an iterator

    iterator2 = iter(iterator)  # an iterator is also an iterable
    print(iterator == iterator2)

    print(iterator)             # <__main__.MyListIter object at 0x7fc7aa139390>
    print(next(iterator))       # 1
    print(next(iterator))       # 2
    print(next(iterator))       # 3
    print(next(iterator))       # StopIteration error


