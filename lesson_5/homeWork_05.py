# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def edit_file():
    file = open("text_1.txt", "w")

    while True:
        line = input("Введите данные ")
        file.write(line + '\n')

        if line == "":
            break

    file.close()


# edit_file()


# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

def count_file():
    count = 0

    with open(r"text_2.txt", "r") as file:
        for line in file:
            words_line = len(line.split(' '))
            print(f"Количество слов в {count + 1} строке {words_line}")
            count += 1

    print(f"Всего строк = {count}")
    file.close()


# count_file()

# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def users_cash():
    with open(r"text_3.txt", "r") as file:
        count = 0
        rezult_salary_mid = 0
        for line in file:
            words_line = line.split(' ')
            salary = float(words_line[1].replace("\n", ""))
            rezult_salary_mid += salary
            count += 1

            if salary < 20000.0:
                print(f"Зарплата меньше 20тыс. у {words_line[0]}")

    print(f"Средняя зарплата всех сотрудников = {rezult_salary_mid / count}")
    file.close()


# users_cash()


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def replace_number():
    with open(r"text_4_old.txt", "r") as file:
        count = 0
        numerals = ('Один', 'Два', 'Три', 'Четыре')
        rezult = []
        for line in file:
            number_line = line.split(' ')
            number = int(number_line[2].replace("\n", ""))
            rezult.insert(count, f"{numerals[count]} - {number}")
            count += 1
    file.close()

    with open(r"text_4_new.txt", "w") as file:
        for line in rezult:
            file.write(line + '\n')


# replace_number()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def sum_number():
    file = open("text_5.txt", "w")
    file.write("0 1 2 3 4 5")
    rezult = 0
    with open(r"text_5.txt", "r") as file:
        for line in file:
            numbers = line.split(' ')

        for numb in numbers:
            rezult += int(numb)

    file.close()
    print(rezult)


# sum_number()

# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def lessons():
    subj = {}
    with open('text_6.txt', 'r') as file:
        for line in file:
            lesson = line.split(" ")
            new_numb = lesson[len(lesson) - 1].replace("\n", "")
            lesson[len(lesson) - 1] = new_numb
            i = 1
            number_sum = 0
            while i < len(lesson):
                number_sum += int(lesson[i])
                i += 1
            subj[lesson[0]] = number_sum
    file.close()

    print(f'Общее количество часов по предмету - \n {subj}')


# lessons()


# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

def company():
    import json
    profit = {}
    prof = 0
    prof_aver = 0
    i = 0
    with open('text_7.txt', 'r') as file:
        for line in file:
            name, firm, earning, damage = line.split()
            profit[name] = int(earning) - int(damage)
            if profit.setdefault(name) >= 0:
                prof = prof + profit.setdefault(name)
                i += 1
        if i != 0:
            prof_aver = prof / i
            print(f'Прибыль средняя - {prof_aver:.2f}')
        else:
            print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
        pr = {'average_profit': round(prof_aver)}
        profit.update(pr)
        print(f'Прибыль каждой компании - {profit}')

    with open('file_7.json', 'w') as write_js:
        json.dump(profit, write_js)

        js_str = json.dumps(profit)
        print(f'Создан файл с расширением json со следующим содержимым: \n '
              f' {js_str}')


company()