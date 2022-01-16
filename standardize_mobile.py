def wrapper(f):
    def fun(l):
        output = []
        for num in l:
            output.append('+91 ' + num[-10 : -5] + ' ' + num[-5: ])
        f(output)
    return fun
