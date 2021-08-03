a=input()
k=0
if "U" in a:
    a=a[a.index("U"):]
    if "C" in a:
        a=a[a.index("C"):]
        if "P" in a:
            a=a[a.index("P"):]
            if "C" in a:
                print("I love UCPC")
                k=1
if k!=1:
    print("I hate UCPC")
