"""
Модуль настроек пользователя.

Управляет персональными параметрами приложения:
языком интерфейса, темой оформления и прочими предпочтениями.
"""


class Settings:
    """
    Класс управления настройками пользователя.

    Хранит и предоставляет доступ к персональным параметрам
    приложения. Позволяет изменять язык по умолчанию,
    тему оформления и управлять параметрами хранения данных.

    :author: Нестеренко А.Р.
    :version: 1.0.0

    Attributes:
        default_language (str): Язык перевода по умолчанию.
        theme (str): Текущая тема оформления (``"light"`` или ``"dark"``).
    """

    def __init__(self) -> None:
        """
        Инициализация настроек значениями по умолчанию.

        Устанавливает английский язык и светлую тему.
        """
        #: Язык перевода по умолчанию
        self.default_language: str = "en"
        #: Тема интерфейса: ``"light"`` (светлая) или ``"dark"`` (тёмная)
        self.theme: str = "light"

    def update_language(self, language: str) -> None:
        """
        Изменить язык перевода по умолчанию.

        :param language: Новый код языка (например, ``"ru"``, ``"de"``).
        :type language: str
        :return: None
        :raises ValueError: Если передана пустая строка.

        Пример использования::

            >>> s = Settings()
            >>> s.update_language("ru")
            >>> s.default_language
            'ru'
        """
        if not language:
            raise ValueError("Код языка не может быть пустым.")
        self.default_language = language

    def toggle_theme(self) -> None:
        """
        Переключить тему оформления между светлой и тёмной.

        Если текущая тема ``"light"`` — устанавливает ``"dark"``,
        и наоборот.

        :return: None
        """
        self.theme = "dark" if self.theme == "light" else "light"
