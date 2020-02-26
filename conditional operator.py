class ConditionalTasks:
    def format_as_sentence(self, text: str):
        """Написать программу, которая делает заглавной первую букву предложения(Если это необходимо), ставит точку в конце
            предложения. Строку взять любую из предыдущих, без точки.
        """
        format_text = text.capitalize()
        if format_text.endswith('.'):
            return format_text
        return format_text + '.'

    def get_numeral_cursive(self, integer):
        """В переменной integer хранится число 2 или 3 или 4. Вывести сообщение 'В переменной integer хранится '
        и число прописью.
        """
        cursive = 'В переменной integer хранится '
        if integer == 2:
            cursive += 'два'
        elif integer == 3:
            cursive += 'три'
        elif integer == 4:
            cursive += 'четыре'
        else:
            cursive += 'другое число'
        return cursive

    def get_number_apple_in_bucket(self, apple_count):
        """В корзине несколько яблок. Если одно яблоко то вывести "Яблоко одно" Если яблок меньше трёх, то "Мало яблок",
         если яблок 3 или больше, то 'Яблок хватит всем'
         """
        if apple_count == 1:
            count = 'Яблоко одно'
        elif apple_count < 3 and apple_count > 1:
            count = 'Мало яблок'
        elif apple_count >= 3:
            count = 'Яблок хватит всем'
        return count

    def compare_numbers(self, first_number, second_number):
        """Сравнить 2 числа, Вывести большее. Если они равны то вывести 'Числа равны'"""
        if first_number == second_number:
            comparison_result = 'Числа равны'
        elif first_number > second_number:
            comparison_result = first_number
        elif first_number < second_number:
            comparison_result = second_number
        return comparison_result

    def lining_bucket(self, bucket):
        """Если в строке, описывающей коризну, есть "яблоки" или "груши" или "апельсины", то вывести Фрукты.
            Если в строке, описывающей корзину, есть одновременно слова "специи" и "овощи" и "мясо", тогда вывести
            'суповой набор'
        """
        if bucket.find('яблоки') != -1 or bucket.find('груши') != -1 or bucket.find('апельсины') != -1:
            return 'Фрукты'
        elif bucket.find('специи') != -1 and bucket.find('овощи') != -1 and bucket.find('мясо') != -1:
            return 'Суповой набор'
        else:
            return 'В корзине не то, что нам нужно'

    def lining_bucket_array(self, bucket):
        """Если в строке, описывающей коризну, есть "яблоки" или "груши" или "апельсины", то вывести Фрукты.
            Если в строке, описывающей корзину, есть одновременно слова "специи" и "овощи" и "мясо", тогда вывести
            'суповой набор'. Корзина - массив
        """
        if 'яблоки' in bucket or 'груши' in bucket or 'апельсины' in bucket:
            return 'Фрукты'
        elif 'специи' in bucket and 'овощи' in bucket and 'мясо' in bucket:
            return 'Суповой набор'
        else:
            return 'В корзине не то, что нам нужно'
