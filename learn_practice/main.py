from .dict_practice import dict
from .string_lessons import string_practice
from .lists_lessons import list_practice

def main():
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



def info_str():
    answer = input(" 1) Подсчитать кол-во символов в вашем предложение!\n 2) Перевернуть ваше предолжние на оборот \n 3) Посчитать кол-во гласных и согласных букв \n 4) Убрать из вашего предложения специальыне символы \n 5) Найти самое длинное слово в вашем предложение \n 6) для выхода \n Выберите услугу: ")
    if not answer.isdigit():
        print("Только цифры давай")
        return
    if answer == "1":
        string_practice.count_simvol()
    elif answer == "2":
        string_practice.revers_stroki()
    elif answer == "3":
        string_practice.count_letters()
    elif answer == "4":
        string_practice.cansel()
    elif answer == "5":
        string_practice.most_long()
    elif answer == "6":
        exit()


def info_list():
    answer = input(" 1) Удалить повторяющиеся элементы\n 2) Найти максимальный, минимальный элементы и сумму всех элементов \n 3) Сдвинуть список \n 4) Найти чётные / нечётные цифры \n 5) Найти среднюю температуру за неделю \n 6) для выхода \n Выберите услугу: ")
    if not answer.isdigit():
        print("Только цифры давай")
        return
    if answer == "1":
        list_practice.del_elem()
    elif answer == "2":
        list_practice.max_min_sum()
    elif answer == "3":
        list_practice.shift()
    elif answer == "4":
        list_practice.even_odd_count()
    elif answer == "5":
        list_practice.temperature()
    elif answer == "6":
        exit()



if __name__ == "__main__":
    main()