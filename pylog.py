from datetime import datetime
import os

class PyLog:
    def __init__(self):
        if not os.path.exists('logs'):
            os.mkdir('logs')

    def get_time(self):
        log_time = datetime.now()
        log_time_dict = {
            'hour': log_time.hour if log_time.hour >= 10 else f'0{log_time.hour}',
            'minute': log_time.minute if log_time.minute >= 10 else f'0{log_time.minute}',
            'second': log_time.second if log_time.second >= 10 else f'0{log_time.second}'
        }
        return f'[{log_time_dict["hour"]}:{log_time_dict["minute"]}:{log_time_dict["second"]}]'

    def get_log_time(self):
        log_time = datetime.now()
        log_time_dict = {
            'hour': log_time.hour if log_time.hour >= 10 else f'0{log_time.hour}',
            'minute': log_time.minute if log_time.minute >= 10 else f'0{log_time.minute}',
            'second': log_time.second if log_time.second >= 10 else f'0{log_time.second}'
        }
        return log_time, f'[{log_time_dict["hour"]}:{log_time_dict["minute"]}:{log_time_dict["second"]}]'

    def log_file_exists(self, path):
        return os.path.exists(path)

    def format_log_file_name(self, log_time):
        return f'{log_time.day}_{log_time.month}_{log_time.year}.log'

    def format_log_value(self, log_time, value):
        if not type(value) == list and not type(value) == dict:
            return f'{log_time} {value}\n'

        return f'{log_time} {value}'

    def write_to_log_file(self, path, value, flag, value_type):
        file = open(path, flag)
        if not value_type == list and not value_type == dict:
            file.write(value)
        else:
            file.write(value)
            file.write('\n')
        file.close()

    def log(self, value):
        log_time = self.get_log_time()
        filename = self.format_log_file_name(log_time[0])
        path = f'logs/{filename}'

        if not self.log_file_exists(path):
            self.write_to_log_file(path, '', 'x', str)

        self.write_to_log_file(path, self.format_log_value(log_time[1], value), 'a', type(value))
        return

