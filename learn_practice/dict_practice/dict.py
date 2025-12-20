LINE = "═" * 70

def print_header(title):
    print("\n" + LINE)
    print(title.center(70))
    print(LINE)

def count_words():
    print_header("ПОДСЧЕТ СЛОВ В ТЕКСТЕ")
    text = input("Введите ваш текст: ")

    symbols_to_remove = ".,!?:;-"
    for symbol in symbols_to_remove:
        text = text.replace(symbol, "")

    words = text.lower().split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print_header("РЕЗУЛЬТАТ")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    print(LINE)


def phone_book():
    contacts = {
        "Алина": "0932456789",
        "Марк": "0671122334",
        "Женя": "0509988776",
        "Олег": "0915566778",
        "Лера": "0954433221"
    }

    print_header("ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    info = input("Что хотите сделать? (добавить/удалить/поиск): ").lower()

    if info == "добавить":
        while True:
            name = input("Введите имя контакта (или 'Стоп' для выхода): ")
            if name.lower() == "стоп":
                break

            numb = input("Введите номер контакта (или 'Стоп' для выхода): ")
            if numb.lower() == "стоп":
                break

            contacts[name] = numb
            print_header("КОНТАКТ ДОБАВЛЕН")
            print(f"Контакт {name} добавлен.")
            print("Текущий список контактов:", contacts)

    elif info == "удалить":
        print_header("УДАЛЕНИЕ КОНТАКТА")
        print("Текущий список контактов:", contacts)
        delcontacts = input("Введите имя контакта для удаления: ")
        if delcontacts in contacts:
            contacts.pop(delcontacts)
            print("Контакт удален!")
            print("Текущий список контактов:", contacts)
        else:
            print("Такого контакта нет.")
            print("Текущий список контактов:", contacts)

    elif info == "поиск":
        search = input("Введите имя контакта: ")
        print_header("ПОИСК КОНТАКТА")
        if search in contacts:
            print("Вот ваш контакт:", contacts[search])
        else:
            print("Контакт не найден.")
        print(LINE)



def dictionaru():
    data = {"a": 1, "b": 2, "c": 1}

    result = {}

    for key, value in data.items():
        if value not in result:
            result[value] = []
        result[value].append(key)

    print_header("ИНВЕРТИРОВАНИЕ СЛОВАРЯ")
    print(result)
    print(LINE)



def store():
    store1 = {"apple": 30, "banana": 20}
    store2 = {"apple": 25, "orange": 40}

    fruits = ["apple", "banana", "orange"]

    print_header("МИНИМАЛЬНАЯ ЦЕНА НА ФРУКТЫ")
    for fruit in fruits:
        values = []
        if fruit in store1:
            values.append(store1[fruit])
        if fruit in store2:
            values.append(store2[fruit])

        if values:
            print(f"{fruit}: {min(values)}")
    print(LINE)




