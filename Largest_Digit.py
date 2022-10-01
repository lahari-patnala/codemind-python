n=int(input())
lst=[]
while n>0:
    r=n%10
    n=n//10
    lst.append(r)
print(max(lst))