import sys
lope_num = int(input())
lope_list =[int(sys.stdin.readline())]
for i in range(1,lope_num):
    lope_list.append(int(sys.stdin.readline()))
lope_list.sort()
max_w = lope_list[0]*lope_num
for j in range(len(lope_list)):
    if max_w < lope_list[j]*(lope_num-j):
        max_w = lope_list[j]*(lope_num-j)
print(max_w)