import pandas

if __name__ == "__main__":
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    # Loop through rows of a data frame
    dict = {}
    for (index, row) in data.iterrows():
        dict[row.letter] = row.code
    print(dict)
    name = input("What is your name: \n")
    for char in name:
        fill = dict[char]
        print(f"{char} as {fill}")
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
