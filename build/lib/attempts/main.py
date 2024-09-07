import datetime
import builtins

attempts_instance = None
default_timestamp_start = "["
default_timestamp_end = "]"
default_timestamp_format = "%H:%M:%S.%f"


class Attempts:
    def __init__(self,
                 replace_print,
                 timestamp_start=default_timestamp_start,
                 timestamp_end=default_timestamp_end,
                 timestamp_format=default_timestamp_format):
        
        self.timestamp_format = timestamp_format
        self.timestamp_end = timestamp_end
        self.timestamp_start = timestamp_start
        self.original_print = builtins.print
        
        if replace_print:
            self.replace_print()

    def attempts_print(self, *args, **kwargs):

        timestamp = datetime.datetime.now().strftime(self.timestamp_format)
        self.original_print(f"{self.timestamp_start}{timestamp}{self.timestamp_end}", *args, **kwargs)

    def replace_print(self):
        builtins.print = self.attempts_print

def init( 
        replace_print: bool,
        timestamp_start: str = default_timestamp_start,
        timestamp_end: str = default_timestamp_end,
        timestamp_format: str = default_timestamp_format):
    
    global attempts_instance

    attempts_instance = Attempts(replace_print,
                                 timestamp_start,
                                 timestamp_end,
                                 timestamp_format)

def printt(*args, **kwargs):
    if attempts_instance is not None:
        attempts_instance.attempts_print(*args, **kwargs)
    else:
        raise RuntimeError("Attempts not initialized. Call attempts.init() first.")
