def pr_str(mal_data):
    res = []
    if not isinstance(mal_data, list):
        return str(mal_data)

    for tk in mal_data:
        if isinstance(tk,list):
            res.append(pr_str(tk))
        else:
            res.append(str(tk))
    return "("+" ".join(res)+")"
