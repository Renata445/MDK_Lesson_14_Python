# Создайте словарь, в котором ключом будет являться число от 1 до 23,
# а значением - буквы английского алфавита.
# Решите эту задачу с помощью генератора словаря

alphabet = []
for i in range(65, 89):
    alphabet.append(chr(i))
dct = {key : value for key,value in zip(range(1, 24), alphabet)}
print(dct)