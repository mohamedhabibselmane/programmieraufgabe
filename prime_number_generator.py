def read():
    # input function
    # return an int.
    while True:
        nb = float(input("Please enter a valid number: "))
        if int(nb) == nb and nb >= 2:
            return int(nb)
            break
        else:
            print("**Given number must be a natural number greater than 1.**")


def is_prime(nb):
    # type nb: int
    # return True if nb is a prime number.
    i = 2
    while nb % i != 0:
        i += 1
    return i == nb


def print__(nb):
    # type nb: int
    # print all prime numbers smaller or equal to the input.
    print("Prime numbers smaller or equal to " + str(nb) + ": ")

    for index in range(2, nb + 1):
        if is_prime(index):
            print(index, end=" ")


def main():
    try:
        n = read()
    except ValueError:
        print("Invalid input")
    else:
        print__(n)


if __name__ == '__main__':
    main()
