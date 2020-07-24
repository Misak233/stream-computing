import random
import datetime
p=1073741789
def Hash():
    a=random.uniform(0,p-1)+1
    b=random.uniform(0,p)
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
        a[j][h_basic(a1[j],b1[j],x,wide)]+=f

def search(x):
    r=1000000000000
    for j in range(deep):
        if r>a[j][h_basic(a1[j],b1[j],x,wide)]:
            r=a[j][h_basic(a1[j],b1[j],x,wide)]
    return r


start = datetime.datetime.now()


a1=[]
b1=[]
i=0
deep=3
wide=0
while i<=deep:
    A,B=Hash()
    a1.append(A)
    b1.append(B)
    i=i+1

f=open("blends4.txt")
m=[]
for line in f.readlines():
    for word in line.split():
        m.append(word)
        wide=wide+1
dic=list(set(m))

f=open("blends2.txt")
n=[]
for line in f.readlines():
    for word in line.split():
        n.append(word)



i=0
w=0
a = [[0 for i in range(wide)] for i in range(deep)]

for i in m:
    update(i,1)
end1 = datetime.datetime.now()
print ("time update",end1-start)

for i in n:
    print(i,search(i))

end2 = datetime.datetime.now()
print ("time query",end2-start)







import psutil
import os
import sys
import time

pid = os.getpid()

p = psutil.Process(pid)
print ('Process info:')
print ('name: ', p.name())
print ('exe:  ', p.exe())

data = []

while True:
    data += list(range(100001))
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024.
    print ('Memory used: {:.2f} MB'.format(memory))
    if memory > 40:
        print ('Memory too big! Exiting.')
        sys.exit()

    time.sleep(1)
