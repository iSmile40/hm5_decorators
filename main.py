import datetime
import os

def logger(log_path):
    def decorator_func(func):
        def wrapper_func(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'Имя функции - {func.__name__} \n')
                date_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                f.write(f'Дата и время вызова функции - {date_time} \n')
                f.write(f'Аргументы функции - {args}, {kwargs} \n')
                f.write(f'Результат - {result} \n')
                f.write(f'Путь к логам - {os.path.abspath(log_path)} \n')
                f.write(f'-------\n')
            return result
        return wrapper_func
    return decorator_func


@logger('logs.txt')
def func_country(name_country):
    result = name_country.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/' + result
    return f'{result}: {url}'

func_country('French Southern and Antarctic Lands')
