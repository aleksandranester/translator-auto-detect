# Ветка core-modules: основной функционал перевода

"""
Модуль управления историей переводов
Сохраняет выполненные переводы
"""

class HistoryManager:
    def __init__(self):
        # Список для хранения истории переводов
        self.history = []

    def save_translation(self, original, translated):
        """Сохранение пары: исходный текст — перевод"""
        self.history.append((original, translated))

    def get_history(self):
        """Получение всей истории переводов"""
        return self.history
