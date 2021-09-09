import sys

book_num = int(input())
library_a =[int(sys.stdin.readline())]

for i in range(1,book_num):
    library_a.append(int(sys.stdin.readline()))

count=1
max_num=max(library_a)
max_idx=library_a.index(max_num)
library_b=library_a[:max_idx]
for i in library_b[::-1]:
    if i == (max_num-1):
        count+=1
        max_num=max_num-1
count=len(library_a)-count
        

print(count)
