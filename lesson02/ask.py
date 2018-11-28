# https://learn.python.ru/lessons/11_while.html?full#8


dic = {
    'how are you?': 'Good',
    'what are you doing?': 'Writing code'
}


# def ask_user():
#     response = None
#     while response != 'good':
#         response = input('How are you?\n').lower()


def ask_user():
    while True:
        response = input('How are you?\n').lower()
        if response == 'good':
            break
        print(dic.get(response, 'Dunno what to say to you'))


def remove_special_chars():
    # TODO
    pass


if __name__ == '__main__':
    ask_user()
