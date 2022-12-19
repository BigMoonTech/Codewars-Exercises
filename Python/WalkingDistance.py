def is_valid_walk(walk):
    try:
        validate(walk)
    except ValueError:
        return False

    if walk.count('s') != walk.count('n') or walk.count('e') != walk.count('w'):
        return False
    return True


def validate(walk: list):
    if not walk:
        raise ValueError('Not enough arguments.')
    elif len(walk) != 10:
        raise ValueError('Not a valid walk.')
    elif not all(walk):
        raise ValueError
    elif not "".join(walk).isalpha():
        raise ValueError
