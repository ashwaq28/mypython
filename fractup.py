def add(t1,t2):
    if(t1[1]==t2[1]):
        t3=((t1[0]+t2[0]),t2[1])
        return(t3)
    else: 
        t4=(((t1[0]*t2[1])+(t1[1]*t2[0])),(t1[1]*t2[1]))
        return(t4)

def main():
    t1=(1,2)
    t2=(2,3)
    t5=add(t1,t2)
    print(t5)
main()
