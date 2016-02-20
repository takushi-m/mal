import sys
import readline

def READ(line):
    return line

def EVAL(line):
    return line

def PRINT(line):
    return line

def rep(input):
    x = READ(input)
    y = EVAL(x)
    z = PRINT(y)
    return z


if __name__ == '__main__':
    while True:
        try:
            line = input("user> ")
            output = rep(line)
            print(output)
        except Exception as e:
            break
