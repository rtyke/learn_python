# https://learn.python.ru/lessons/12_exceptions.html?full#12


def add(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return None