# Функция для нахождения наибольшего общего делителя (алгоритм Евклида)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Функция для упрощения дроби
def simplify_fraction(numerator, denominator):
    common = gcd(numerator, denominator)
    # Деление числителя и знаменателя на их наибольший общий делитель
    return numerator // common, denominator // common


# Функция для сложения дробей
def add_fractions(expression):
    terms = expression.split('+')
    total_numerator, total_denominator = 0, 1

    for term in terms:
        numerator, denominator = map(int, term.split('/'))
        # Обновление числителя и знаменателя суммы
        total_numerator = total_numerator * denominator + numerator * total_denominator
        total_denominator *= denominator

    # Упрощение результата
    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator


# Функция для вычитания дробей
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

    # Упрощение результата
    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator


# Функция для умножения дробей
def multiply_fractions(expression):
    terms = expression.split('*')
    total_numerator, total_denominator = 1, 1

    for term in terms:
        numerator, denominator = map(int, term.split('/'))
        # Умножение числителя и знаменателя
        total_numerator *= numerator
        total_denominator *= denominator

    # Упрощение результата
    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator


# Функция для деления дробей
def divide_fractions(expression):
    terms = expression.split('/')
    total_numerator, total_denominator = 1, 1

    # Первое слагаемое является числителем, остальные - знаменателями
    for i, term in enumerate(terms):
        if i == 0:
            total_numerator *= int(term)
        else:
            total_denominator *= int(term)

    # Упрощение результата
    result_numerator, result_denominator = simplify_fraction(total_numerator, total_denominator)
    return result_numerator, result_denominator


# Основной цикл программы
while True:
    # Получение ввода от пользователя
    user_input = input("Введите выражение с дробями (например, 1/3 + 2/5 с пробелами): ")

    # Разделение введенного выражения на части
    parts = user_input.split(" ")
    operator = parts[1]  # Получение оператора

    # Выполнение операции в зависимости от оператора
    match operator:
        case '+':
            # Выполнение сложения и вывод результата
            result = add_fractions(user_input)
            print(f"Результат сложения: {result[0]}/{result[1]}")
        case '-':
            # Выполнение вычитания и вывод результата
            result = subtract_fractions(user_input)
            print(f"Результат вычитания: {result[0]}/{result[1]}")
        case '*':
            # Выполнение умножения и вывод результата
            result = multiply_fractions(user_input)
            print(f"Результат умножения: {result[0]}/{result[1]}")
        case '/':
            # Выполнение деления и вывод результата
            result = divide_fractions(user_input)
            print(f"Результат деления: {result[0]}/{result[1]}")
        case _:
            # В случае неподдерживаемой операции выводится сообщение
            print("Неподдерживаемая операция")
