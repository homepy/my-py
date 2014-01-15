# Filename: tail.py
'''only for windows    usage：tail.py <filename>'''
import sys
import time


assert len(sys.argv) >= 2, 'sys.argv[1] should be a file...'
with open(sys.argv[1]) as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(5)
        else:
            print(line, end=' ')
