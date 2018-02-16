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
def main():
    feladat_1(5,2)
    feladat_2()
    print(feladat_3(1.5))
    feladat_4(-1,-1,-1)
    feladat_5(1,-3,-2,5)
    feladat_6()
if __name__ == '__main__':
    main()
