import bisect

N = int(input())
arr = list(map(int,input().split()))

LIS = [arr[0]]
for i in range(1,N):
    if (arr[i]>LIS[-1]):
        LIS.append(arr[i])
    else:
        idx = bisect.bisect_left(LIS, arr[i]) # bisect.bisect_left(arr,x) : 정렬되어있다면 arr의 x가 들어갈 인덱스 반환
        LIS[idx] = arr[i]
print(len(LIS))
