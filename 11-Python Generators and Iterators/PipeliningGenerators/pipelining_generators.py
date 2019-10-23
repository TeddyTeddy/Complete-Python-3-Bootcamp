with open('sells.log') as file:
    pizza_col = (line.split(' ')[3] for line in file)  # line is a str
    per_hour = (int(x) for x in pizza_col if x != 'N/A\n')
    print("Total pizzas sold = ", sum(per_hour))  # sum accepts an iterable
