# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def calculate():
    try:
        salary = int(input('Ставка в час '))
        benefit = int(input('Премия '))
        time = float(input('Выработка в часах '))
        resault = time * salary + benefit
        print(f'К выплате  {resault}')
    except ValueError:
        return print('Ошибка! Необходимо ввести число!')
calculate()

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_numb = [188, 199, 56, 120, 555, 1, 4, 100]
my_new_numb = [el for numbers, el in enumerate(my_numb) if my_numb[numbers - 1] < my_numb[numbers]]
print(f'Исходный список {my_numb}')
print(f'Новый список {my_new_numb}')

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

print([х for х in range(20, 241) if х % 20 == 0 or х % 21 == 0])

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [11, 2, 2, 2, 4, 4, 21, 45, 45, 60]
print([x for x in my_list if my_list.count(x)==1])

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

my_list = [x for x in range(100, 1001) if x % 2 == 0]
def my_func(x, y):
    return x * y

print(reduce(my_func, my_list))

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)

def my_cycle_func(my_list, iteration):
    count = 0
    for item in cycle(my_list):
        if count > iteration:
            break
        print(item)
        count += 1


my_count_func(start_number = int(input("Введите начальное число: ")), stop_number = int(input("Введите завершающее число: ")))
my_cycle_func(my_list = [1, 2], iteration = int(input("введите итерацию: ")))


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count
from math import factorial

def func_gen():
    for el in count(1):
        yield factorial(el)

gen = func_gen()
x = 0
for i in gen:
    if x < 20:
        print(i)
        x += 1
    else:
        break
