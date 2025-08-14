"""
EXPLORE:  
 -> 1234
    ^
 
 <- 11223344
 
 assumptions:
    - n will be a non negative number
    - need to only work with integer opertations 
    - assume you cant use string operations
    - assume i will be creating a new number of integers
     
BRAINSTORM:
Algo: iterative approach 
Time: O(n)
Space: O(n) on runtime 
       O(1) on return

PLAN:

 init a variable to hold my result 

 Use modulus 10 to rip off the last number i.e (n%10)
 

"""


def solution(n):
    result = 0
    storage = []
    while n > 0:
        digit = n % 10
        storage.append(digit)
        storage.append(digit)
        n //= 10
    # Now storage holds the digits in reverse. We'll build the final result from it later.
    for d in reversed(storage):
        result = result * 10 + d
    return result

print(solution(1234))