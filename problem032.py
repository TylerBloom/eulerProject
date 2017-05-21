#! /usr/bin/python

a = []
passed = True

for i in range(988):
    strI = str(i)
    for n in range(988):
        strN = str(n)
        if len(strI + strN) > 5:
            break
        prod = i * n
        strProd = str(prod) + strI + strN
        for u in range(1,10):
            try:
                if strProd.index(str(u)) != strProd.rindex(str(u)):
                    passed = False
                    break
            except:
                passed = False
                break
        try:
            if strProd.index('0') > -1:
                passed = False
        except:
            pass
        if passed:
            a.append(prod)
        else:
            passed = True

Sum = 0
list = []

for i in a:
    try:
        list.index(i)
    except:
        Sum += i
        list.append(i)

print Sum

