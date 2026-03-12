"""
Модуль управления историей переводов.
Сохраняет выполненные переводы в течение сессии.
"""

class HistoryManager:
    """
    Класс для управления историей переводов.
    
    Хранит пары исходный текст — перевод
    и предоставляет доступ к ним.
    
    Attributes:
        history (list): Список кортежей с парами переводов.
    """

    def __init__(self):
        """
        Инициализация менеджера истории.
        Создаёт пустой список для хранения переводов.
        """
        self.history = []

    def save_translation(self, original, translated):
        """
        Сохраняет пару: исходный текст — перевод.

        Args:
            original (str): Исходный текст до перевода.
            translated (str): Переведённый текст.

        Returns:
            None
        """
        self.history.append((original, translated))

    def get_history(self):
        """
        Возвращает всю историю переводов.

        Returns:
            list: Список кортежей вида (original, translated).
        """
        return self.history
