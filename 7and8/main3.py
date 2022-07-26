import math


def paint_calc(height, width, cover):
    print(math.ceil((height * width) / cover))

if __name__ == "__main__":
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = int(input("Coverage of wall: "))
    paint_calc(test_h, test_w, coverage)