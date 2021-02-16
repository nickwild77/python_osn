
words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(words):
    if s.replace("+", "").isdigit():
        if s[0] == "+":
            words[i] = f'"{s[0]}0{s[1:]}"'
        else:
            words[i] = f'"0{s}"'
print(words)
print(" ".join(words))
