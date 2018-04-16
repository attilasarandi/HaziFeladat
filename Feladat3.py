import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
def feladat_1():
    lista=[]
    n=int(input("db szam:"))
    for i in range(n):
        a=int(input())
        lista.append(a)
    for j in range(len(lista)-1):
        if lista[j]==lista[j+1]:
            print(j,j+1)
def feladat_2(n):
    db_paros=0
    db_paratlan=0
    for i in range(n):
        a=int(input())
        if a%2==0:
            db_paros+=1
        if a%2!=0:
            db_paratlan+=1
    print(db_paros/db_paratlan)
def feladat_3(tomb,n):
    db=0
    a=0
    for i in range(n):
        db+=1
        a+=abs(tomb[i])
    print(a/db)
def feladat_4(n):
    db=0
    c=0
    b=1
    for i in range(n):
        a=float(input("szamok="))
        if a>0:
            b=b*a
        elif a<0:
            db+=1
            c+=a
    print("pozitiv szamok szorzata:",b)
    print("negativ szamok szamtani kozeparanyosa:",c/db)
def feladat_5(n):
    c=0
    b=1
    for i in range(n):
        a=float(input("szamok="))
        if a<7:
            b=b*a
        elif a>10:
            c+=a
    print("7-nél kisebbek szorzata:",b)
    print("10-nél nagyobbak osszege:",c)
def feladat_6():
    db=0
    x=0
    y=0
    while True:
        db+=1
        a=int(input("szam: "))
        if x+y==a and y!=0:
            print(a)
        if db%2==0:
            y=a
        if db%2!=0:
            x=a
        if a==0:
            break

def feladat_7():
    lista=[]
    max=0
    x=0
    y=0
    z=0
    while True:
        a=int(input("szam: "))
        if a!=0:
            lista.append(a)
        if a==0:
            break
    for i in range(0,len(lista)-2):
        for j in range(i+1,len(lista)-1):
            for a in range(i+2,len(lista)):
                if ((lista[i]+lista[j]+lista[a])/3)>max and lista[i]!=lista[j] and lista[i]!=lista[a] and lista[j]!=lista[a]:
                    max=((lista[i]+lista[j]+lista[a])/3)
                    x=lista[i]
                    y=lista[j]
                    z=lista[a]
    print(x,y,z)
def feladat_8(tomb,meret):
    for i in range(0,meret-1):
        for j in range(i+1,meret):
            if tomb[i]>tomb[j]:
                return False
    return True

def lnko(x,y):
    r=x%y
    if r==0:
        return y
    else:
        return lnko(y,r)



def feladat_9(tomb,meret):
    for i in range(meret-1):
        for j in range(i+1,meret):
            if lnko(tomb[i],tomb[j])!=1:
                return 0
            else:
                return 1
def oszto(n):
    db=2
    for i in range(2,n//2+1):
        if n%i==0:
            db+=1
    return db
def feladat_10(tomb,k):
    lista=[]
    meret=len(tomb)
    for i in range(meret-1):
        for j in range(i+1,meret):
            if tomb[i]>tomb[j]:
                tmp=tomb[i]
                tomb[i]=tomb[j]
                tomb[j]=tmp

    for i in range(meret):
        lista.append(oszto(tomb[i]))

    also=0
    felso=meret-1
    while also<=felso:
        kozep=(felso+also)//2
        if k<lista[kozep]:
            felso=kozep-1
            if k<lista[kozep]:
                return kozep

        elif k>lista[kozep]:
            also=kozep+1
            if k<lista[kozep]:
                return kozep
def feladat_11(matrix,n,m):
    for j in range(m):
        db=0
        db1=0
        for i in range(n):
            if matrix[i][j]==0:
                db+=1
            if matrix[i][j]<0:
                db1+=1
        if db1*2>db:
            print(j)
def feladat_12(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if (i+j)!=0:
                if matrix[i][j]%(i+j)==0:
                    print(matrix[i][j])
    print(matrix)
def feladat_13(matrix,n,m):
    for j in range(m):
        min=[m][0]
        for i in range(n):
            if matrix[i][j]<min:
                min=matrix[i][j]
            matrix[i][j]-=min
    print(matrix)
def feladat_14(matrix,n):
    max=0
    for i in range(n):
        for j in range(n):
            if i+j>=n:
                if matrix[i][j]>max:

                    max=matrix[i][j]
    print(max)
def feladat_15(matrix,n):
    db=0
    for i in range(n):
            if matrix[i][i]==0:
                db+=1
    print(matrix)
    if db==n:
        return True
    return False
def feladat_16(matrix,matrix1,n,m):
    for i in range(n):
        for j in range(m):
            matrix1[i][j]=matrix[j][i]
    print(matrix1)
def feladat_17(x):
    a=np.power(-x,3)
    c=np.log(abs(x))
    b=np.power(x,(1/3))*(1/(1+x))*np.power(2,a*c)
    return b
def main():
    feladat_1()
    feladat_2(5)
    n=int(input("n="))
    tomb=np.empty(n,dtype='int')
    for i in range(n):
        tomb[i]=float(input())
    feladat_3(tomb,5)
    feladat_4(5)
    feladat_5(5)
    feladat_6()
    feladat_7()
    n=int(input("n: "))
    tomb=np.empty(n,dtype='float')
    for i in range(n):
        tomb[i]=float(input())
    print(feladat_8(tomb,len(tomb)))
    n=int(input("n: "))
    tomb=np.empty(n,dtype='int')
    for i in range(n):
        tomb[i]=int(input())
    print(feladat_9(tomb,len(tomb)))
    n=int(input("n: "))
    k=int(input("k: "))
    tomb=np.empty(n,dtype='int')
    for i in range(n):
        tomb[i]=int(input())
    print(feladat_10(tomb,k))
    n = int(input("n="))
    m = int(input("m="))
    matrix = np.zeros((n, m), dtype='int')
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(input())
    print(matrix)
    feladat_11(matrix, n, m)
    n = int(input("n: "))
    m = int(input("m: "))
    matrix = np.zeros((n, m), dtype="int")
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(input())
    feladat_12(matrix, n, m)
    n = int(input("n: "))
    m = int(input("m: "))
    matrix = np.zeros((n, m), dtype="int")
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(input())
    print(matrix)
    feladat_13(matrix, n, m)
    n = int(input("n: "))
    matrix = np.zeros((n, n), dtype="int")
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(input())
    print(matrix)
    feladat_14(matrix, n)
    n = int(input("n: "))
    matrix = np.zeros((n, n), dtype="int")
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(input())
    print(feladat_15(matrix, n))
    n = int(input("n: "))
    m = int(input("m: "))
    matrix = np.zeros((n, m), dtype="d")
    for i in range(n):
        for j in range(m):
            matrix[i][j] = (input())
    matrix1 = np.zeros((m, n), dtype="d")
    feladat_16(matrix, matrix1, n, m)
    x = np.arange(-15, 2, 0.1)
    y = feladat_17(x)
    plt.plot(x, y, "b-")
    plt.xlabel('x elemei')
    plt.ylabel('y=f(x) elemei')
    plt.show()
if __name__ == '__main__':
    main()