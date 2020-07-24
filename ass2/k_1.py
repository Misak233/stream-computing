import random
import datetime
starttime = datetime.datetime.now()
p=97
p2=1073741789
a1=random.randint(1,p2-1)
b1=random.randint(0,p2)
q=random.randint(1,p-1)
k=0
wide=0
word=[]
fq=[]
f1=open("material.txt")
def Hash(x1,range):
    x=hash(x1)
    prod = a1*x
    prod =prod+b1
    y = prod % p2
    r =  y % range
    return int(r)
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

fre=0
fi=0
fiq=0
fiq2=0
range=107
i=0
j=0
for i,j in zip(word,fq):
    fre=fre+int(j)
    fi=fi+int(j)*Hash(i,range)
    fiq=fiq+Hash(i,range)**2*int(j)
    fiq2=(fiq2+int(j)*q**Hash(i,range))


print("test for insert only",fi**2-fiq*fre)
if fre==0:
    print("there is not item here")
else:
    test=fre*q**(fi/fre)
    print("test for all", fiq2-test)


endtime = datetime.datetime.now()
print(endtime - starttime)
