"""
Intro to writing better python code.

Topics:
    1. Imports
    2. Using a main function
    3. Comprehension and generator expressions
    4. Default argument values
    5. Typing
    6. Properties
    7. Getters and setters
    8. Lexical scoping
    9. Exception handling
"""

from my_package import main as my_package_name
from my_package.main import NumberTooSmall, NumberTooBig


def foo():
    print("Hola mundo")
    return 70


def main():
    """
    for (int i = 0; i < algo; i++) {
        arr[i] = // asignamos algo
    }
    """
    elements = ["Martin", "Rodrigo", "Topi", "TheDelphin"]

    # print({
    #     element: my_package_name.sum_numbers(len(element), 101)
    #     for element in elements
    # })
    for el in elements:
        try:
            if el == "Topi":
                print(my_package_name.sum_numbers(len(el), 101))
            elif el == "Rodrigo":
                print(my_package_name.sum_numbers(len(el), -101))
            else:
                print(my_package_name.sum_numbers(len(el)))
        except NumberTooBig:
            print("Algo salió mal")
        except NumberTooSmall:
            print("Otra cosa salió mal")


if __name__ == "__main__":
    main()
