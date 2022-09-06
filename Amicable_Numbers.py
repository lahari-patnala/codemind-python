n=int(input())
m=int(input())
s1=0
s2=0
for i in range(1,n):
    if n%i==0:
        s1+=i
for i in range(1,m):
    if m%i==0:
        s2+=i
if n==s2 and m==s1:
    print("Amicable")
elif n!=s2 or m!=s1:
    print("Not Amicable")
else:
    print("Not Amicble")