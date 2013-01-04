# Filename: tail.py
'''usage：tail.py <filename>'''
import sys
import time
if len(sys.argv) < 2:
    print('len(sys.argv) < 2 !!! No file to tail..')
else:
    with open(sys.argv[1]) as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                time.sleep(5)
            else:
                print(line, end=' ')
