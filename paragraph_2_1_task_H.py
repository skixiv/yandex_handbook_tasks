# Наше развлечение не осталось незамеченным...
# И наказание нам выбрали соответствующее.

# Напишите программу, которая выводит N строк наказания. Каждая строка должна содержать текст в указанном формате, включающий часть наказания, введённую пользователем.

# Решение
n = int(input())
punishment = input()
print(f'Я больше никогда не буду писать "{punishment}"!\n' * n, end='')