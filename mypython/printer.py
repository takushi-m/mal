import types

def pr_str(mal_data):
    res = []
    if isinstance(mal_data, (types.LambdaType,dict)):
        return "#<function>"
    elif isinstance(mal_data,bool):
        if mal_data:
            return "true"
        else:
            return "false"
    elif isinstance(mal_data,str):
        return str(mal_data)
    elif not isinstance(mal_data, list):
        return str(mal_data)

    for tk in mal_data:
        if isinstance(tk,list):
            res.append(pr_str(tk))
        else:
            res.append(pr_str(tk))
    return "("+" ".join(res)+")"
