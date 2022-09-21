n=int(input())
cnt1=0
cnt2=0
for i in str(n):
    if int(i)%2==0:
       cnt1+=1 
    elif int(i)%2!=0:
        cnt2+=1
if cnt1!=0 and cnt2!=0:
    print("Mixed")
elif cnt1!=0 and cnt2==0:
    print("Even")
else :
    print("Odd")