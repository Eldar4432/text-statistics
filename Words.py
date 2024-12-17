import re

# Open a file with text
file_path = '17.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Counting proposals
sentences = re.split(r'[.!?]', text)
num_sentences = len([s for s in sentences if s.strip()])  # Checking for empty sentences

# Word count
words = re.findall(r'\b\w+\b', text)  # \b - main words, \w+ - symbol
num_words = len(words)

# Output of results
print(f'Количество предложений: {num_sentences}')
print(f'Количество слов: {num_words}')
