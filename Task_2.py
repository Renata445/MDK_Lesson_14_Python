# Напишите функцию-генератор, которая выдает буквы английского алфавита от a до z.
# Опустошите генератор любым способом.

def alphabet_english():
    for i in range(97, 123):
        yield chr(i)

for i in alphabet_english():
    print(i)