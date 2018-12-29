from functools import wraps
from time import sleep
from typing import TextIO

from ampy.pyboard import Pyboard, PyboardError
from serial.serialposix import Serial


def run_code(board, code):
    try:
        board.exec_(code)
    except PyboardError as e:
        if 'timeout waiting for first EOF reception' not in str(e):
            print(e)
            print('Trying again in 1 second...')
            sleep(1)
            print('Trying again.')
            run_code(board, code)


class MySerial:
    def __init__(self, original: Serial, file: TextIO):
        self.original = original
        self.file = file
    
    def __getattr__(self, attr):
        original = getattr(self.original, attr)
        
        @wraps(original)
        def f(*args, **kwargs):
            result = original(*args, **kwargs)
            self.file.write(f'serial.{attr}(*{args}, **{kwargs}) = {result}\n')
            return result
        
        return f


def main():
    print('Connecting...')
    
    board = Pyboard(
        '/dev/serial/by-id/usb-Adafruit_Industries_LLC_CircuitPlayground_Express_58656DBA3564051502020253E1F111FF-if00')
    
    print('Connected.')
    print('Monkeypatching serial...')
    board.serial = MySerial(board.serial, open('log.log', 'w'))
    print('Serial monkeypatched.')
    
    with open('/home/solly/PycharmProjects/Circuit-Python/code2.py') as f:
        code = f.read()
    
    print('Entering raw REPL...')
    board.enter_raw_repl()
    print('In raw REPL.')
    print('Executing...')
    run_code(board, code)
    board.exec_(code)
    print('Program finished.')
    print('Exiting raw REPL...')
    board.exit_raw_repl()
    print('Exited raw REPL.')
    print('Finishing up...')
    
    print('Done.')


if __name__ == '__main__':
    main()
