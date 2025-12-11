from datetime import date, datetime, timedelta
import calendar


def current_time():
    from datetime import datetime

    now = datetime.now()

    print(now.strftime("%Y-%m-%d"))  # дата
    print(now.strftime("%H:%M:%S"))  # время
    print(now.strftime("%A"))  # день недели



def Time_difference():

    first = int(input ("Введите часы первого времени:  "))
    second = int(input("Введите минуты первого временеи: "))

    first_2 = int(input("Введите часы второго времени:  "))
    second_2 = int(input("Введите минуты второго времени: "))

    total_minuts = (first * 60 + second) - (first_2 * 60 + second_2)

    print(f"Разница между временнами {total_minuts}")


def time_left():

    now = datetime.now()
    midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())

    delta = midnight - now
    print(delta)

def next_data():

    today = date.today()
    print("Хотите узнать сколько дней до вашей даты?")
    print("Сегодняшняя дата:")
    print(today.strftime("%d-%m-%Y"))

    data = input("Введите число: ")
    data_2 = input("Введите месяц: ")
    data_3 = input("Введите год: ")


    user_input = f"{data}-{data_2}-{data_3}"

    user_date = datetime.strptime(user_input, "%d-%m-%Y").date()


    delta = user_date - today

    print(f"До выбранной даты осталось: {delta.days} дней")


def leap_year():

    print("Давайте определим, высокосный ли год!")
    year = int(input("Введите год: "))
    if year % 4 == 0:
        print(f" {year} высокосный ")
    else:
        print(f" {year} не высокосный ")


def conversion():

    now = datetime.now()

    print(now.strftime("%d.%m.%Y"))

