def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

if __name__ == "__main__":
    test_values = [1, 2, 3, 5]
    expected = [1, 2, 6, 120]
    for n, exp in zip(test_values, expected):
        assert factorial(n) == exp, f"{factorial(n)} != {exp}"
        print(f"success")
