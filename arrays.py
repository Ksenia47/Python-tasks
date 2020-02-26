class ArraysTasks:
    def get_first_and_last_symbols(self, string):
        """Создать массив символов из строки. Размер массива должен автоматически рассчитываться.
        Вывести первый и последний элементы массива.
        """
        array = list(string)
        first_and_last_symbols = 'Первый символ: ' + array[0] + '\n' + 'Последний символ: ' + array[len(array) - 1]
        return first_and_last_symbols

    def get_central_numeral(self, array):
        """Вывести одну цифру из середины целочисленного массива, если длина массива не чётная,
        *иначе вывести 2 числа из середины.
        """
        if len(array) != 0 and len(array) % 2 == 0:
            middle = len(array) // 2
            central_number = str(array[middle - 1]) + ', ' + str(array[middle])
        elif len(array) != 0 and len(array) % 2 == 1:
            middle = (len(array) - 1) // 2
            central_number = array[middle]
        else:
            central_number = ''
        return central_number
