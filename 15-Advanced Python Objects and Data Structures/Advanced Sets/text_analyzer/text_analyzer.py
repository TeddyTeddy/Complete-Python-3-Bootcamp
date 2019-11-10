# CHALLENGE: Create a program that takes some text and returns a list of all the characters in the text that \
# are not vowels, and sorted in the alphabetical order

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
       'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
       'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse ' \
       'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in ' \
       'culpa qui officia deserunt mollit anim id est laborum.'

vovels_and_rubbish = {'a', 'e', 'i', 'o', 'u', ' ', '.', ','}
all_the_characters_in_text = set([*text])
difference = all_the_characters_in_text.difference(vovels_and_rubbish)
result = sorted(difference)
print(result)
