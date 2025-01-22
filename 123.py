import random
import string

def create_nested_list(rows, cols):
    nested_list = []


    for _ in range(rows):
        row = [random.choice(string.ascii_uppercase) for _ in range(cols)]
        nested_list.append(row)
        return nested_list


def print_nested_list(nested_list):
    for row in nested_list:
        print(row)

def main():
    rows = int(input('Input amount of rows'))
    cols = int(input('Input amount of cols'))

    nested_list = create_nested_list(rows, cols)

    print(("Nested list: "))
    print_nested_list(nested_list)

if __name__ == '__main__':
    main()