import datetime


class context_time:

    def __init__(self, ):
        self.time_now = datetime.datetime.utcnow()

    def __enter__(self):
        print(f'Начало работы(utc): {self.time_now}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is not None:
            print(f'Error: {exc_val}')

        print(f'Конец работы(utc): {datetime.datetime.utcnow()}\n'
              f'Время работы: {datetime.datetime.utcnow() - self.time_now}')