def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

def add_fractions(expression):
    terms = expression.split('+')
    result_numerator, result_denominator = 0, 1

    for term in terms:
        if '/' in term:
            numerator, denominator = map(int, term.split('/'))
            result_numerator = result_numerator * denominator + numerator * result_denominator
            result_denominator *= denominator
        else:
            # Если нет "/", значит это целое число, прибавляем его к результату
            result_numerator += int(term)

    return result_numerator, result_denominator

def subtract_fractions(expression):
    terms = expression.split('-')
    result_numerator, result_denominator = 0, 1

    # Из первого слагаемого вычитаем остальные
    for i, term in enumerate(terms):
        if '/' in term:
            numerator, denominator = map(int, term.split('/'))
            if i == 0:
                result_numerator = numerator * result_denominator
            else:
                result_numerator -= numerator * result_denominator
            # Если это не первый элемент, вычитаем его из результата
            if i != 0:
                result_numerator += numerator * result_denominator
            result_denominator *= denominator
        else:
            # Если нет "/", значит это целое число
            if i == 0:
                result_numerator += int(term) * result_denominator
            else:
                result_numerator -= int(term) * result_denominator

    return result_numerator, result_denominator

def multiply_fractions(expression):
    terms = expression.split('*')
    result_numerator, result_denominator = 1, 1

    for term in terms:
        if '/' in term:
            numerator, denominator = map(int, term.split('/'))
            result_numerator *= numerator
            result_denominator *= denominator
        else:
            # Если нет "/", значит это целое число
            result_numerator *= int(term)

    return result_numerator, result_denominator

def divide_fractions(expression):
    terms = expression.split('/')
    result_numerator, result_denominator = 1, 1

    # Первое слагаемое является числителем, остальные - знаменателями
    for i, term in enumerate(terms):
        if '/' in term:
            numerator, denominator = map(int, term.split('/'))
            if i == 0:
                result_numerator *= numerator
            else:
                result_denominator *= numerator
                result_numerator *= denominator
        else:
            # Если нет "/", значит это целое число
            if i == 0:
                result_numerator *= int(term)
            else:
                result_denominator *= int(term)

    return result_numerator, result_denominator


while(True):
    user_input = input("Введите выражение с дробями (например, 1/3 + 2/5 с пробелами): ")  # Получение ввода от пользователя
    parts = user_input.split(" ")  # Разделение введенного выражения на части
    operator = parts[1]
    # Выполняем операцию
    match operator:  # Проверка оператора
        case '+':  # Сложение
            print(add_fractions(user_input)[0], "/", add_fractions(user_input)[1])
        case '-':  # Вычитание
          print(subtract_fractions(user_input)[0], "/", subtract_fractions(user_input)[1])
        case '*':  # Умножение
            print(multiply_fractions(user_input)[0], "/", multiply_fractions(user_input)[1])
        case '/':  # Деление
            print(divide_fractions(user_input)[0], "/", divide_fractions(user_input)[1])
        case _:  # Неподдерживаемая операция
            print("Неподдерживаемая операция")