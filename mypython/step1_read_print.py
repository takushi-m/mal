import sys
import readline

import reader
import printer

DEBUG = False

def READ(line):
    res = reader.read_str(line)
    if DEBUG:
        print("READ: "+str(res))
    return res

def EVAL(line):
    return line

def PRINT(line):
    res = printer.pr_str(line)
    if DEBUG:
        print("PRINT: "+str(res))
    return res

def rep(input):
    x = READ(input)
    y = EVAL(x)
    z = PRINT(y)
    return z


if __name__ == '__main__':
    while True:
        #try:
            line = input("user> ")
            output = rep(line)
            print(output)
        #except Exception as e:
        #    break
