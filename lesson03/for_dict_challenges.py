from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]


# def count_name_occurrence(list_of_dicts):
#     """когда-то нашла такой сниппет и с тех пор для подобных задач (посчитать
#     дубли) использую этот прием. Это не слишком костыльно?"""
#     names_occurrence = {}
#     for dicti in list_of_dicts:
#         name = dicti['first_name']
#         names_occurrence[name] = names_occurrence.get(name, 0) + 1
#     return names_occurrence
def count_name_occurrence(students):
    students_names = [student['first_name'] for student in students]
    return Counter(students_names)


students_names_occurrence = count_name_occurrence(students)
for name, repeats in students_names_occurrence.items():
    print(f'{name}: {repeats}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]


# def get_key_with_max_value(dicti):
#     highest_occurrence_score = max(dicti.values())
#     for key, occurrence_score in dicti.items():
#         if occurrence_score == highest_occurrence_score:
#             return key
def get_key_with_max_value(dicti):
    key_with_max_value = Counter(students_names_occurrence).most_common(1)
    return key_with_max_value[0][0]


students_names_occurrence = count_name_occurrence(students)
most_common_name = get_key_with_max_value(students_names_occurrence)
print(f'The most common name is: {most_common_name}')


# Пример вывода:
# Самое частое имя среди учеников: Маша


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


for i, school_class in enumerate(school_students):
    students_names_occurrence = count_name_occurrence(school_class)
    most_common_name = get_key_with_max_value(students_names_occurrence)
    print(
        f'{most_common_name} is the most common name in class {i+1}'
    )


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def define_students_sex(students):
    students_sex = {'Male': 0, 'Female': 0}
    for student in students:
        student_name = student['first_name']
        if is_male[student_name]:
            students_sex['Male'] += 1
        else:
            students_sex['Female'] += 1
    return students_sex


for school_class in school:
    students_sex = define_students_sex(school_class['students'])
    class_name = school_class['class']
    print(
        f'There are {students_sex["Female"]} girls and {students_sex["Male"]} '
        f'boys in {class_name}'
          )

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
  {'class': '3d', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]}
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


male_most = None
female_most = None

males_females = {}
for i, school_class in enumerate(school):
    students = school_class['students']
    students_sex = define_students_sex(students)
    class_name = school_class['class']
    males_females[class_name] = students_sex
    if not male_most or not female_most:
        male_most = class_name
        female_most = class_name
    else:
        current_class_males_count = students_sex['Male']
        current_class_females_count = students_sex['Female']
        previous_class_name = school[i-1]['class']
        previous_class_males_count = males_females[previous_class_name]['Male']
        previous_class_females_count = males_females[previous_class_name]['Female']
        if current_class_males_count > previous_class_males_count:
            male_most = school_class['class']
        if current_class_females_count > previous_class_females_count:
            female_most = school_class['class']

print(f'Больше всего мальчиков в классе {male_most}')
print(f'Больше всего девочек в классе {female_most}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
