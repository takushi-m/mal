import printer

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
}
