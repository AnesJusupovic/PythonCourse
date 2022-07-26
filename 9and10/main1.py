if __name__ == "__main__":
    programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                              "Function": "A piece of code that you can easily call over and over again."}

    #Retriebing items from dictionary
    print(programming_dictionary["Bug"])

    #Adding new items to dictionary
    programming_dictionary["Loop"] = "The action of doing something over and over again."
    print(programming_dictionary)

    empty_dictionary = {}