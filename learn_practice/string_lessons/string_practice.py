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

