import getpass
import hashlib
import logging


logger = logging.getLogger('password_checker')


def input_and_check_password():
    logger.debug('Начало input_and_check_password')
    password: str = getpass.getpass()

    if not password:
        logger.warning('Вы ввели пустой пароль!')
        return False

    try:
        hasher = hashlib.md5()
        logger.debug(f"Мы создали объект hasher {hasher!r}")
        hasher.update(password.encode('latin-1'))
        logger.debug(f"Мы использовали метод update для объекта hasher")
        if hasher.hexdigest() == '827ccb0eea8a706c4c34a16891f84e7b':
            logger.info('Добро пожаловать!')
            return True
    except ValueError as err:
        logger.exception('Вы ввели некорректный символ ', exc_info=err)
    logger.warning('Неверный пароль!')
    return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Вы пытаетесь аутентифицироваться на сайт')
    count_number: int = 3
    logger.info(f'У вас есть {count_number} попыток')

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error('Пользователь 3 раза ввёл неправильный пароль!')
    exit(1)
