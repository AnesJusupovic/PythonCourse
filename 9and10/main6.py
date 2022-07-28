#Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Empty"
    return f_name.title() + " " + l_name.title()

if __name__ == "__main__":
    print(format_name("Marvin", "Goldman"))