import os , sys

clear_console = 'clear' if os.name == 'posix' else 'CLS'

def console_draw(raster:str, width:int = 80):
    scan = '\n'.join(raster[i:i+width] for i in range(0, len(raster), width))
    os.system(clear_console)
    sys.stdout.write(scan)
    sys.stdout.flush()

def _test():
    console_draw('test',2)

if __name__ == '__main__':
    _test()
    

