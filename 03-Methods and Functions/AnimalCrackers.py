# TASK
# ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(two_word_string):
    words = two_word_string.lower().split()  # ['Levelheaded', 'Llama']
    if words[0][0] == words[1][0]:
        return True
    return False


print(f'animal_crackers("Levelheaded Llama"): {animal_crackers("Levelheaded Llama")}')
print(f'animal_crackers("Crazy Kangaroo"): {animal_crackers("Crazy Kangaroo")}')
print(f'animal_crackers("Crazy cat"): {animal_crackers("Crazy cat")}')
