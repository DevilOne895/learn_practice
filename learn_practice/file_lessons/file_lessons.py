
def open_file():
    with open("File.txt", "r", encoding="utf-8") as file:
        print(file.read())


def count_lines():
    with open("File.txt", "r", encoding="utf-8") as file:
        count = 0
        for line in file:
            count += 1
        print(file.read())
        print(f"Кол-во строк: {count}")

def count_words():
    with open("File.txt", "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()

        count = 0
        for word in words:
            count += 1

        print(f"Кол-во слов: {count}")




def longest_words():
    with open("File.txt", "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()

        max_word = ""
        for word in words:
            if len(word) > len(max_word):
                max_word = word

        print("Самое длинное слово:", max_word)
        print("Длина:", len(max_word))


def copy_file():
    with open("File.txt", "r", encoding="utf-8") as file:
        data = file.read()

    with open("copy.txt", "w", encoding="utf-8") as copy:
        copy.write(data)

    print(data)

def print_on_file():
    lines = ["первая строка\n", "вторая строка\n", "третья строка\n"]

    with open("File.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

    with open("File.txt", "r", encoding="utf-8") as file:
        txt = file.read()
        print(txt)


def add_numbers():
    numbers = list(range(1, 101))

    with open("number.txt", "w", encoding="utf-8") as file:
        for numb in numbers:
            file.write(f"{numb}\n")
            print(numb)


def logs():
    with open("logs.txt", "w", encoding="utf-8") as file:
        file.write("[2025-04-12 10:45] Программа успешно запущена")

    with open("logs.txt", "r", encoding="utf-8") as file:
        txt = file.read()
        print(txt)


def add_new_words():
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write("Новая запись")

    with open("file.txt", "r", encoding="utf-8") as file:
        txt = file.read()
        print(txt)


def remove_old_words():
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write("Файл был обновлен!")

    with open("file.txt", "r", encoding="utf-8") as file:
        txt = file.read()
        print(txt)


