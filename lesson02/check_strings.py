# https://learn.python.ru/lessons/10_if.html?full#9


def check_strings(first_string, second_string):
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return 0
    elif first_string == second_string:
        return 1
    elif len(first_string) > len(second_string):
        return 2
    elif second_string == 'learn':
        return 3
    else:
        return None
