# Чикида Римма 
# Открываем исходный файл для чтения
with open("text.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# Переворачиваем каждую строку
reversed_lines = [line.strip()[::-1] + "\n" for line in lines]

# Записываем результат в новый файл
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(reversed_lines)
