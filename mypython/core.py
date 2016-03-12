import printer
import reader
import re
from type import Atom

def malstring2pythonstring(s):
    a = re.search(r"\"((?:\\.|[^\"])*)\"", s)
    return a.group(1)

def readfile(name):
    name = malstring2pythonstring(name)
    ret = "";
    with open(name,"r") as f:
        ret = f.read()
    return ret

def concat(*lst):
    ret = []
    for l in lst:
      ret.extend(l)
    return ret

def nth(lst,idx):
    if idx<0 or idx>=len(lst):
        raise "out of range"
    else:
        return lst[idx]

def rest(lst):
    if len(lst)<2:
        return []
    else:
        return lst[1:len(lst)]

ns = {
    "+": lambda x,y: x+y
    ,"-": lambda x,y: x-y
    ,"*": lambda x,y: x*y
    ,"/": lambda x,y: x/y
    ,"nil": "nil"
    ,"not": lambda x: not ((type(x)==bool and x) or (type(x)!=bool and x!="nil"))
    ,"list": lambda *l: [*l]
    ,"list?": lambda lst: isinstance(lst,list)
    ,"empty?": lambda lst: len(lst)==0
    ,"count": lambda lst: len(lst) if type(lst)==list else 0
    ,"=": lambda x,y: x==y
    ,">": lambda x,y: x>y
    ,"<": lambda x,y: x<y
    ,">=": lambda x,y: x>=y
    ,"<=": lambda x,y: x<=y
    ,"read-string": lambda s: reader.read_str(malstring2pythonstring(s))
    ,"slurp": lambda fname:"\""+readfile(fname)+"\""
    ,"str": lambda *x: "\""+"".join([malstring2pythonstring(printer.pr_str(v,False)) for v in x])+"\""
    ,"atom": lambda v:Atom(v)
    ,"atom?": lambda a:isinstance(a,Atom)
    ,"deref": lambda a:a.value
    ,"reset!": lambda a,v:a.reset(v)
    ,"swap!": lambda a,f,*arg:a.reset(f(a.value,*arg) if not isinstance(f,dict) else f["fn"](a.value,*arg))
    ,"cons": lambda a,lst: [a,*lst]
    ,"concat": concat
    ,"nth": nth
    ,"first": lambda lst:"nil" if len(lst)==0 or lst=="nil" else nth(lst,0)
    ,"rest": rest
}
