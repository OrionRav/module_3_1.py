# Домашняя работа по уроку "Пространство имён"

# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!

# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

calls = 0   # создание переменной calls
def count_calls():      # создание функции count_calls
    global calls        # изменение значения переменной calls
    calls += 1          # подсчет остальных функций

def string_info(string):    # создание функции string_info
    count_calls()           # вызов функции из первой
    string = str(string)    # принимает аргумент - строку
    i = (len(string), string.upper(), string.lower())   # возвращает кортеж из:
    return i                            # длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

def is_contains(string, list_to_search):    # создание функции is_contains
    count_calls()                           # вызов функции из первой
    string = str(string).lower()            # принимает аргумент-строку в нижнем регистре
    list_to_search = list(list_to_search)   # принимает аргумент-список
    for j in range(len(list_to_search)):            # для j в последовательности длины списка
        if str(list_to_search[j]).lower() == string:    # если строка в списке с j (с нижним регистром) равна строке
            i = True                                    # то правда
            break                                       # закончить
        else:                                           # иначе
            i = False                                   # ложь
            continue                                    # продолжить
    return i                                            # вернуться ко второй функции

# вывод на консоль
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))   # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches
print(calls)