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


def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)

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

#print(degree(5))

#_______________________THIRD-LEVEL_____________________________________

massive = [12, 33, 45, 12, 22, 43]
def sum_massive(massive):
    if massive == []:
        return 0
    return massive[0] + sum_massive(massive[1:])

#print(sum_massive(massive))

def max_element(massive):
    if len(massive) == 1:
        return massive[0]
    first = massive[0]
    maximum = max_element(massive[1:])
    if massive[0] > maximum:
        return massive[0]
    else:
        return maximum

#print(max_element(massive))

def is_massive_sort(massive):
    if len(massive) <= 1:
        return True
    if massive[0] > massive[1]:
        return False
    return is_massive_sort(massive[1:])


#print(is_massive_sort(massive))

def count_elements_of_massive(massive):
    if massive == []:
        return 0
    return 1 + count_elements_of_massive(massive[1:])

#print(count_elements_of_massive(massive))

def recursion_search(massive):
    answer = int(input("Введите число которое надо найти: "))
    if massive == []:
        return False
    elif massive[0] == answer:
        return massive[0],print("Ваш елемент есть в списке!")
    elif massive[0] != answer:
        print("Такого елемента нету в списке!(")
    else:
        return recursion_search(massive[1:])

#print(recursion_search(massive))