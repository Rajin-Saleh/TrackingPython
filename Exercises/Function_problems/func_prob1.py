def greatest(a, b, c):
    if a > b and a > c:
        print(f"Greatest {a}")
    elif b > a and b > c:
        print(f"Greatest {b}")
    else:
        print(f"Greatest {c}")


greatest(1, 2, 3)
