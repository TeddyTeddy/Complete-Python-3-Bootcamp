# TASK
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'


def old_macdonald(name):
    length = len(name)
    result = ''
    if length == 0:  # do nothing if empty string
        pass
    elif length < 4:  # if length is from 1 to 3
        result = name.capitalize()
    else:  # if length is greater than or equal to 4
        result = name[0].capitalize() + name[1:3] + name[3].capitalize() + name[4:]

    return result


print(f'old_macdonald(""): {old_macdonald("")}')  # pass an empty string
print(f'old_macdonald("mac"): {old_macdonald("mac")}')
print(f'old_macdonald("macd"): {old_macdonald("macd")}')
print(f'old_macdonald("macdo"): {old_macdonald("macdo")}')
print(f'old_macdonald("macdonald"): {old_macdonald("macdonald")}')
