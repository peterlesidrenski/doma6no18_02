from math import ceil
list1 = []
while True:
    a = input()
    if a == "Stop":
        break
    a = int(input())
    list1.append(a)

print(f"Count of monza lap: {len(list1)}")
print(f"list of laps: {list1}")
print(f"slowest lap: {max(list1)}")
print(f"fastest lap: {min(list1)}")
print(f"Total laps time: {sum(list1)}")
b = (sum(list))
c = (len(list))
print(f"average laps time: {(ceil(b/c))}")
