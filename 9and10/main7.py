def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
                return "leap"
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
            return "leap"
    else:
        print("Not leap year.")


def days_in_month(year_p, month_p):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_p) == "leap":
        if month_p == 2:
            return 29
        else:
            return month_days[month_p-1]
    else:
        return month_days[month_p-1]

if __name__ == "__main__":
    # 🚨 Do NOT change any of the code below
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)