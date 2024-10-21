# функция для проверки, является ли введенное значение числом
def is_valid_number(input_value):
    try:
        int(input_value)  # пробуем преобразовать значение в целое число
        return True  # если успешно, возвращаем True
    except ValueError:
        return False  # если ошибка, возвращаем False
# запрашиваем у пользователя количество строк
num_lines = input("Введите количество строк: ")
# проверяем, является ли введенное значение числом и больше нуля
while not is_valid_number(num_lines) or int(num_lines) <= 0:
    num_lines = input("Некорректный ввод. Введите положительное число: ")  # повторяем запрос, пока ввод некорректен
num_lines = int(num_lines)  # преобразуем введенное значение в целое число
# инициализируем пустую строку для хранения введенного текста
text = ""
# запрашиваем строки у пользователя
for i in range(num_lines):  # цикл от 0 до num_lines-1
    line = input(f"Введите строку {i + 1}: ")  # запрашиваем каждую строку
    text += line + " "  # добавляем строку к тексту, добавляя пробел после каждой строки
# разделяем текст на слова, используя пробелы и символы конца строки
words = text.split()  # метод split() разделяет строку на слова
# создаем множество для хранения уникальных слов
unique_words = set(words)  # множество автоматически удаляет дубликаты
# определяем количество различных слов
num_unique_words = len(unique_words)  # получаем количество уникальных слов
# выводим результат
print(f"Количество различных слов: {num_unique_words}")  # Печатаем количество уникальных слов
