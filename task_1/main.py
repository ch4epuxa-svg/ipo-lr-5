# Чикида Римма
str = input("Введите строку на русском: ")
list_vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ" # Делаем список всех гласных 
vowel_count = 0
consonant_count = 0 # Счетчики гласных и согласных 
for char in str:
    if char.isalpha():  # Проходим по каждому символу 
        if char in list_vowels: # Проверяем гласные 
            vowel_count += 1 # Добавляем +1 к гласным
        else: # Если не гласный символ
            consonant_count += 1 # +1 к согласным 

# Вывод данных 
print("Длина строки:", len(str))
print("Количество гласных букв:", vowel_count) 
print("Количество согласных букв:", consonant_count)
