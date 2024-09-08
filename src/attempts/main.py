import datetime
import builtins
from colorama import Fore, Style, init as colorama_init

attempts_instance = None
default_timestamp_start = "["
default_timestamp_end = "]"
default_timestamp_format = "%H:%M:%S.%f"
default_timestamp_color = "GREEN"


class Attempts:
    def __init__(self,
                 replace_print,
                 timestamp_start=default_timestamp_start,
                 timestamp_end=default_timestamp_end,
                 timestamp_format=default_timestamp_format,
                 timestamp_color=default_timestamp_color):
        
        self.timestamp_format = timestamp_format
        self.timestamp_end = timestamp_end
        self.timestamp_start = timestamp_start
        self.original_print = builtins.print
        self.timestamp_color = timestamp_color
        colorama_init(autoreset=True)
        
        if replace_print:
            self.replace_print()

    def attempts_print(self, *args, **kwargs):

        timestamp = datetime.datetime.now().strftime(self.timestamp_format)
        formatted_timestamp = f"{self.timestamp_color}{self.timestamp_start}{timestamp}{self.timestamp_end}{Style.RESET_ALL}"
        self.original_print(f"{formatted_timestamp}", *args, **kwargs)

    def replace_print(self):
        builtins.print = self.attempts_print


def init( 
        replace_print: bool,
        timestamp_start: str = default_timestamp_start,
        timestamp_end: str = default_timestamp_end,
        timestamp_format: str = default_timestamp_format,
        timestamp_color: str = default_timestamp_color):
    
    global attempts_instance

    colorama_color = convert_to_colorama_color(timestamp_color)

    attempts_instance = Attempts(replace_print,
                                 timestamp_start,
                                 timestamp_end,
                                 timestamp_format,
                                 colorama_color)
    
def convert_to_colorama_color(color): 
    color = color.upper()
    if color not in Fore.__dict__:
        import warnings
        warnings.warn(f"Invalid color: {color}. Defaulting to white. Available colors: {', '.join(Fore.__dict__.keys())}")
        return Fore.WHITE
    return Fore.__dict__[color]


def printt(*args, **kwargs):
    if attempts_instance is not None:
        attempts_instance.attempts_print(*args, **kwargs)
    else:
        raise RuntimeError("Attempts not initialized. Call attempts.init() first.")
