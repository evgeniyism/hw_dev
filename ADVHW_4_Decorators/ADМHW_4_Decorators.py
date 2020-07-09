from datetime import datetime
import inspect
import os

def function_logger_current_folder(function):
    def logged_function(*args, **kwargs):
        result = function(*args, **kwargs)
        now = datetime.now()
        function_arguments = dict(inspect.signature(function).bind(*args, **kwargs).arguments)
        function_name = function.__name__
        string_to_log = str(
            {'time': str(now), 'function': function_name, 'parameters': function_arguments, 'result': result})
        with open(f'function_{function_name}_calling_log.txt', 'w') as file:
            file.write(string_to_log)
        return result

    return logged_function


def function_logger_new_folder(function):
    path_to_log = input('Choose directory for log file:')
    def logged_function(*args, **kwargs):
        result = function(*args, **kwargs)
        function_arguments = dict(inspect.signature(function).bind(*args, **kwargs).arguments)
        string_to_log = str(
            {'time': str(datetime.now()), 'function': function.__name__, 'parameters': function_arguments, 'result': result})
        if not os.path.exists(path_to_log):
            os.makedirs(path_to_log)
        with open(path_to_log+f'\\function_{function_name}_calling_log.txt', 'w') as file:
            file.write(string_to_log)
        return result
    return logged_function
