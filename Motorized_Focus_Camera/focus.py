import os
import time
import sys
import threading
import readchar
from time import ctime, sleep


def runfocus():

    temp_val = 512
    while True:
        print("press a / z to focus up / down, q to quit:")
        key = readchar.readkey()
        print(repr(key))
        if key == 'a':
            print(temp_val)
            print('UP')
            if temp_val < 1000:
                temp_val += 10
            else:
                temp_val = temp_val
            value = (temp_val<<4) & 0x3ff0
            dat1 = (value>>8)&0x3f
            dat2 = value & 0xf0
            #print("i2cset -y 0 0x0c %d %d" % (dat1, dat2))
            os.system("i2cset -y 0 0x0c %d %d" % (dat1, dat2))
        elif key == 'z':
            print(temp_val)
            print('DOWN')
            if temp_val <12 :
                temp_val = temp_val
            else:
                temp_val -= 10
            value = (temp_val<<4) & 0x3ff0
            dat1 = (value>>8)&0x3f
            dat2 = value & 0xf0
            #print("i2cset -y 0 0x0c %d %d" % (dat1, dat2))
            os.system("i2cset -y 0 0x0c %d %d" % (dat1, dat2))
        elif key == 'q':
            print('Quitting!')
            quit()


if __name__ == "__main__":
    runfocus()