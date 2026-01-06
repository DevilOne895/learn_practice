def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)

def numbers(n):
    if n <= 0:
        return
    numbers(n - 1)
    print(n)


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

#print(sum(5))


def digits(n):
        if n == 0:
            return 0
        return 1 + digits(n // 10)


print(digits(12345))
