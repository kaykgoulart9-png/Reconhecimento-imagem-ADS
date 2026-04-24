def is_prime(number: int) -> bool:
    """Verifica se um número inteiro é primo."""
    if number <= 1:
        return False

    max_divisor = int(number**0.5)
    return all(number % divisor != 0 for divisor in range(2, max_divisor + 1))


if __name__ == "__main__":
    import sys

    try:
        value = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Uso: python num_primos.py <numero>")
    else:
        print(is_prime(value))