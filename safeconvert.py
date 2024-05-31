
def convert(inp, typ) -> any:
    out = None
    status = None
    try:
        out = typ(inp)
        status = 0
    except:
        print(f"type {type(inp)} failed conversion to {typ}")
        status = -1

    return out
        