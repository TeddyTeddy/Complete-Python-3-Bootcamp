# TASK
# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'


def master_yoda(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)


print(f'master_yoda("I am home"): {master_yoda("I am home")}')
print(f'master_yoda("We are ready"): {master_yoda("We are ready")}')
