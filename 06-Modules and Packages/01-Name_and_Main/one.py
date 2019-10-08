def func():
    print("func() ran in one.py")


print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print(f'one.py is being imported into another module. __name__ is {__name__}')
