"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name (str): Имя пользователя

    Returns:
        str: Текст приветствия
    """
    name = name.title()
    return 'Привет, {string}'.format(string=name)
