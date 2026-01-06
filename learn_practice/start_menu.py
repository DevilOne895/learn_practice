from file_lessons import file_lessons
from time_practice import time_lessons
from dict_practice import dict
from string_lessons import string_practice
from lists_lessons import list_practice
import start_menu
LINE = "═" * 70

def header(title):
    print("\n" + LINE)
    print(f"{title.center(70)}")
    print(LINE)


def main():
    main_map = {
        "1": info_str,
        "2": info_list,
        "3": info_time,
        "4": info_dict,
        "5": info_file,
    }
    while True:
        header("EUGENE_INC • ГЛАВНОЕ МЕНЮ")

        answer = input(
            " 1) Работа со строками\n"
            " 2) Работа со списками\n"
            " 3) Работа со временем\n"
            " 4) Работа со словарями\n"
            " 5) Работа с файлами\n"
            " 6) Выход из программы\n\n"
            " ➜ Введите номер: "
        )

        if not answer.isdigit():
            print("\n⚠ Только цифры\n")
            continue

        if answer == "6":
            print("\nПрограмма завершена.\n")
            break

        action = main_map.get(answer)

        if action:
            action()
        else:
            print("\n❌ Нет такого пункта меню\n")



def info_str():
    string_map = {
        "1": string_practice.count_simvol,
        "2": string_practice.revers_stroki,
        "3": string_practice.count_letters,
        "4": string_practice.cansel,
        "5": string_practice.most_long,
    }
    while True:
        header("РАБОТА СО СТРОКАМИ")

        answer = input(
            " 1) Подсчитать количество символов\n"
            " 2) Перевернуть предложение\n"
            " 3) Посчитать гласные и согласные\n"
            " 4) Убрать специальные символы\n"
            " 5) Найти самое длинное слово\n"
            " 6) Назад в главное меню\n\n"
            " ➜ Выбор: "
        )

        if not answer.isdigit():
            print("\n⚠ Только цифры\n")
            continue

        if answer == "6":
            break

        action = string_map.get(answer)

        if action:
            action()
        else:
            print("\n❌ Нет такого пункта меню\n")






def info_list():
    list_map = {
        "1": list_practice.del_elem,
        "2": list_practice.max_min_sum,
        "3": list_practice.shift,
        "4": list_practice.even_odd_count,
        "5": list_practice.temperature,
    }
    while True:
        header("РАБОТА СО СПИСКАМИ")

        answer = input(
            " 1) Удалить повторяющиеся элементы\n"
            " 2) Найти максимум, минимум и сумму\n"
            " 3) Сдвинуть список\n"
            " 4) Найти чётные и нечётные\n"
            " 5) Средняя температура за неделю\n"
            " 6) Назад в главное меню\n\n"
            " ➜ Выбор: "
        )

        if not answer.isdigit():
            print("\n⚠ Только цифры\n")
            continue

        if answer == "6":
            break

        action = list_map.get(answer)

        if action:
            action()
        else:
            print("\n❌ Нет такого пункта меню\n")




def info_time():
    time_map = {
        "1": time_lessons.current_time,
        "2": time_lessons.Time_difference,
        "3": time_lessons.time_left,
        "4": time_lessons.next_data,
        "5": time_lessons.leap_year,
        "6": time_lessons.conversion,
    }
    while True:
        header("РАБОТА СО ВРЕМЕНЕМ")

        answer = input(
            " 1) Текущее время\n"
            " 2) Разница между временами\n"
            " 3) Сколько осталось до полуночи\n"
            " 4) Дата через N дней\n"
            " 5) Високосный год\n"
            " 6) Конвертация даты\n"
            " 7) Назад в главное меню\n\n"
            " ➜ Выбор: "
        )

        if not answer.isdigit():
            print("\n⚠ Только цифры\n")
            continue

        if answer == "7":
            break

        action = time_map.get(answer)

        if action:
            action()
        else:
            print("\n❌ Нет такого пункта меню\n")




def info_dict():
    dict_map = {
        "1": dict.count_words,
        "2": dict.phone_book,
    }
    while True:
        header("РАБОТА СО СЛОВАРЯМИ")


        answer = input(
            " 1) Подсчитать количество слов\n"
            " 2) Телефонный справочник\n"
            " 3) Назад в главное меню\n\n"
            " ➜ Выбор: "
        )

        if not answer.isdigit():
            print("\n⚠ Только цифры\n")
            continue

        if answer == "3":
            break

        action = dict_map.get(answer)

        if action:
            action()
        else:
            print("\n❌ Нет такого пункта меню\n")



def info_file():

    menu_map = {
        "1": file_lessons.open_file,
        "2": file_lessons.count_lines,
        "3": file_lessons.count_words,
        "4": file_lessons.longest_words,
        "5": file_lessons.copy_file,
        "6": file_lessons.print_on_file,
        "7": file_lessons.add_numbers,
        "8": file_lessons.logs,
        "9": file_lessons.add_new_words,
        "10": file_lessons.remove_old_words,
    }
    while True:
        print("\n" + "═" * 70)
        print("РАБОТА С ФАЙЛАМИ".center(70))
        print("═" * 70)

        answer = input(
            " 1) Прочитать файл\n"
            " 2) Подсчитать строки\n"
            " 3) Подсчитать слова\n"
            " 4) Найти самое длинное слово\n"
            " 5) Скопировать файл\n"
            " 6) Записать список в файл\n"
            " 7) Создать файл с числами\n"
            " 8) Логирование\n"
            " 9) Добавить текст\n"
            "10) Перезаписать файл\n"
            "11) Назад в главное меню\n\n"
            " ➜ Выбор: "
        )

        if not answer.isdigit():
            print("\n⚠ Только цифры\n")
            continue

        if answer == "11":
            break

        action = menu_map.get(answer)

        if action:
            action()
        else:
            print("\n❌ Нет такого пункта меню\n")

