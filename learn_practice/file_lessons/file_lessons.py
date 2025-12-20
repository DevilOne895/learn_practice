LINE = "═" * 70

def print_header(title):
    print("\n" + LINE)
    print(title.center(70))
    print(LINE)


def open_file():
    print_header("ПРОСМОТР ФАЙЛА")
    with open("File.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
    print(LINE)



def count_lines():
    print_header("ПОДСЧЕТ СТРОК В ФАЙЛЕ")
    with open("File.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("Содержимое файла:")
        print("".join(lines))
        print(f"\nКоличество строк: {len(lines)}")
    print(LINE)


def count_words():
    print_header("ПОДСЧЕТ СЛОВ В ФАЙЛЕ")
    with open("File.txt", "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        print(f"Количество слов: {len(words)}")
    print(LINE)





def longest_words():
    print_header("НАЙТИ САМОЕ ДЛИННОЕ СЛОВО")
    with open("File.txt", "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        max_word = max(words, key=len)
        print(f"Самое длинное слово: {max_word}")
        print(f"Длина: {len(max_word)}")
    print(LINE)



def copy_file():
    print_header("КОПИРОВАНИЕ ФАЙЛА")
    with open("File.txt", "r", encoding="utf-8") as file:
        data = file.read()

    with open("copy.txt", "w", encoding="utf-8") as copy:
        copy.write(data)

    print("Содержимое файла было скопировано:")
    print(data)
    print(LINE)


def print_on_file():
    print_header("ЗАПИСЬ СПИСКА В ФАЙЛ")
    lines = ["первая строка\n", "вторая строка\n", "третья строка\n"]

    with open("File.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

    with open("File.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Файл после записи:")
        print(content)
    print(LINE)


def add_numbers():
    print_header("ЗАПИСЬ ЧИСЕЛ В ФАЙЛ")
    numbers = list(range(1, 101))

    with open("number.txt", "w", encoding="utf-8") as file:
        for numb in numbers:
            file.write(f"{numb}\n")
            print(numb)
    print(LINE)



def logs():
    print_header("ЛОГИ ПРОГРАММЫ")
    with open("logs.txt", "w", encoding="utf-8") as file:
        file.write("[2025-04-12 10:45] Программа успешно запущена")

    with open("logs.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
    print(LINE)



def add_new_words():
    print_header("ДОБАВЛЕНИЕ НОВЫХ ЗАПИСЕЙ В ФАЙЛ")
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write("Новая запись\n")

    with open("file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Файл после добавления:")
        print(content)
    print(LINE)



def remove_old_words():
    print_header("ПЕРЕЗАПИСЬ ФАЙЛА")
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write("Файл был обновлен!\n")

    with open("file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Файл после обновления:")
        print(content)
    print(LINE)


