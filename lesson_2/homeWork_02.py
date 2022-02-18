# Задание №1

my_list = [22, None, -88, 'True', True, 6.5]

def my_type(list):
    el = 0
    for el in range(len(list)):
        print(type(list[el]))

my_type(my_list)

# Задание №2

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

# Задание 3

month = int(input("Введите номер месяца"))

months_dict = {1: "Зима", 2: "Зима", 12: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
               9: "Осень", 10: "Осень", 11: "Осень"}

if 12 >= month >= 1:
    print(months_dict[month])
else:
    print("Такого месяца нет")

#Задание 4

my_str = input("Введите предложение ")
number = 1
my_word = my_str.split(" ")

for el in my_word:
    if len (str(el)) > 10:
        print(f" {number} {el[0:10]}")
    else:
        print(f" {number} {el}")
    number += 1

#Задание 5

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число "))

for el in range(len(my_list)):
    if my_list[el] == digit:
        my_list.insert(el + 1, digit)
        break
    elif my_list[0] < digit:
        my_list.insert(0, digit)
        break
    elif my_list[-1] > digit:
        my_list.append(digit)
        break
    elif my_list[el] > digit and my_list[el + 1] < digit:
        my_list.insert(el + 1, digit)
print(f"текущий список - {my_list}")

#Задание 6

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
