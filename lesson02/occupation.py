# https://learn.python.ru/lessons/10_if.html?full#8


def define_occupation(age):
    if age in range(0, 7):
        return 'Kindergarten'
    elif age in range(7, 18):
        return 'School'
    elif age in range(18, 23):
        return 'University'
    else:
        return 'Working hard'


if __name__ == '__main__':
    uage = int(input('How old are you?\n'))
    occupation = define_occupation(uage)
    print(occupation)

