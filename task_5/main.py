# Чикида Римма 
text = input("Введите строку: ")# Ввод строки от пользователя
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ" # Список русских гласных букв
for i in range(len(text)): # Перебор символов с индексами
    char = text[i]
    if char.isalpha() and char not in vowels:
        print(f"Согласная буква '{char}' найдена на индексе {i}")
