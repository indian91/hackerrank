#Sample Input:
#1 4
#x**3 + x**2 + x + 1
#__________________________________________________
#sample Output:
#True
#_________________________________________________
x,k=list(map(int,input().split()))
P=eval(input())
if P==k:
    print(True)
else:
    print(False)
