from console_dump import console_dump

def console_draw(raster:str, width:int = 80):
    scan = '\n'.join(raster[i:i+width] for i in range(0, len(raster), width))
    console_dump(scan)

def _test():
    console_draw('test',2)

if __name__ == '__main__':
    _test()
    

