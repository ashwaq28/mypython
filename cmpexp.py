def compExp(a, b, c):
    h = a if(a>b) else b
    high = c if(c>h) else h
    print(high)
    return high

compExp(29,64.7,20.9)
