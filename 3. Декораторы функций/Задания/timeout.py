import threading
from functools import wraps

import time
def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            def target():
                result = func(*args, **kwargs)
            thread = threading.Thread(target = target)
            thread.daemon = True
            thread.start()
            thread.join(timeout = seconds)
            if thread.is_alive():
                raise TimeoutError('Функция выполняется слишком долго')