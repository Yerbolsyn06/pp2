import json
with open("NTAP (1).json", "r") as read_file:
    a=json.load(read_file)

# print(a["Date"])  
# print(a["Open"])
# print(a["Close"])
cnt=0
while(cnt!=5):
    for i in a:
        print(i,str(cnt),":",a[i][str(cnt)])
    cnt+=1      

