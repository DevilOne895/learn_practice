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


#print(digits(12345))


#_______________________SECOND-LEVEL_____________________________________

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

#print(factorial(5))


def pow(a,n):
    if n == 1:
        return 1
    return a * pow(a,n - 1)

#print(pow(2,4))

def sumDigits(n):
    if n == 0:
        return 0
    return sumDigits(n // 10) + n % 10

#print(sumDigits(123))

def degree(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return degree(n // 2 )

print(degree(5))