#Четные целые числа, не превышающие 5 цифр. Каждое число на нечетном месте выводить словами.
import re
file = '4.txt'

def words(number):
    """Функция для преобразования числа в слова"""
    words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(words[digit] for digit in str(number))

def process_file(open_file):
    with open(open_file, 'r', encoding='utf-8') as file:
        content = file.read()
        # целые, четные, до 5 цифр
        a = re.findall(r'\b\d{1,5}\b', content)
        even_numbers = [] # список для четных чисел
        for num in a:
            num_int = int(num)  # строку в число
            if num_int % 2 == 0: 
                    even_numbers.append(num_int) 

        
        result = []
        for index, number in enumerate(even_numbers, start=1):
            if index % 2 != 0:  # Нечетное место
                result.append(words(number))
            else:  # Четное место
                result.append(str(number))
        print(' '.join(result))
process_file(file)
