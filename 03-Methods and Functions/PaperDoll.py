#TASK
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(string):
    result = []
    for letter in list(string):
        result.extend([letter]*3)
    result = ''.join(result)
    return result


print(f'paper_doll("Hello"): {paper_doll("Hello")}')
print(f'paper_doll("Mississippi"): {paper_doll("Mississippi")}')
print(f'paper_doll(""): {paper_doll("")}')