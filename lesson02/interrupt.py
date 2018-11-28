# https://learn.python.ru/lessons/12_exceptions.html?full#11

dic = {
    'how are you?': 'Good',
    'what are you doing?': 'Writing code'
}


def ask_user():
    # TODO ugly??
    while True:
        try:
            response = input('How are you?\n').lower()
            if response == 'good':
                break
            print(dic.get(response, 'Dunno what to say to you'))
        except KeyboardInterrupt:
            print('\nBye!')
            break


if __name__ == '__main__':
    ask_user()
