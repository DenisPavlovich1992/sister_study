def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

str = ""

def simplify_fraction(numerator, denominator):
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

def add_fractions(expression):
    terms = expression.split('+')
    total_numerator, total_denominator = 0, 1

    for term in terms:
        numerator, denominator = map(int, term.split('/'))
        total_numerator = total_numerator * denominator + numerator * total_denominator
        total_denominator *= denominator

    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator

def subtract_fractions(expression):
    terms = expression.split('-')
    total_numerator, total_denominator = 0, 1

    # Из первого слагаемого вычитаем остальные
    for i, term in enumerate(terms):
        if i == 0:
            # Если это первое слагаемое, просто добавляем его
            numerator, denominator = map(int, term.split('/'))
            total_numerator = numerator * total_denominator
            total_denominator *= denominator
        else:
            # Если это не первое слагаемое, вычитаем его
            numerator, denominator = map(int, term.split('/'))
            total_numerator -= numerator * total_denominator

    # Если результат отрицательный, преобразуем его в отрицательную дробь
    if total_numerator < 0:
        total_numerator = -total_numerator
        total_denominator = -total_denominator

    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator


def multiply_fractions(expression):
    terms = expression.split('*')
    total_numerator, total_denominator = 1, 1

    for term in terms:
        numerator, denominator = map(int, term.split('/'))
        total_numerator *= numerator
        total_denominator *= denominator

    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator

def divide_fractions(expression):
    terms = expression.split('/')
    total_numerator, total_denominator = 1, 1

    # Первое слагаемое является числителем, остальные - знаменателями
    for i, term in enumerate(terms):
        if i == 0:
            total_numerator *= int(term)
        else:
            total_denominator *= int(term)

    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
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