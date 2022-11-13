"""
This program demonstrates how to use an addition function.

"""


def addition(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total


def main():
    answer = addition(12, 21, 5, 3, 42, 33, 7, 8, 13)
    print(answer)


if __name__ == "__main__":
    main()
