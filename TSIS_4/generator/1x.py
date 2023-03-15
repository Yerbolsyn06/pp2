a=input().split()
cnt=0
for i in a:
    if(i[::-1]==i):
        print(i)
        cnt+=1
print(cnt)       

