# функция для возврата слов с прописной буквы

def int_func(t):
    return t.title()

word = input('Введите слово: ')
print(int_func(word))

text = input('Введите текст: ')

res_text = [int_func(i) for i in text.split()]

print (' '.join(res_text))