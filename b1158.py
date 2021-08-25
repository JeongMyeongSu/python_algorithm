N,K = map(int,input().split())
li=[i for i in range(1,N+1)]
que = []
k = K-1
while len(li):
    if len(li) > k:
        que.append(str(li.pop(k)))
        k += K-1
    else:
        k = k%len(li)
        que.append(str(li.pop(k)))
        k += K-1

print("<", ", ".join(que),">", sep='')



# N,K = map(int,input().split())
# li=[i for i in range(1,N+1)]
# que = []
# while len(li):
#     for i in range(K-1):
#         li.append(li.pop(0))
#     que.append(str(li.pop(0)))
# print("<", ", ".join(que),">", sep='')


# N,K = map(int,input().split())
# li=[i for i in range(1,N+1)]
# visited=[0]*N
# answer=[]
# check=0
# while 1:
#     for i in range(N*K):
#         if visited[i%N]==0:
#             check += 1
#         if check == K:
#             visited[i%N] = 1
#             answer.append(li[i%N])
#             check = 0
#             continue
#     if len(answer)==N:
#         break
# print("<",end="")
# for i in answer[:-1]:
#     print(i,end=', ')
# print("{}>".format(answer[-1]))



