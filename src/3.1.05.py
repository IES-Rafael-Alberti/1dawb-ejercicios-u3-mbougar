def make_tuple():
    tuple_num = tuple(i for i in range(1, 101))
    return tuple_num


def print_numbers(tuple_num: tuple, spacer: str = ", "):
    for i in range(-1, -len(tuple_num) -1, -1):
        if i != -len(tuple_num):
            print(tuple_num[i], end=spacer)
        else:
            print(tuple_num[i])


def main():

    numbers = make_tuple()

    print_numbers(numbers)



if __name__ == "__main__":
    main()