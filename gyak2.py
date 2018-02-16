import codecs as cod
def fibo(n):
    a=1
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        c=a+b
        print(a,b,c)
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c)
            k=k+1
def fibo2(n):
    a=1
    b=1
    k=1
    file=open("ki1.txt",mode="w")
    while k<n:
        file.write("%.4f "%(a/b))
        a=a+b
        b=a-b
        k=k+1
    file.close()
def be1_txt(file_nev):
    file=cod.open(file_nev,encoding='utf-8',mode="r")
    max=0
    max_sor=""
    for i in file:
        i=i.strip()
        if (i[0].isupper()and len(i)>max):
            max=len(i)
            max_sor=i
    print(max,max_sor)
    file.close()
def feladat2():
    file=open('be1.txt',mode="r")
    for i in file:
        if ("   " in i):
            file=open("ki1.txt",mode="w")
            file.write(i)
            file.close()
            break
def feladat3(lista,betu):
    li=[]
    file=open("ki2.txt",mode="w")
    for i in lista:
        if i[0]==betu:
            li.append(i)
    file.write(str(li))
    file.close()

def main():
    fibo2(10)
    be1_txt("be1.txt")
    feladat2()
    feladat3( ["alma","ananasz","narancs"],"a")
if __name__ == '__main__':
    main()