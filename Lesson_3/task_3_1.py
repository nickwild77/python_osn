my_dict = {"zero": "ноль", "one": "один", "two": "два", "three": "три",
           "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь",
           "eight": "восемь", "nine": "девять", "ten": "десять"}


def translate(word):
    return my_dict.get(word)


print(translate(input("ВВедите число на ангилйском: ")))