from typing import Iterable, Tuple


def calculate_statistics(numbers: Iterable[int]) -> Tuple[int, float, int, int]:
    """Calcula soma, média, maior e menor valor de uma sequência de números."""
    values = list(numbers)
    if not values:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return total, average, maximum, minimum


def display_statistics(numbers: Iterable[int]) -> None:
    total, average, maximum, minimum = calculate_statistics(numbers)
    print("total:", total)
    print("media:", average)
    print("maior:", maximum)
    print("menor:", minimum)


if __name__ == "__main__":
    sample_numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    display_statistics(sample_numbers)
