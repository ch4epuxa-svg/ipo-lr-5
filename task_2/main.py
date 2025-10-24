# Чикида Римма
str1 = input("Введите первую строку: ").replace(" ", "").lower()
str2 = input("Введите виорую строку: ").replace(" ", "").lower()
if sorted(str1) == sorted(str2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")
