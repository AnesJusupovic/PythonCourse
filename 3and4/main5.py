if __name__ == "__main__":
    states_of_america = ["Delaware", "Pennsylvania"]
    states_of_america[1] = "Pencilvania"

    print(states_of_america)
    states_of_america.append("Angelaland")
    print(states_of_america)

    states_of_america.extend(["Jack Bauer Land", "Anes Land"])
    print(states_of_america)