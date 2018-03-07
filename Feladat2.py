def feladat_11():
    ev1=int(input("ev_1:"))
    ho1=int(input("honap_1:"))
    nap1=int(input("nap_1:"))
    ev2=int(input("ev_2:"))
    ho2=int(input("honap_2:"))
    nap2=int(input("nap_2:"))
    sum=0
    for i in range(ev1+1,ev2):
        if (i//4==0 and i//100!=0 or i//400==0):
            sum=sum+366
        else:
            sum=sum+365
    for j in range(ho1,13):
        if ho1==2 and ev1//4==0 and ev1//100!=0 or ev1//400==0:
            sum=sum+29
        else:
            sum=sum+28
        if ho1==4 or ho1==6 or ho1==9 or ho1==11:
            sum=sum+30
        else:
            sum=sum+31
    for k in range(1,ho2):
        if ho2==2 and ev2//4==0 and ev2//100!=0 or ev2//400==0:
            sum=sum+29
        else:
            sum=sum+28
        if ho2==4 or ho2==6 or ho2==9 or ho2==11:
            sum=sum+30
        else:
            sum=sum+31
    sum=sum-nap1
    sum=sum+nap2
    return sum
def feladat_1(n):
    db=0
    for i in range(1,n+1):
        if n%i==0:
            db=db+1
    if db==4:
        return True
    else:
        return False

def prim_e(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def feladat_2(n):
    p=[2]
    a=3
    while len(p)<n:
        if prim_e(a):
            p.append(a)
        a=a+1
    return p[n-1]
def feladat_3(n):
    a=1
    while 2*a<n:
        a=a*2
    print(2*a)
def feladat_4():
    a=0
    for i in range(1,10):
        a=a+1
        b=0
        for j in range(9):
            b=b+1
            c=0
            if b!=c and a!=b and c!=a:
                print(a,b,c)
            for x in range(9):
                c=c+1
                if a!=b and b!=c and a!=c:
                    print(a,b,c)



def feladat_6(x,y):
    db=0
    x=str(x)
    y=str(y)
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                db=db+1
    if db>=2:
        return True
    else:
        return False
def feladat_7(x,y):
    db = 0
    x=str(x)
    y=str(y)
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                db=db+1
    if db>=1:
        return True
    else:
        return False
def main():
     print(feladat_11())
     print(feladat_1(8))
     print((feladat_2(5)))
     feladat_3(513)
     feladat_4()
     print(feladat_6(123,302))
     print(feladat_7(11,212))
if __name__ == '__main__':
    main()



