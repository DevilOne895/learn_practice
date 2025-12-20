def del_elem():

    print("____________________________________________________________________________________")
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Только цифры давай")
        return
    list_of_numbers = []

    for i in numbers:
        digit = int(i)
        list_of_numbers.append(digit)


    result = []
    for number in list_of_numbers:
        if number not in result:
            result.append(number)

    print("____________________________________________________________________________________")
    print("ВОТ ВАШ РЕЗУЛЬТАТ: ")
    print(result)
    print("____________________________________________________________________________________")


def max_min_sum():

    print("____________________________________________________________________________________")
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Только цифры давай")
        return
    list_of_elem = []

    for i in numbers:
        digit = int(i)
        list_of_elem.append(digit)
        n = sorted(list_of_elem)

    print("____________________________________________________________________________________")
    print(f"\n Самый маленький елемент: {n[0]} \nСамый большой елемент {n[-1]} ")
    print(f"\n Сумма всех елементов: ", sum(n))
    print("____________________________________________________________________________________")



def shift():

    print("____________________________________________________________________________________")
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Только цифры давай")
        return
    print("____________________________________________________________________________________")
    tern = input("Введите число сдвига: ")
    if not numbers.isdigit():
        print("Только цифры давай")
        return
    list_of_num = []

    for i in numbers:
        digit = int(i)
        list_of_num.append(digit)
        x = list_of_num.pop()
        list_of_num.insert(0, x)

    print("____________________________________________________________________________________")
    print("ВОТ ВАШ РЕЩУЛЬТАТ")
    print(list_of_num)
    print("____________________________________________________________________________________")



def even_odd_count():

    print("____________________________________________________________________________________")
    n = int(input("Введите числа: "))
    n = str(n)
    if not n.isdigit():
        print("Только цифры давай")
        return
    even = 0
    odd = 0
    for lol in str(n):
        if int(lol) % 2 == 0:
            odd += 1
        else:
            even += 1

    print("____________________________________________________________________________________")
    print("ВОТ ВАШ РЕЗУЛЬТАТ")
    print (f" \n Четные числа {odd},Не четыне числа {even}")
    print("____________________________________________________________________________________")




def temperature():
    temperatures = []
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    print("____________________________________________________________________________________")
    for i in range(len(days)):
        temp = int(input(f"Введите температуру за {days[i]}: "))
        temperatures.append(temp)
        print(f"\n{days[i]}: {temperatures[i]}°C")

    max_temp = max(temperatures)
    max_day = days[temperatures.index(max_temp)]
    print("____________________________________________________________________________________")
    print("Максимальная температура:", max_day, max_temp ,"°C")

    average_temp = sum(temperatures) / len(temperatures)
    print("Средняя температура:", int(average_temp),"°C")
    print("____________________________________________________________________________________")


