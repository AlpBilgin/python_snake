import os , sys

clear_console = 'clear' if os.name == 'posix' else 'CLS'

def console_dump(scan):
    os.system(clear_console)
    sys.stdout.write(scan)
    sys.stdout.flush()