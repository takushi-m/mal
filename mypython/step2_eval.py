import sys
import readline

import reader
import printer

DEBUG = False

repl_env = {
    "+": lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "*": lambda x,y: x*y,
    "/": lambda x,y: int(x/y)
}

def eval_ast(ast,env):
    if isinstance(ast,str):
        return env[ast]
    elif isinstance(ast,list):
        return [EVAL(x,env) for x in ast]
    else:
        return ast

def READ(line):
    res = reader.read_str(line)
    if DEBUG:
        print("READ: "+str(res))
    return res

def EVAL(ast, env):
    if DEBUG:
        print("EVAL: "+str(ast))
    evaled = eval_ast(ast, env)
    if not isinstance(ast,list):
        return evaled
    else:
        return evaled[0](*evaled[1:])


def PRINT(line):
    res = printer.pr_str(line)
    if DEBUG:
        print("PRINT: "+str(res))
    return res

def rep(line):
    ast = READ(line)
    y = EVAL(ast,repl_env)
    z = PRINT(y)
    return z


if __name__ == '__main__':
    while True:
        try:
            line = input("user> ")
            output = rep(line)
            print(output)
        except EOFError as e:
            break
        except Exception as e:
            print(e)
