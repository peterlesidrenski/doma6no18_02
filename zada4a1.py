from math import ceil
n = int(input())
list1=[]
for i in range(n):
    a = float(input())
    list1.append(a)
print(f"Count of stadium lap: {len(list1)}")
print(f"list of laps: {list1}")
print(f"slowest lap: {max(list1)}")
print(f"fastest lap: {min(list1)}")
print(f"Total laps time: {sum(list1)}")
b = (sum(list))
c = (len(list))
print(f"average laps time: {(ceil(b/c))}")
