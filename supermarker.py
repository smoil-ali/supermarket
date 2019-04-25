from collections import defaultdict
d = defaultdict(list)
N=int(input())
sum=0
for x in range(N):
    str=input().split()
    length=len(str)
    val=int(str[length-1])
    var=str[0:length-1]
    d[" ".join(var)].append(val)

print(dic)
for item,value in d.items():
    for x in range(len(value)):
        sum+=value[x]
    print(item,sum)
    sum=0



