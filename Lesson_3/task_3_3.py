def thesaurus(*args):
    names = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names:
            names[letter] = []
        if letter in names:
            names[letter].append(i)

    return names

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Николай", "Сергей", "Арина"))