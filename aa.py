d=int(input())
l=[]
for i in range(d):
    x,y,z=input().split()
    x=int(x)
    y=int(y)
    z=int(z)
    l=l+[[x,y,z]]

print(l)
def hcf(x,y):
    HCF=[]
    xx=min(x,y)
    for j in range(1,xx+1):
        if(x%j==0 & y%j==0):
            HCF+=[j]
    return(HCF)
for i in l:
    p=hcf(i[0],i[1])
    print(p)
    q=len(p)
    if(i[2]>q):
        print("No crymeth today")
    else:
        print(p[q-i[2]])
