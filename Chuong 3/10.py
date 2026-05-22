# vi du 
f=open("e:\\dulieu.txt","r")
s=f.read()
s=s.strip()
a=s.splist(" ")
t=0
print("day so duoc doc la:",a)
for i in a:
    t=t+int(i)
    print("tong cua day so la:",t)