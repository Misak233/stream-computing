import random
import datetime
starttime = datetime.datetime.now()
p=107
p2=1073741789
a1=random.randint(1,p2-1)
b1=random.randint(0,p2)
q=random.randint(1,p-1)
def Hash(x1,range):
    x=hash(x1)
    prod = a1*x
    prod =prod+b1
    y = prod % p2
    r =  y % range
    return int(r)

range=244**2
word=[]
s2=244**2
s=0
sample=0
f1=open("material.txt")
f2=open("result.txt","a+")
samples=1000

for i in f1.readlines():
    for j in i.split():
        s=Hash(j,range)
        if s<s2:
            sample=j
            s2=s
f2.write("\n")
f2.write(sample)

endtime = datetime.datetime.now()
print(endtime - starttime)




