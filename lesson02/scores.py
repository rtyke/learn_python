# https://learn.python.ru/lessons/13_for.html?full#16


PERFOMANCE = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '2b', 'scores': [5, 4, 4, 5, 5]},
    {'school_class': '9b', 'scores': [3, 3, 4, 4, 5]},
]


def average_school_score():
    total_scores, scores_number = 0, 0
    for school_class in PERFOMANCE:
        total_scores += sum(school_class['scores'])
        scores_number += len(school_class['scores'])
    return total_scores/scores_number


def average_class_score(class_name):
    for school_class in PERFOMANCE:
        if school_class['school_class'] == class_name:
            scores = school_class['scores']
            return sum(scores)/len(scores)


print(average_school_score())
print(average_class_score('4a'))
print(average_class_score('2b'))
print(average_class_score('9b'))
