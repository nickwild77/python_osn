digit = int(input("Enter digits: "))
list_of_words = ["процент", "процента", "процентов"]

if 4 < digit % 100 < 20 or digit % 10 == 0:
    print(digit, "%", list_of_words[2])

elif 1 < digit % 10 < 5:
    print(digit, "%", list_of_words[1])

else:
    print(digit, "%", list_of_words[0])
