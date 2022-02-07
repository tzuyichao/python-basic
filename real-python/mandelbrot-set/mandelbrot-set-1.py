
def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n-1, c) ** 2 + c


if __name__ == '__main__':
    for n in range(10):
        print(f"z({n}) = {z(n, c=1)}")