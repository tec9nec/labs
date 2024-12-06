# Четные целые числа, не превышающие 5 цифр. Каждое число на нечетном месте выводить словами.
words = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

def number_words(number):
    """Преобразует число в слова."""
    result = ""
    for digit in str(number):
        result += words[digit] + " "  # добавляем слово и пробел
    return result.strip()  # убрать пробел

def process(input_posled):
    """Обрабатывает последовательность символов, распознавая числа."""
    result = ""
    position = 1  # позиция числа 
    numbers = input_posled.split()  # деление строки на слова
    
    for item in numbers:
        if item.isdigit() and len(item) <= 5: 
            number = int(item)
            if number % 2 == 0:
                if position % 2 != 0:
                    result += number_words(number) + " "
                else:  # Чётная позиция
                    result += item + " "
                position += 1  # Учитываем только подходящие числа

    return result.strip()  # Убираем лишний пробел в конце

# Пример чтения из файла и обработки
with open('33.txt', 'r') as file:
    input_data = file.read()

output = process(input_data)
print(output)

