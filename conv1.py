def convert(l):
    s = ''
    for i in l:
        count = 0
        for j in i:
            count += 1
            s += s.join(j)
            if count==1: s += s.join('=')
        s += ';'
    return s

print(convert([('a','b'),('c','d'),('e','f'),('g','h')]))
