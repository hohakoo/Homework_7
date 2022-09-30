import os


# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).


def return_domains_without_point(filename):
    with open(filename, "r") as file:
        domains = [element[1:].strip() for element in file.readlines()]
    return domains


filename = "domains.txt"
print(return_domains_without_point(filename))

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"


def return_surnames(filename):
    with open(filename, 'r') as file:
        surnames = [line.split()[1] for line in file.readlines()]
    return surnames


filename = "names.txt"


print(return_surnames(filename))

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]


def return_date(filename):
    with open(filename, "r") as file:
        info = file.readlines()

    the_list = []

    for line in info:
        if "-" in line:
            the_list.append({"date": line[:line.find(" -")]})
    return the_list


filename = "authors.txt"

print(return_date(filename))
# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - это та же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]


def modifying_of_date(filename):

    with open(filename, "r") as file:
        info = file.readlines()

    months = [line.strip() for line in info if 1 < len(line) < 11] #Список месяцев

    number_of_each_month = {month: str(value+1).zfill(2) for value,month in enumerate(months)} #Номер каждого месяца в формате 01,02,03...

    the_list = []

    for line in info:

        if "-" in line:
            original_date = line[:line.find(" -")]
            #условие для экземпляра без числа
            if original_date[0].isalpha():
                original_date = "XX " + original_date
                day = "XX"

            elif original_date[:2].isdigit():
                day = original_date[:2]
            #Превращаем однозначные числа в формат 01,02,03...
            else:
                day = original_date[:1].zfill(2)

            month = number_of_each_month[original_date[original_date.find(' ')+1: original_date.rfind(' ')]]

            year = original_date[-4:]

            modified_date = f"{day}/{month}/{year}"

            the_list.append({"date_original": original_date, "date_modified": modified_date})
    return(the_list)


print(modifying_of_date(filename))