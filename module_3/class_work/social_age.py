def get_social_status(age: (int, float)) -> str:
    if not isinstance(age, (int, float)):
        raise ValueError('Пожалуйста, введите число')
    if age <= 0:
        raise ValueError('Возраст не может быть отрицательным')

    if 0 < age < 13:
        return 'Ребёнок'
    elif 13 <= age < 18:
        return 'Подросток'
    elif 18 <= age < 50:
        return 'Взрослый'
    elif 50 <= age < 65:
        return 'Пожилой'
    else:
        return 'Пенсионер'

