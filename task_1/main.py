# Чикида Римма
str = input("Введите строку на русском: ")
list_vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowel_count = 0
consonant_count = 0
for char in str:
    if char.isalpha():  # Проверяем, что символ — буква
        if char in list_vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Вывод результатов
print("Длина строки:", len(str))
print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)
