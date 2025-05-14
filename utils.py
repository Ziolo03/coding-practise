"""Module providing basic calculator operations."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b."""
    return a / b


def to_binary(n):
    if not isinstance(n, int):
        raise TypeError("Input must be a natural number")
    if not (0 <= n <= 100):
        raise ValueError("Number must be between 0 and 100")
    return bin(n)
