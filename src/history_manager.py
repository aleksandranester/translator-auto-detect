"""
Модуль управления историей переводов.

Сохраняет выполненные переводы в течение сессии и предоставляет
доступ к ранее полученным результатам.
"""

from typing import List, Tuple


class HistoryManager:
    """
    Класс для управления историей переводов.

    Хранит пары «исходный текст — перевод» и предоставляет
    доступ к ним. Позволяет пользователю повторно просматривать
    и использовать ранее выполненные переводы.

    :author: Нестеренко А.Р.
    :version: 1.0.0

    Attributes:
        history (list): Список кортежей с парами переводов.
    """

    def __init__(self) -> None:
        """
        Инициализация менеджера истории.

        Создаёт пустой список для хранения пар переводов.
        """
        #: Список кортежей вида (original, translated)
        self.history: List[Tuple[str, str]] = []

    def save_translation(self, original: str, translated: str) -> None:
        """
        Сохранить пару: исходный текст — перевод.

        Добавляет новую запись в конец списка истории.

        :param original: Исходный текст до перевода.
        :type original: str
        :param translated: Переведённый текст.
        :type translated: str
        :return: None
        :raises TypeError: Если один из аргументов не является строкой.

        Пример использования::

            >>> hm = HistoryManager()
            >>> hm.save_translation("Hello", "Привет")
            >>> hm.get_history()
            [('Hello', 'Привет')]
        """
        if not isinstance(original, str) or not isinstance(translated, str):
            raise TypeError("Оба аргумента должны быть строками.")
        self.history.append((original, translated))

    def get_history(self) -> List[Tuple[str, str]]:
        """
        Вернуть всю историю переводов текущей сессии.

        :return: Список кортежей вида ``(original, translated)``.
        :rtype: list[tuple[str, str]]

        Пример использования::

            >>> hm = HistoryManager()
            >>> hm.save_translation("Cat", "Кот")
            >>> hm.get_history()
            [('Cat', 'Кот')]
        """
        return self.history

    def clear_history(self) -> None:
        """
        Очистить всю историю переводов.

        После вызова этого метода список истории становится пустым.

        :return: None
        """
        self.history.clear()
