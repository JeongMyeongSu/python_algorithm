import sys
def check(words):
    if words==words[::-1]:
        return True
    else:
        return False
T = int(input())
for _ in range(T):
    checker = 2
    word = sys.stdin.readline().rstrip()
    if check(word):
        print(0)
        break
    for i in range(len(word)):
        new_word = word[:i]+word[i+1:]
        if check(new_word):
            checker=1
            break
    print(checker)
    