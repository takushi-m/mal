import re
import sys
import readline
from more_itertools import chunked

import reader
import printer
import core
from env import Env

DEBUG = False

def eval_ast(ast,env):
    if isinstance(ast,str):
        if re.search(r"\"(?:\\.|[^\"])*\"", ast)!=None:
            return ast
        else:
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
    while True:
        if DEBUG:
            print("EVAL: "+str(ast))

        if not isinstance(ast,list):
            evaled = eval_ast(ast, env)
            return evaled

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
                new_env = Env(cenv)
                cenv = new_env

            ast = ast[2]
            env = cenv
            #return EVAL(ast[2],cenv)
        elif f=="do":
            eval_ast(ast[1:-1],env)
            ast = ast[-1]
        elif f=="if":
            cond = EVAL(ast[1],env)
            if (type(cond)==bool and cond) or (type(cond)!=bool and cond!="nil"):
                ast = ast[2]
            elif len(ast)==3:
                ast = "nil"
            else:
                ast = ast[3]
        elif f=="fn*":
            # (fn* (x y) (+ x y))
            binds = ast[1]
            body = ast[2]
            if DEBUG:
                print("function| binds: "+str(binds)+". body: "+str(body))
            fn = lambda *param:EVAL(body,Env(env,binds,param))
            return {
                "ast": body
                ,"params": binds
                ,"env": env
                ,"fn": fn
                ,"__fn__": True
            }
        else:
            evaled = eval_ast(ast, env)
            f = evaled[0]
            p = evaled[1:]
            if type(f)==dict:
                ast = f["ast"]
                env = Env(f["env"],f["params"],p)
            else:
                return f(*p)


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
    repl_env = Env()
    for k,v in core.ns.items():
        repl_env.set(k,v)
    repl_env.set("eval", lambda ast:EVAL(ast, repl_env))

    rep("(def! load-file (fn* (f) (eval (read-string (str \"(do \" (slurp f) \")\")))))")

    while True:
        try:
            line = input("user> ")
            output = rep(line)
            print(output)
        except EOFError as e:
            break
        except Exception as e:
            print(e)
