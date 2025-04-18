class BlockErrors:
    def __init__(self, ignored_exceptions):
        self.ignored_exceptions = ignored_exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.ignored_exceptions:

            return True
        return False

# Тесты
def test_block_errors():
    import traceback
    import io

    err_types = {ZeroDivisionError}
    try:
        with BlockErrors(err_types):
            a = 1 / 0
        print('Тест 1: Выполнено без ошибок')
    except Exception as e:
        print('Тест 1: Неожиданная ошибка:', e)

    err_types = {ZeroDivisionError}
    try:
        with BlockErrors(err_types):
            a = 1 / '0'
        print('Тест 2: Выполнено без ошибок')
    except Exception as e:
        print('Тест 2: Поймано исключение:', e)

    outer_err_types = {TypeError}
    try:
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}
            try:
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                print('Тест 3: Внутренний блок: выполнено без ошибок')
            except Exception as e:
                print('Тест 3: Неожиданная ошибка в внутреннем блоке:', e)
        print('Тест 3: Внешний блок: выполнено без ошибок')
    except Exception as e:
        print('Тест 3: Поймано исключение:', e)

    err_types = {Exception}
    try:
        with BlockErrors(err_types):
            a = 1 / '0'
        print('Тест 4: Выполнено без ошибок')
    except Exception as e:
        print('Тест 4: Неожиданная ошибка:', e)

test_block_errors()