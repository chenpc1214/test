def upper(func):
    def newfunc(args):
        olderesult = func(args)
        newresult = olderesult.upper()
        return newresult
    return newfunc

def bold(func):
    def wrapper(args):
        return "bold"+func(args)+"bold"
    return wrapper

def italic(func):
    def wrapper(args):
        return "italic"+func(args)+"italic"
    return wrapper
    

@italic
@bold
@upper
def greeting(args):
    return args


print(greeting("Hello! iPhone"))
