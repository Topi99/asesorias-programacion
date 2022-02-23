class NumberTooSmall(ValueError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class NumberTooBig(ValueError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def sum_numbers(number_1: float, number_2: float = 10.) -> float:
    if number_2 > 100:
        raise NumberTooBig("Tu número es muy grande")
    if number_2 < 0:
        raise NumberTooSmall("Tu número es muy pequeño")
    return number_1 + number_2


def multiply(number_1: float, number_2: float) -> float:
    return number_1 * number_2


def sum_all(elements: list[float]) -> float:
    result = 0
    for element in elements:
        result += element

    return result
