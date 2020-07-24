import random
p=1073741789
p2=37
q=random.randint(1,p2-1)
def Hash():
    a=random.randint(0,p-1)+1
    b=random.randint(0,p)
    return a,b

def h_basic(k,j,x1,range):
    x=hash(x1)
    prod = k*x
    prod =prod+j
    y = prod % p
    r =  y % range
    return int(r)

def update(x,f):
    for j in range(deep):
        ws=h_basic(a1[j],b1[j],x,wide)
        a[j][ws]=a[j][ws]+int(f)
        a[j+3][ws]=a[j+3][ws]+int(f)*ws
        a[j+6][ws]=(a[j+6][ws]+int(f)*q**(ws))


def search(x):
    for j in range(deep):
        ws=h_basic(a1[j],b1[j],x,wide)
        f1=a[j][ws]
        if f1==0:
            judge=0
            print(x)
            print(judge)
            break
        fi=a[j+3][ws]
        qi=a[j+6][ws]
        if qi==f1*q**(fi/f1):
            judge=1
            print(x)
            print(judge)
        else:
            judge=0
            print(x)
            print(judge)

def show(x):
    for j in range(deep):
        f=a[j][h_basic(a1[j],b1[j],x,wide)]
        print(x,f)



k=0
wide=0
word=[]
fq=[]
f1=open("material.txt")
word=[0 for i2 in range(wide)]
fq=[0 for i in range(wide)]
for i in f1.readlines():
    for j in i.split():
        if k==0:
            k=1
            word.append(j)
        else:
            fq.append(j)
            k=0

h=list(set(word))
for i in h:
    wide+=1
wide=wide**3


a1=[]
b1=[]
i=0
deep=3
while i<=deep:
    A,B=Hash()
    a1.append(A)
    b1.append(B)
    i=i+1
a = [[0 for i in range(wide)] for i in range(deep*3)]

for i,j in zip(word,fq):
    update(i,j)

for i in h:
    search(i)
    show(i)







