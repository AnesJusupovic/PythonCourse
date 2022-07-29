from prettytable import PrettyTable


if __name__ == "__main__":
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])

    table.align = "l"
    print(table)
