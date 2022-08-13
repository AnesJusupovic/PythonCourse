if __name__ == "__main__":
    numbers = [1, 2, 3]
    new_list = [n+1 for n in numbers]
    print(new_list)
    name = "Angela"
    letters_list = [letter for letter in name]

    test_range = range(1, 5)
    new_numbers = [number*2 for number in test_range]
    print(new_numbers)

    names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
    print(names)
    new_names = [name_new for name_new in names if len(name_new) < 5]
    print(new_names)
    new_names2 = [name_new.upper() for name_new in names if len(name_new) > 5]
    print(new_names2)