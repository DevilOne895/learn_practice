LINE = "═" * 70

def print_header(title):
    print("\n" + LINE)
    print(title.center(70))
    print(LINE)


def del_elem():

    print_header("УДАЛЕНИЕ ПОВТОРЯЮЩИХСЯ ЭЛЕМЕНТОВ")
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("\n⚠ Только цифры давай")
        return
    list_of_numbers = []

    for i in numbers:
        digit = int(i)
        list_of_numbers.append(digit)

    result = []
    for number in list_of_numbers:
        if number not in result:
            result.append(number)

    print_header("РЕЗУЛЬТАТ")
    print(result)
    print(LINE)


def max_min_sum():

    print_header("НАИБОЛЬШИЙ, НАИМЕНЬШИЙ И СУММА")
    numbers = input("Введите числа через пробел: ")

    list_of_elem = []

    for i in numbers.split():
        if not i.isdigit():
            print("\n⚠ Нельзя вводить отрицательные числа или буквы")
            return
        list_of_elem.append(int(i))

    n = sorted(list_of_elem)

    print_header("РЕЗУЛЬТАТ")
    print(f"Самый маленький элемент: {n[0]}")
    print(f"Самый большой элемент: {n[-1]}")
    print(f"Сумма всех элементов: {sum(n)}")
    print(LINE)





def shift():

    print_header("СДВИГ СПИСКА")
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("\n⚠ Только цифры давай")
        return
    print(LINE)
    tern = input("Введите число сдвига: ")
    if not tern.isdigit():
        print("\n⚠ Только цифры давай")
        return
    list_of_num = []

    for i in numbers:
        digit = int(i)
        list_of_num.append(digit)
        x = list_of_num.pop()
        list_of_num.insert(0, x)

    print_header("РЕЗУЛЬТАТ")
    print(list_of_num)
    print(LINE)




def even_odd_count():

    print_header("ПОДСЧЕТ ЧЕТНЫХ И НЕЧЕТНЫХ")
    n = input("Введите числа: ")
    if not n.isdigit():
        print("\n⚠ Только цифры давай")
        return
    even = 0
    odd = 0
    for lol in n:
        if int(lol) % 2 == 0:
            odd += 1
        else:
            even += 1

    print_header("РЕЗУЛЬТАТ")
    print(f"Четные числа: {odd}")
    print(f"Нечетные числа: {even}")
    print(LINE)





def temperature():
    temperatures = []
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    print_header("ВВОД ТЕМПЕРАТУРЫ ЗА НЕДЕЛЮ")
    for i in range(len(days)):
        temp = int(input(f"{days[i]}: "))
        temperatures.append(temp)

    max_temp = max(temperatures)
    max_day = days[temperatures.index(max_temp)]
    average_temp = sum(temperatures) / len(temperatures)

    print_header("РЕЗУЛЬТАТ")
    print(f"Максимальная температура: {max_temp}°C ({max_day})")
    print(f"Средняя температура: {int(average_temp)}°C")
    print(LINE)



