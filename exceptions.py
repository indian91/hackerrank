
#You are given two values a and b.
#Perform integer division and print a/b.
#sample Input
#3
#1 0
#2 $
#3 1
#________________________________________________________________________
#sample output
#Error Code: integer division or modulo by zero
#Error Code: invalid literal for int() with base 10: '$'
#3
#__________________________________________________________________________
T=int(input())
for i in range(T):
    try:
        a,b=list(map(int,input().split()))
        x=a//b
        print(x)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print(f"Error Code: {e}")
