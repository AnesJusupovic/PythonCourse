def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if __name__ == "__main__":
    #age: int
    #name: str
    #height: float
    #is_human: bool

    if police_check(19):
        print("You may pass")
    else:
        print("Pay a fine.")
