import sys
import readline
from more_itertools import chunked

import reader
import printer
from env import Env

DEBUG = False

repl_env = Env()
repl_env.set("+", lambda x,y: x+y)
repl_env.set("-", lambda x,y: x-y)
repl_env.set("*", lambda x,y: x*y)
repl_env.set("/", lambda x,y: int(x/y))

def eval_ast(ast,env):
    if isinstance(ast,str):
        return env.get(ast)
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

    if not isinstance(ast,list):
        evaled = eval_ast(ast, env)
        return evaled
    else:
        f = ast[0]
        if f=="def!":
            v = EVAL(ast[2],env)
            env.set(ast[1], v)
            return v
        elif f=="let*":
            bindings = ast[1]
            if DEBUG:
                print("bindings: "+str(bindings))
            if len(bindings)%2!=0:
                raise

            cenv = Env()
            cenv.outer = env
            for k,vast in chunked(bindings,2):
                v = EVAL(vast,cenv)
                cenv.set(k,v)
                new_env = Env()
                new_env.outer = cenv
                cenv = new_env

            return EVAL(ast[2],cenv)
        else:
            evaled = eval_ast(ast, env)
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
