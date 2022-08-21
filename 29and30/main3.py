

if __name__ == "__main__":
    fruits = ["Apple", "Pear", "Orange"]


    # TODO: Catch the exception and make sure the code runs without crashing.
    def make_pie(index):
        try:
            fruit = fruits[index]
            print(fruit + " pie")
        except IndexError:
            print("The index is out of bounds")
        else:
            print("Success")

    make_pie(4)