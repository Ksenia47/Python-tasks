class StringTasks:
    def get_text_and_length(self, first_text: str, second_text: str):
        """ Вывести строки "Ксюша любит SUP", "Обожаю клеить неопрен" и их длину. """
        all_text = first_text + ' ' + str(len(first_text)) + '\n' + second_text \
                   + ' ' + str(len(second_text))
        return all_text

    def get_upper_case(self, text: str):
        """ Вывести строку в верхнем регистре, вывести первоначальный вариант. "Перестань кричать" """
        all_text = str(text.upper()) + '\n' + text
        return all_text

    def get_lower_case(self, text: str):
        """ Вывести строку в нижнем регистре, вывести первоначальный вариант. "ТИХО СКАЗАЛ" """
        all_text = str(text.lower()) + '\n' + text
        return all_text

    def delete_interval(self, text):
        """ Убрать пробелы в начале и конце строки. Вывести результат.
        "                        Неопрен бяка рвётся сам         "
        """
        not_interval_text = text.strip()
        return not_interval_text

    def get_index_of_word(self, text: str, word: str):
        """ Найти индекс слова бяка в строке. Вывевсти строку и индекс. "Неопрен бяка рвётся сам" """
        index = text.index(word)
        all_text = text + ' ' + str(index)
        return all_text

    def substring_first_and_last_words(self, text):
        """ Обрезать строку в начале и конце, так чтобы осталось только "Лето закончилось".
        Изначальный вариант: "бяка Лето закончилось. бяка".
        """
        first_index = text.find(' ')
        last_index = text.rindex(' ')
        substring = text[first_index:last_index]
        return substring

    def exscind_word_from_string(self, text: str, word: str):
        """ Вырезать слово бяка из строки. Вывевсти обе строки. "Неопрен бяка рвётся сам" """
        index = text.index(word)
        first_substring = text[:index]
        second_substring = text[index + len(word):]
        new_text: str = first_substring + second_substring
        all_text = new_text + '\n' + text
        return all_text

    def replace_word(self, text, word_before: str, word_after: str):
        """ Заменить в строке все вхождения слова «бяка» на «вырезано цензурой».
        "Вчера было холодно, бяка. Потому мы остались дома, бяка. А так хотелось купаться,
        но вода уже бяка."
        :param text: Исходная строка для редактирования
        """
        replace = text.replace(word_before, word_after)
        return replace
