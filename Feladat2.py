import codecs as cs
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
def ostok_szama(n):
    db=2
    for i in range(2,n//2+1):
        if n%i==0:
            db=db+1
    return db
def feladat_5(n):
    max=1
    for i in range(2,n+1):
        if max<ostok_szama(i):
            max=ostok_szama(i)
            print(i)

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
def feladat_8(n):
    i=1
    a=0
    db=0
    while True:
        a=a+i
        i=i+1
        db=db+1
        if a>=n:
            break
    print(db)
def feladat_9():
    i=1
    a=0
    while True:
        i=i+1
        a=a+1/i
        if a==300:
            break
    print(i)
def feladat_10():
    try:
        file=cs.open("be.txt",encoding='utf-8',mode="r")
        max=0
        for sor in file:
            sor=sor.strip()
            if (sor[0].isupper())and(len(sor)>max):
                max=len(sor)
        print(max)
        file.close()
    except Exception as e:
        print(e)
def feladat_11():
    try:
        file=cs.open("be.txt",encoding='utf-8',mode="r")
        min=0
        for sor in file:
            sor=sor.strip()
            for i in range(len(sor)):
                if (sor[i]==".") or (sor[i]=="!") or (sor[i]=="?") and (len(sor)<min):
                    min=len(sor)
            print(min)
        file.close()
    except Exception as e:
        print(e)
def feladat_12():
    try:

        file=open("be.txt",mode="r")
        file1=open("ki.txt",mode="w")
        db=1
        for sor in file:
            sor=sor.split(" ")
            for i in range(len(sor)-1):
                if sor[i]==sor[i+1]:
                    db=db+1
            if db>=int(sor[len(sor)-1]):
                file1.write("True")
            else:
                file1.write("False")
        file.close()
        file1.close()
    except Exception as e:
        print(e)
def feladat_13():
    try:
        file=open("be.txt",mode="r")
        db=0
        for sor in file:
            sor=sor.split(" ")
            for i in range(len(sor)-1):
                for j in range(i+1,len(sor)-1):
                    a=int(sor[i])
                    b=int(sor[j])
                    c=int(sor[len(sor)-1])
                    if abs(a-b)<=c:
                        db=db+1
            print(db)
        file.close()
    except Exception as e:
        print(e)
def feladat_15():
    try:
        file = open("be.txt", mode="r")
        file1 = open("ki.txt", mode="w")
        for sor in file:
            sor=sor.strip()
            if sor != "":
                    sor=sor.split(" ")
            else:
                break
            for i in sor:
                file1.write("%s\n" % (i))
        file.close()
        file1.close()
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)
def feladat_16():
    try:
        file=cs.open("be.txt",encoding='utf-8',mode="r")
        file1=open("ki.txt",mode="w")
        nagy=True
        for sor in file:
            sor=sor.strip()
            li=sor.split(" ")
            for szo in li:
                if not(szo[0].isupper()):
                    nagy=False
                    break
            if nagy:
                file1.write("%s\n"%(sor))
                break

            else:
                nagy=True
        file.close()
        file1.close()
    except FileExistsError:
        print("file nem létezik")
    except Exception:
        print("valamilyen hibat dobott!")
def feladat_17():
    try:
        file=cs.open("be.txt",encoding='utf-8',mode="r")
        file1=open("ki.txt",mode="w")
        nagy=True
        for sor in file:
            sor=sor.strip()
            li=sor.split(" ")
            for szo in li:
                if not(szo[0].islower()):
                    nagy=False
                    break
            if nagy:
                    sor = str(sor)
                    file1.write(sor)
                    file1.write("\n")
                    break
            else:
                    nagy=True
        file.close()
        file1.close()
    except FileExistsError:
        print("nem letezik a file!")
    except Exception:
        print("valamilyen kivetelt dobott!")
def main():
    print(feladat_11())
    print(feladat_1(8))
    print((feladat_2(5)))
    feladat_3(513)
    feladat_4()
    feladat_5(20)
    print(feladat_6(123, 302))
    print(feladat_7(11, 212))
    feladat_8(7)
    feladat_9()
    feladat_10()
    feladat_11()
    feladat_12()
    feladat_13()
    feladat_15()
    feladat_16()
    feladat_17()
if __name__ == '__main__':
    main()



