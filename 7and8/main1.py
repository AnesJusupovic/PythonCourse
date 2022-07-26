def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today?")

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

if __name__ == "__main__":
    greet()
    greet_with_name("Billie")