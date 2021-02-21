from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeate=False):
    """

     Функция возвращает случайные шутки, собранные из ьрех списков слов
    :param n: колличество шуток
    :param repeate: уникальные/неуникальные
    :return: список случайных шуток
    """

    list_of_jokes = []
    for i in range(0, n):
        if repeate and len(nouns) == 0:
            break
        nouns_select = choice(nouns)
        adverbs_select = choice(adverbs)
        adjectives_select = choice(adjectives)
        list_of_jokes.append(f"{nouns_select} {adverbs_select} {adjectives_select}")
        if repeate:
            nouns.remove(nouns_select)
            adverbs.remove(adverbs_select)
            adjectives.remove(adjectives_select)
    return list_of_jokes


print(get_jokes(7, True))