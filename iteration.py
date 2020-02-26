class IterationTasks:
    def get_array_inverce(self, array):
        """Вывести массив типа boolean в обратном порядке используя цикл со счётчиком."""
        revers: str = ''
        for i in reversed(array):
            revers = revers + str(i) + ' '
        return revers

    def get_array_to_vacuity(self, array):
        """Массив типа char выводить символы пока не встретится пробел."""
        vacuity = array.index(' ')
        part_array: str = ''
        for i in range(vacuity):
            part_array = part_array + str(array[i]) + ' '
        return part_array

    def get_array_to_vacuity_whit_while(self, array) -> str:
        vacuity = array.index(' ')
        part_array: str = ''
        i = 0
        while i < vacuity:
            part_array = part_array + str(array[i]) + ' '
            i += 1
        return part_array

    def get_factorial(self, n):
        """Дана переменная n. Вывести факториал n."""
        var = 1
        i = 1
        while i <= n:
            var *= i
            i += 1
        return var

    def get_pow_easy(self, x, n):
        """Даны две переменные: x, n. Вычислить x в степени n."""
        pow = x ** n
        return pow

    def get_pow(self, x, n):
        """Даны две переменные: x, n. Вычислить x в степени n."""
        pow = x
        for i in range(1, n):
            pow *= x
        return pow

    def get_all_pow_of_two(self, n):
        """По данному числу N вывести все целые степени двойки, не превосходящие N, в порядке возрастания.
        Например: 1 2 4 8 16 32 для N=52
        """
        base_number = 2
        set_pow = ''
        for i in range(0, n):
            a = base_number ** i
            if a > n:
                break
            pow = base_number ** i
            set_pow += str(pow) + ' '
        return set_pow

    def evaluate_pow_of_two(self, n):
        """Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки,
        или слово NO в противном случае.
        """
        base_number = 2
        pow = 1
        answer = ''
        for i in range(0, n):
            pow *= base_number
            if pow >= n:
                break
        if n == pow:
            answer = 'YES'
        if n != pow:
            answer = 'NO'
        return answer

    def get_sum_elements(self, array):
        """Определите сумму всех элементов последовательности, завершающейся числом 0."""
        sum = 0
        zero = array.index(0)
        for i in range(0, zero):
            sum += array[i]
        return sum

    def get_number_max_elements(self, array):
        """Последовательность состоит из натуральных чисел и завершается числом 0.
        Определите, какое количество элементов этой последовательности равны ее наибольшему элементу.
        """
        max = 0
        number_max_elements = 0
        for i in range(len(array)):
            if array[max] < array[i]:
                max = i
            elif array[max] == array[i]:
                number_max_elements += 1
        return number_max_elements

    def define_number_fib(self, n):
        """По данному числу N определите N-е число Фибоначчи"""
        a = 0
        b = 1
        fib = 1
        for i in range(1, n):
            fib = a + b
            a = b
            b = fib
        return fib

    def define_numeral_fib(self, a):
        """Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
        то есть выведите такое число N, что F(N) = A. Если А не является числом Фибоначчи, выведите число -1
        """
        c = 0
        b = 1
        fib = 1
        for i in range(2, a):
            fib = c + b
            c = b
            b = fib
            if fib >= a:
                break
        if a == fib:
            numeral_fib = i
        else:
            numeral_fib = -1
        return numeral_fib

    def get_mean_array_to_zero(self, array):
        """Определите среднее значение всех элементов последовательности, завершающейся числом 0."""
        zero_position = array.index(0)
        sum = 0
        for i in range(0, zero_position):
            sum += array[i]
        return sum / (i + 1)

    def get_element_whitn_even_index(self, array):
        """Вывести все элементы массива с четными индексами"""
        even_index = ''
        for i in range(0, len(array), 2):
            even_index += str(array[i]) + ' '
        return even_index

    def get_even_elements(self, array):
        """Вывести все четные элементы массива."""
        even_elements = ' '
        for i in range(0, len(array)):
            if array[i] % 2 == 0:
                even_elements += str(array[i]) + ' '
        return even_elements

    def get_quantity_positive_elements(self, array):
        """Найти количество положительных элементов в данном массиве."""
        positive_elements = 0
        for i in range(0, len(array)):
            if array[i] > 0:
                positive_elements += 1
        return positive_elements

    def get_number_more_the_previous(self, array):
        """Дан массив чисел. Выведите все элементы массива, которые больше предыдущего элемента"""
        more_the_previous = ''
        for i in range(0, len(array)):
            if array[i] > array[i - 1]:
                more_the_previous += str(array[i]) + ' '
        return more_the_previous

    def count_pairs_of_equals_elements(self, array):
        """Дан массив чисел. Посчитайте, сколько в нем пар элементов, равных друг другу."""
        count_pairs = 0
        for i in range(0, len(array)):
            for j in range(i + 1, len(array)):
                if array[i] == array[j]:
                    count_pairs += 1
        return count_pairs

    def get_unique_elements(self, array):
        """Дан массив. Выведите те его элементы, которые встречаются в массиве только один раз.
        Элементы нужно выводить в том порядке, в котором они встречаются в списке.
        """
        unique_elements = ''
        for i in array:
            if array.count(i) == 1:
                unique_elements += str(i) + ' '
        return unique_elements

    def get_deposit_remound(self, p, x, y, k):
        """Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада через год.
        Вклад составляет X рублей Y копеек. Определите размер вклада через K лет.
        """
        sum = x * 100 + y
        deposit_remount = 0
        for i in range(k):
            percent = sum / 100 * p
            deposit_remount = sum + percent
            sum = deposit_remount
        return deposit_remount / 100

    def swap_nearby_elements(self, array):
        """Переставьте соседние элементы массива (A[0] c A[1], A[2] c A[3] и т.д.).
        Если элементов нечетное число, то последний элемент остается на своем месте.
        """
        swap_elements = ''
        for i in range(1, len(array), 2):
            array[i - 1], array[i] = array[i], array[i - 1]
            swap_elements = ' '.join([str(i) for i in array])
        return swap_elements

    def get_right_shift(self, array):
        """Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ...,
        последний элемент переходит на место A[0]).
        """
        shift_array = [0 for i in range(len(array))]
        shift_elements = ''
        for i in range(1, len(array)):
            shift_array[i] = array[i - 1]
        shift_array[0] = array[len(array) - 1]
        for i in range(len(array)):
            shift_elements += str(shift_array[i]) + ' '
        return shift_array
