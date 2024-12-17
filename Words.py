import re

# Открываем файл с текстом
file_path = '17.txt'  # Ваш файл называется 17.txt

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Подсчёт предложений
sentences = re.split(r'[.!?]', text)
num_sentences = len([s for s in sentences if s.strip()])  # Проверка на пустые предложения

# Подсчёт слов
words = re.findall(r'\b\w+\b', text)  # \b - граница слова, \w+ - символы, составляющие слово
num_words = len(words)

# Вывод результатов
print(f'Количество предложений: {num_sentences}')
print(f'Количество слов: {num_words}')
