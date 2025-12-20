from datetime import date, datetime, timedelta
import calendar

LINE = "═" * 70

def print_header(title):
    print("\n" + LINE)
    print(title.center(70))
    print(LINE)


def current_time():
    from datetime import datetime

    now = datetime.now()
    print_header("ТЕКУЩЕЕ ВРЕМЯ И ДАТА")

    print(f"Дата: {now.strftime('%Y-%m-%d')}")
    print(f"Время: {now.strftime('%H:%M:%S')}")
    print(f"День недели: {now.strftime('%A')}")
    print(LINE)




def Time_difference():
    print_header("РАЗНИЦА МЕЖДУ ВРЕМЕНЕМ")

    first = int(input("Введите часы первого времени:  "))
    second = int(input("Введите минуты первого времени: "))

    first_2 = int(input("Введите часы второго времени:  "))
    second_2 = int(input("Введите минуты второго времени: "))

    total_minutes = abs((first * 60 + second) - (first_2 * 60 + second_2))

    print_header("РЕЗУЛЬТАТ")
    print(f"Разница между временами: {total_minutes} минут")
    print(LINE)



def time_left():
    from datetime import datetime, timedelta

    now = datetime.now()
    midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())

    delta = midnight - now

    print_header("ВРЕМЯ ДО ПОЛУНОЧИ")
    print(f"До полуночи осталось: {delta}")
    print(LINE)




def next_data():
    from datetime import date, datetime

    today = date.today()
    print_header("РАСЧЕТ ДНЕЙ ДО ВАШЕЙ ДАТЫ")
    print(f"Сегодня: {today.strftime('%d-%m-%Y')}")

    data = input("Введите число: ")
    data_2 = input("Введите месяц: ")
    data_3 = input("Введите год: ")

    user_input = f"{data}-{data_2}-{data_3}"
    user_date = datetime.strptime(user_input, "%d-%m-%Y").date()
    delta = user_date - today

    print_header("РЕЗУЛЬТАТ")
    print(f"До выбранной даты осталось: {delta.days} дней")
    print(LINE)


def leap_year():
    print_header("ПРОВЕРКА ВИСОКОСНОГО ГОДА")
    year = int(input("Введите год: "))

    if year % 4 == 0:
        result = "високосный"
    else:
        result = "не високосный"

    print_header("РЕЗУЛЬТАТ")
    print(f"{year} — {result}")
    print(LINE)


def conversion():
    from datetime import datetime

    now = datetime.now()
    print_header("КОНВЕРТАЦИЯ ДАТЫ")
    print(f"Дата в формате дд.мм.гггг: {now.strftime('%d.%m.%Y')}")
    print(LINE)


