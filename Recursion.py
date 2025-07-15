#Recursion- a function calling itself to solve a problem

#factorial

def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

# TAIL recursion

def tail_fact(n,acc=1):
    if n==0:
        return 0
    else:
        return tail_fact(n-1,acc*n)
    
def nontail_fact(n):
    if n==1:
        return 1
    else:
        return n*nontail_fact(n-1)
    
print(tail_fact(6))
print(nontail_fact(7))

