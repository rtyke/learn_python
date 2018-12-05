# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)

# за решение ниже по рукам не бьют? Вроде жаль городить цикл из-за крошечной операции,
# с другой стороны, распаковка списка в print выглядит непривчной
print(*names, sep=', ')


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name, len(name))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for name in names:
    if name not in is_male:
        print(f'{name} is not in the dictionary')
    elif is_male[name]:
        print(f'{name} is male')
    else:
        print(f'{name} is female')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

groups_number = len(groups)
members_in_group = [len(inner_group) for inner_group in groups]


print(f'There are {groups_number} groups.')
for group_volume in members_in_group:
    print(f'There are {members_in_group} students in group.')


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

group_counter = 1
for i, inner_group in enumerate(groups):
    names = ', '.join(inner_group)
    print(f'Group {i+1} : {names}')
