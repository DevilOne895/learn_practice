#_______________________First-LEVEL_____________________________________
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


#_______________________Fourth-LEVEL_____________________________________
task = [1, 2, [], [3, 4], [5]]
cont = 0

def deep_sum(task):
    if not isinstance(task, list):
        return task
    if task == []:
        return 0
    else:
        return deep_sum(task[0]) + deep_sum(task[1:])



#print(deep_sum(task))

def rec(lst, count, max_count):
    input(f"rec({lst},{count},{max_count})")
    # Базовый случай: пустой список (rec([], Count, MaxCount))
    if not lst:
        return count - 1, max_count

    # Разделение на голову (H) и хвост (T)
    h = lst[0]
    t = lst[1:]

    # Первый паттерн: голова является списком (when is_list(H))
    if isinstance(h, list):
        # Логика case: проверяем, увеличилась ли глубина
        if count + 1 > max_count:
            # Новый виток с обновленным максимумом
            _, max_count1 = rec(h, count + 1, count + 1)
        else:
            # Новый виток со старым максимумом
            _, max_count1 = rec(h, count + 1, max_count)

        # Рекурсия для хвоста с обновленным max_count1
        return rec(t, count, max_count1)

    # Второй паттерн: голова не список (rec([_H|T]...))
    else:
        return rec(t, count, max_count)


# Пример использования (обертка для запуска)
def get_max_depth(lst):
    # Начальные значения: Count=1, Max=1 (как в комментариях Erlang кода)
    _, max_depth = rec(lst, 1, 1)
    return max_depth


# Тесты
data = [2, [4, [5]]]  # Глубина 3
#print(get_max_depth(data))  # Вывод: 3



binary_list = [1,4,22,44,54,2,5,6,88,0,23]
def recurs_binary_search(binary_list, number):
    if not binary_list:
        return "Похоже, вашего числа нету в списке!"

    sorted_task = sorted(binary_list)
    mid = len(sorted_task) // 2
    mid_value = sorted_task[mid]

    if mid_value == number:
        return "Ваше число есть в списке!"
    elif number < mid_value:
        return recurs_binary_search(sorted_task[:mid], number)
    else:
        return recurs_binary_search(sorted_task[mid+1:], number)



print(recurs_binary_search(binary_list, 45))
