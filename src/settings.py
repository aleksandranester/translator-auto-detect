"""
Модуль настроек пользователя
Управляет параметрами приложения
"""

class Settings:
    def __init__(self):
        # Язык по умолчанию
        self.default_language = "en"
        
        # Тема интерфейса
        self.theme = "light"

    def update_language(self, language):
        """Изменение языка по умолчанию"""
        self.default_language = language
