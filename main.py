import pandas


# Create a list of the phonetic code words from a word that the user inputs
def spell_word():
    user_word = input("What word would you like to convert? ").upper()
    try:
        word_nato_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Only letters in the alphabet, please.")
        spell_word()
    else:
        print(word_nato_list)


# Import nato alphabet csv
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# Spell the word using the phonetic alphabet
spell_word()
