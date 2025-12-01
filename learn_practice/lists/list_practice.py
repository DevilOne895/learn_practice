def del_elem():
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Сыбался, только цифры давай")
        return
    list_of_numbers = []

    for i in numbers:
        digit = int(i)
        list_of_numbers.append(digit)


    result = []
    for number in list_of_numbers:
        if number not in result:
            result.append(number)

    print(result)


def max_min_sum():
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Сыбался, только цифры давай")
        return
    list_of_elem = []

    for i in numbers:
        digit = int(i)
        list_of_elem.append(digit)
        n = sorted(list_of_elem)

    print(f"Самый маленький елемент: {n[0]} \nСамый большой елемент {n[-1]} ")
    print(f"Сумма всех елементов: ", sum(n))



def sdvig():
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Сыбался, только цифры давай")
        return
    tern = input("Введите число сдвига: ")
    if not numbers.isdigit():
        print("Сыбался, только цифры давай")
        return
    list_of_num = []

    for i in numbers:
        digit = int(i)
        list_of_num.append(digit)
        x = list_of_num.pop()
        list_of_num.insert(0, x)
    print(list_of_num)



def even_odd_count():
    n = int(input("Введите числа: "))
    n = str(n)
    if not n.isdigit():
        print("Сыбался, только цифры давай")
        return
    even = 0
    odd = 0
    for lol in str(n):
        if int(lol) % 2 == 0:
            odd += 1
        else:
            even += 1
    print (f" Четные числа {odd},Не четыне числа {even}")




def temperature():
    temperatures = [18, 21, 19, 22, 20, 23, 21]
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

    for i in range(len(days)):
        print(f"{days[i]}: {temperatures[i]}°C")

    max_temp = max(temperatures)
    print("Максимальная температура:", days[i], max_temp)

    average_temp = sum(temperatures) / len(temperatures)
    print("Средняя температура:", average_temp)




def info_list():
    print("ДОБРО ПОЖАЛОВАТЬ В Eugene_INC, ВОТ СПИСОК УСЛУГ КОТОРЫЕ МЫ ПРЕДОСТОВЛЯЕМ:")
    answer = input(" 1) Удалить повторяющиеся элементы\n 2) Найти масимальный,минимальный елементы и сумму всех елементов \n 3) Сдвинуть список \n 4) Найти чётные / нечётные цифры \n 5) Найти среднюю температуру за неделю \n 6) для выхода \n Выберите услугу: ")
    if not answer.isdigit():
        print("Сыбался, только цифры давай")
        return
    if answer == "1":
        count_simvol()
    elif answer == "2":
        revers_stroki()
    elif answer == "3":
        count_letters()
    elif answer == "4":
        cansel()
    elif answer == "5":
        most_long()
    elif answer == "6":
        exit()

while True:
    info_list()