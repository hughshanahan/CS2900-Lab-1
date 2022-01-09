def check_orthogonal(u, v):
    return u.dot(v) == 0


def check_p():
    import inspect
    import re
    local_vars = inspect.currentframe().f_back.f_locals
    return len(re.findall("p\\s*=\\s*0", str(local_vars))) == 0
