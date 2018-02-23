import math as mt
def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
def feladat_2():
    a=int(input("első szám:"))
    b=int(input("második:"))
    c=int(input("harmadik:"))
    if a>b and a>c and b>c:
        print(c,b,a)
    elif a>b and a>c and b<c:
        print(b,c,a)
    elif a>b and a<c and b<c:
        print(b,a,c)
    elif a<b and a<c and b<c:
        print(a,b,c)
    elif a<b and a<c and b>c:
        print(a,c,b)
    elif a<b and a>c and b>c:
        print(c,a,b)
def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    else:
        print("Hiba")
def feladat_4(x,y,z):
    min=0
    if x<y:
        if y<z:
            min=x
        elif y>z and x<z:
            min=x
        else:
            min=z
    elif x>y:
        if y<z:
            min=y
        else:
            min=z
    elif x==y and y==z:
        min=x
    print("minimum:",min)
    max=0
    x=abs(x)
    y=abs(y)
    z=abs(z)
    if x > y:
        if y > z:
            max = x
        elif y < z and x > z:
            max = x
        else:
            max = z
    elif x < y:
        if y > z:
            max = y
        else:
            max = z
    elif x == y and y == z:
        max = x
    print("abs maximuma",max)
def feladat_5(a,b,c,d):
    print(a,b,c,d)
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)
def feladat_6():
    while True:
        a=float(input("1.oldal="))
        b=float(input("2.oldal="))
        c=float(input("3.oldal="))
        if a<=0 or b<=0 or c<=0:
            print("Hibás adatok")
        else:
            break
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c/(4*T)
        print("R=%.2f és r=%.2f"%(R,r))
def feladat_7(hossz,szel,drothossz):
    kerulet=2*(hossz+szel)
    if kerulet==drothossz:
        return 0
    elif kerulet>drothossz:
        sz=kerulet-drothossz
        return sz
    else:
        return drothossz-kerulet
def feladat_8(x,a,b,c,d):
    if x<5:
        print(3*x-5)
    elif x>=5 and x<=10:
        print(10)
    elif x>10:
        print(9*x+1)
    if a+c>2*d and b>0:
        print(d-3*b)
    elif a+c<2*d and b<0:
        print(d+3*b)
    else:
        print(4)
def feladat_9(a,b,c):
    delta=b*b-4*a*c
    if delta==0:
        return -b/(2*a)
    elif delta<0:
        return "Nincs valós megoldás"
    else:
        return "%.2f %.2f"%((-b+mt.sqrt(delta))/(2*a),(-b-mt.sqrt(delta))/(2*a))
def feladat_10(a,b):
    i=1
    s=1
    v=abs(a-b)
    while i<v:
        if i%4==0 and i%100!=0:
            s=s+1
        i = i + 1
    print(s)
def feladat_12(pontszam,maximum_pontszam):
    if pontszam>maximum_pontszam*0.6:
        print("Sikeres")
    else:
        print("Sikertelen")
def feladat_13(jegy):
    if jegy==1:
        print("Elégtelen")
    elif jegy==2:
        print("Elégséges")
    elif jegy==3:
        print("Közepes")
    elif jegy==4:
        print("Jó")
    elif jegy==5:
        print("Jeles")
    else:
        "Hibás adatok"
def feladat_14(sorszam):
    if sorszam==1:
        print("Január")
    elif sorszam==2:
        print("Február")
    elif sorszam==3:
        print("Március")
    elif sorszam==4:
        print("Április")
    elif sorszam==5:
        print("Május")
    elif sorszam==6:
        print("Június")
    elif sorszam==7:
        print("Július")
    elif sorszam==8:
        print("Augusztus")
    elif sorszam==9:
        print("Szeptember")
    elif sorszam==10:
        print("Október")
    elif sorszam==11:
        print("November")
    elif sorszam==12:
        print("December")
    else:
        print("Hibás adatok")
def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados=hanyados+1
        a=a-b
    return hanyados
def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a
def feladat_17(szam):
    m=szam
    uj=0
    while szam>0:
        b=szam%10
        uj=uj*10+b
        szam=szam//10
    return uj==m
def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2!=0:
            p=p+y
        x=x//2
        y=y+y
    return p
def feladat_19(n):
    v=True
    if n==1:
        v=False
    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            v=False
            break
    return v
def feladat_20_1(n):
    x=1
    y=1
    if n==1:
        print(x,end=" ")
    elif n==2:
        print(x,y,end=" ")
    else:
        z=x+y
        print(x,y,z,end=" ")
        k=3
        while k<n:
            x=y
            y=z
            z=x+y
            print(z,end=" ")
            k=k+1
def feladat_20_2(n):
    x=1
    y=1
    k=1
    print()
    while k<=n:
        print(y,end=" ")
        x=x+y
        y=x-y
        k=k+1
def feladat_21(n):
    ujszam=0
    while n!=0:
        ujszam=ujszam*10+n%10
        n=n//10
    return ujszam

def feladat_22(alap,kitevo):
    eredmeny=1
    while kitevo>0:
        if kitevo%2!=0:
            eredmeny=eredmeny*alap
            kitevo=kitevo-1
        alap=alap*alap
        kitevo=kitevo//2
    return eredmeny
def main():
    feladat_1(5,2)
    feladat_2()
    print(feladat_3(1.5))
    feladat_4(-1,-1,-1)
    feladat_5(1,-3,-2,5)
    feladat_6()
     print(feladat_7(2,3,8))
    feladat_8(4,1,-2,3,4)
    print(feladat_9(3,4,1))
    feladat_10(1900,2020)
    feladat_12(60,100)
    feladat_13(3)
    feladat_14(4)
    print(feladat_15(15,5))
    print(feladat_16(360,225))
    print(feladat_17(11))
    print(feladat_18(45,17))
    print(feladat_19(11))
    feladat_20_1(5)
    print()
    feladat_20_2(5)
    print()
    print(feladat_21(135))
    print(feladat_22(3,4))
if __name__ == '__main__':
    main()
