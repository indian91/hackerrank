'''Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5'''

'''Sample Output

90.0 
91.0 
82.0 
90.0 
85.5'''

"""Print the total marks of student and average marks"""

N,X=list(map(int,input().split()))
l=list(map(float, input().split()) for i in range(X))
for i in zip(*l):
    print(sum(i)/X)
