def ask_int():
    while True:
        try:
            value = int(input('Enter an integer: '))
        except:
            print('An error occured! Please try again!')
            continue
        else:
            print(f'Thank you. Your number squared is {value**2}')
            break


if __name__ == '__main__':
    ask_int()
