import pandas as pd

# Method 1: create a dict to store letter and word
# with open('nato_phonetic_alphabet.csv') as nato_file:
#     new_dict = {(blabla.strip()[0]): (blabla.strip()[2:]) for blabla in nato_file.readlines()[1:]}

# Method 2:
df = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input('What is your name?\n').upper()
word_list = [new_dict[letter] for letter in word]
print(word_list)
