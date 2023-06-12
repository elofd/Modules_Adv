def is_strong_password(password: str):
    with open('/usr/share/dict/words', 'r') as file:
        data = tuple(filter(lambda el: len(el) > 4, file.read().split()))
        for elem in data:
            if elem in password.lower():
                return False
        return True


if __name__ == '__main__':
    print(is_strong_password('qweapPle'))
