# Ветка ui-modules: модуль пользовательского интерфейса

"""
Модуль пользовательского интерфейса
Отвечает за взаимодействие пользователя с системой
"""

class UserInterface:
    def __init__(self):
        # Исходный текст пользователя
        self.input_text = ""
        
        # Язык перевода по умолчанию
        self.target_language = "en"

    def get_user_input(self):
        """Получение введённого пользователем текста"""
        return self.input_text

    def display_result(self, result):
        """Отображение результата перевода"""
        print("Результат перевода (UI):")
