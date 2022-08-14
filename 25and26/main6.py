import pandas

if __name__ == "__main__":
    data = []
    data1 = []
    with open("file1.txt") as file:
        data = file.readlines()
    with open("file2.txt") as file1:
        data1 = file1.readlines()
    for check in data:
        check.replace("\n", "")
    for check in data1:
        check.replace("\n", "")
    print(data)
    print(data1)
    new_list = []
    for now in data:
        new_list.append([int(same) for same in data1 if same == now])
    list_new = pandas.DataFrame(new_list)
    list_new.to_csv("new_list_csv")
