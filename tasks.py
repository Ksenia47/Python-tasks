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


string_tasks = StringTasks()

# Заменить в строке все вхождения слова «бяка» на «вырезано цензурой».
# "Вчера было холодно, бяка. Потому мы остались дома, бяка. А так хотелось купаться,
# но вода уже бяка."
# text = 'Вчера было холодно, бяка. Потому мы остались дома, бяка. А так хотелось купаться,' \
#        'но вода уже бяка.'
# answer = string_tasks.replace_word(text)
# print(answer)

# Вырезать слово бяка из строки. Вывевсти обе строки. "Неопрен бяка рвётся сам"
# text = 'Неопрен бяка рвётся сам'
# answer = string_tasks.exscind_word_from_string(text)
# print(answer)

# Обрезать строку в начале и конце, так чтобы осталось только "Лето закончилось".
# Изначальный вариант: "бяка Лето закончилось. бяка".
# text = 'бяка Лето закончилось. бяка'
# answer = string_tasks.substring_first_and_last_words(text)
# print(answer)

# Найти индекс слова бяка в строке. Вывевсти строку и индекс. "Неопрен бяка рвётся сам"
# word = 'бяка'
# text = 'Неопрен бяка рвётся сам'
# answer = string_tasks.get_index_of_word(text, word)
# print(answer)

# Убрать пробелы в начале и конце строки. Вывести результат.
#         "                        Неопрен бяка рвётся сам         "
# text = '                        Неопрен бяка рвётся сам         '
# answer = string_tasks.delete_interval(text)
#
# print(answer)

# Вывести строку в нижнем регистре, вывести первоначальный вариант. "ТИХО СКАЗАЛ"
# text = 'ТИХО СКАЗАЛ'
# answer = string_tasks.get_lower_case(text)
#
# print(answer)

# Вывести строку в верхнем регистре, вывести первоначальный вариант. "Перестань кричать"
# text = 'Перестань кричать'
# answer = string_tasks.get_upper_case(text)
#
# print(answer)

# Вывести строки "Ксюша любит SUP", "Обожаю клеить неопрен" и их длину.
# first_text = 'Ксюша любит SUP'
# second_text = 'Обожает клеить неопрен'
# answer = string_tasks.get_text_and_length(first_text, second_text)
#
# print(answer)
