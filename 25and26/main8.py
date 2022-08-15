if __name__ == "__main__":
    sentence = input("Please write a sentence:\n").split(" ")
    result = {word:len(word) for word in sentence}
    print(result)