import time
from datetime import date, datetime, timedelta
import calendar

from file_lessons import file_lessons
from time_practice import time_lessons
from dict_practice import dict
from string_lessons import string_practice
from lists_lessons import list_practice
from main_menu import start_menu
LINE = "═" * 70

def header(title):
    print("\n" + LINE)
    print(f"{title.center(70)}")
    print(LINE)


def main():
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

        if answer == "1":
            info_str()
        elif answer == "2":
            info_list()
        elif answer == "3":
            info_time()
        elif answer == "4":
            info_dict()
        elif answer == "5":
            info_file()
        elif answer == "6":
            print("\nПрограмма завершена.\n")
            break



def info_str():
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
            break





def info_list():
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
            break




def info_time():
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

        if answer == "1":
            time_lessons.current_time()
        elif answer == "2":
            time_lessons.Time_difference()
        elif answer == "3":
            time_lessons.time_left()
        elif answer == "4":
            time_lessons.next_data()
        elif answer == "5":
            time_lessons.leap_year()
        elif answer == "6":
            time_lessons.conversion()
        elif answer == "7":
            break




def info_dict():
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

        if answer == "1":
            dict.count_words()
        elif answer == "2":
            dict.phone_book()
        elif answer == "3":
            break


def info_file():
    while True:
        header("РАБОТА С ФАЙЛАМИ")

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

        if answer == "1":
            time_lessons.open_file()
        elif answer == "2":
            time_lessons.count_lines()
        elif answer == "3":
            time_lessons.count_words()
        elif answer == "4":
            time_lessons.longest_words()
        elif answer == "5":
            time_lessons.copy_file()
        elif answer == "6":
            time_lessons.print_on_file()
        elif answer == "7":
            time_lessons.add_numbers()
        elif answer == "8":
            time_lessons.logs()
        elif answer == "9":
            time_lessons.add_new_words()
        elif answer == "10":
            time_lessons.remove_old_words()
        elif answer == "11":
            break