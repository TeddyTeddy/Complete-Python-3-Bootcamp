def myfunc(string):
    result = []
    for i,letter in enumerate(string):
        if i % 2 == 0:  # every odd letter is lowercase
            result.append(letter.lower())
        else:           # every even letter is uppercase
            result.append(letter.upper())

    return ''.join(result)

