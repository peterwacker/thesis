"""This code just print even numbers."""

__author__ = "Peter Wacker"


def even_number_print():
    """Prints even numbers."""

    # To avoid an error if user types in a wrong symbol.
    # Convert string into integer.
    while True:
        try:
            n = int(input("Type in the number to which you want to check even \
numbers: "))
            if n <= 0:
                print("\nNumber must be greater than 0!")
                continue

            break

        except:
            ValueError
            print("Wrong input, try again!")
            continue

    for even_number in range(0, n+1):
        # Checks if number is even or not.
        if even_number % 2 == 0:
            print(even_number)

    # To avoid termination of the program in the console.
    input("Press enter to quit!")


def main():
    """Executes the program."""

    even_number_print()


if __name__ == "__main__":
    main()
