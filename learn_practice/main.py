def count_simvol():
    text = input("Введите ваш текст: ")

    letters = 0
    digits = 0
    spaces = 0
    others = 0

    for i in text:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
        elif i.isspace():
            spaces += 1
        else:
            others += 1

    print(f"Букв: {letters}")
    print(f"Цифр: {digits}")
    print(f"Пробелов: {spaces}")
    print(f"Других символов: {others}")


def revers_stroki():
    txt = input("Введите ваш текст:  ")
    reversed_txt = ""
    for i in txt:
        reversed_txt = i + reversed_txt
    print(reversed_txt)


def count_letters():
    vowels = ["А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]
    consonants = ["Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш","Щ"]

    txt = input("Введите ваше предложение: ").upper()

    v_count = 0
    c_count = 0

    for i in txt:
        if i in vowels:
            v_count += 1
        elif i in consonants:
            c_count += 1


    print(f"Гласные буквы: {v_count}")
    print(f"Согласные буквы: {c_count}")




def cansel():
    punctuation = [
        ".", ",", ";", ":", "...", "!", "?", "-", "—",
        "(", ")", "[", "]", "{", "}", "«", "»", "“", "”", "‘", "’", "'", '"',
        "/", "\\", "@", "#", "$", "%", "&", "*", "~", "|", "_", "^"
    ]

    txt = input("Введите ваше предложение: ")
    for i in punctuation:
        txt = txt.replace(i, "")

    print(txt)


def most_long():
    txt = input("Введите ваше предложение: ")
    txt = txt.split()

    longest_word = ""
    for word in txt:
        if len(word) > len(longest_word):
            longest_word = word

    print(f"Самое длинное слово: '{longest_word}', длина: {len(longest_word)}")



def info_str():
    answer = input(" 1) Подсчитать кол-во символов в вашем предложение!\n 2) Перевернуть ваше предолжние на оборот \n 3) Посчитать кол-во гласных и согласных букв \n 4) Убрать из вашего предложения специальыне символы \n 5) Найти самое длинное слово в вашем предложение \n 6) для выхода \n Выберите услугу: ")
    if not answer.isdigit():
        print("Только цифры давай")
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


def del_elem():
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

    print(result)


def max_min_sum():
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Только цифры давай")
        return
    list_of_elem = []

    for i in numbers:
        digit = int(i)
        list_of_elem.append(digit)
        n = sorted(list_of_elem)

    print(f"Самый маленький елемент: {n[0]} \nСамый большой елемент {n[-1]} ")
    print(f"Сумма всех елементов: ", sum(n))



def shift():
    numbers = input("Введите числа: ")
    if not numbers.isdigit():
        print("Только цифры давай")
        return
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
    answer = input(" 1) Удалить повторяющиеся элементы\n 2) Найти максимальный, минимальный элементы и сумму всех элементов \n 3) Сдвинуть список \n 4) Найти чётные / нечётные цифры \n 5) Найти среднюю температуру за неделю \n 6) для выхода \n Выберите услугу: ")
    if not answer.isdigit():
        print("Только цифры давай")
        return
    if answer == "1":
        del_elem()
    elif answer == "2":
        max_min_sum()
    elif answer == "3":
        shift()
    elif answer == "4":
        even_odd_count()
    elif answer == "5":
        temperature()
    elif answer == "6":
        exit()



def main_menu():
    print("ДОБРО ПОЖАЛОВАТЬ В Eugene_INC, ВОТ СПИСОК УСЛУГ КОТОРЫЕ МЫ ПРЕДОСТОВЛЯЕМ:")
    print("Выберите какой раздел вам надо:")
    answer = input("1) Работа со строками \n2) Работа со списками \n Введите числа: ")
    if not answer.isdigit():
        print("Только цифры давай")
        return
    if answer == "1":
        info_str()
    elif answer == "2":
        info_list()
    else:
        pass

while True:
    main_menu()
