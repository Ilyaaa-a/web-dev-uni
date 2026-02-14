import datetime
import functools

def function_logger(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # время начала вызова
            start_time = datetime.datetime.now()
            start_str = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")

            # логируем название функции и время вызова
            with open(log_file_path, 'a', encoding='utf-8') as f:
                f.write(f"{func.__name__}\n")
                f.write(f"{start_str}\n")
                f.write(f"{args}\n")
                if kwargs:
                    f.write(f"{kwargs}\n")
                else:
                    f.write("{}\n")

            try:
                # выполняем функцию
                result = func(*args, **kwargs)
                return_value = str(result) if result is not None else "-"
            except Exception as e:
                # если функция выбрасывает исключение... логируем его как результат
                return_value = f"Exception: {e}"
                raise
            finally:
                # время завершения
                end_time = datetime.datetime.now()
                end_str = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")
                duration = end_time - start_time
                # длительность
                duration_str = str(duration)

                # дописываем в файл (результат, время окончания, длительность)
                with open(log_file_path, 'a', encoding='utf-8') as f:
                    f.write(f"{return_value}\n")
                    f.write(f"{end_str}\n")
                    f.write(f"{duration_str}\n")

            return result
        return wrapper
    return decorator

@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'

greeting_format('John')