import random
import datetime
starttime = datetime.datetime.now()
p=1073741789
p2=107
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
        a[j][ws]+=int(f)
        a[j+deep][ws]+=int(f)*ws
        a[j+2*deep][ws]+=int(f)*(ws**2)


def search(x,j):
    ws=h_basic(a1[j],b1[j],x,wide)
    f1=a[j][ws]
    if f1==0:
        judge=0
        return judge
    fi=a[j+deep][ws]
    qi=a[j+2*deep][ws]
    if fi**2==f1*qi:
        judge=1
        return judge
    else:
        judge=0
        return judge

def verify(a,i,j):
    f=a[j][i]
    if f1==0:
        judge=0
        return judge
    fi=a[j+deep][i]
    qi=a[j+2*deep][i]
    if fi**2==f*qi:
        judge=1
        return judge
    else:
        judge=0
        return judge

def show(x,j):
    f=a[j][h_basic(a1[j],b1[j],x,wide)]
    print(x,f)



k=0
num=0
word=[]
fq=[]
f1=open("material.txt")
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
    num+=1
num2=num**3
a2,b2=Hash()


wide=20

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

h2=[]
h3=[]
for i,j in zip(word,fq):
    if h_basic(a2,b2,i,num2)<num2*wide/num:
        h2.append(i)
        h3.append(j)
for i,j in zip(h2,h3):
    update(i,j)

for j in range(deep):
    count=0
    for i in range(wide):
        if verify(a,i,j)==1:
            count+=1
        if count>wide/2:
            print(count)
            break

f2=open("result.txt",'a+')

for j in range(deep):
    count=0
    for i in h:
        if search(i,j)==1:
            f2.write(i)
            f2.write("\n")
            break

endtime = datetime.datetime.now()
print(endtime - starttime)









