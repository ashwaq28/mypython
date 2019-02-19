def compBool(a,b,c):
    if((a>b) and (a>c)):
        print(str(a) + "is largest")
    if((b>c) and (b>a)):
        print(str(b) + "is largest")
    if((c>a) and (c>b)):
        print(str(c) + "is largest")

compBool(6,5,8)

