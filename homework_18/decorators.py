def log_args_and_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Arguments: {args}, {kwargs} -> Result: {result}")
        return result
    return wrapper

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper
