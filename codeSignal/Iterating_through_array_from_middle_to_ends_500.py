"""
You are given an array of n integers, where n can range from 1 to 500, inclusive. 
Your task is to create a new array in which each element is a tuple, determined by 
pairing elements from the middle to both ends of the original array.

If the original array has an odd length, pair the middle element with 0. 

If the original array has an even length, start pairing from the two middle elements. 
Continue the pairing by alternating elements from the left and the right until all elements 
have been paired. After creating the paired elements, return the new array of tuples. 

Ultimately, your result should be an array of tuples, each of size two. 
Each element within a tuple, as well as within the array, can range from -1000 to 1000, inclusive.


EXPLORE:
         even
    ---> [3, 6, 8, 9] 
             ^  ^
             
    <--- [(6,8),(3,9)]   
    
         odd
    ---> [3, 6, 8, 9, 12]
             ^ 
                   ^
    <--- [(8,0),(6,9),(3,12)]
    
    Assumptions:
    - can I assume the length of the list will always be larger than 2 ✅
    

BRAINSTORM:
Algo1: check the length of list to determin odd or even, then in one pass pair outwards
Time: O(n)
Space: O(n)

PLAN:
init result = []
let n = len(nums)

if n is even:
    set L = n//2 - 1, R = n//2
else:
    set mid = n//2
    append (nums[mid], 0) to result
    set L = mid - 1, R = mid + 1
while L >= 0 and R < n:
    append (nums[L], nums[R]) to result
    L -= 1, R += 1
    
return result
"""

def solution(numbers):
    result = []
    n = len(numbers)
    
    if (n % 2 == 0):
        l = n // 2 - 1 
        r = n // 2
    else:
        mid = n // 2
        result.append((numbers[mid], 0))
        l = mid - 1
        r = mid + 1
    while l >= 0 and r < n:
        result.append((numbers[l],numbers[r]))
        l-= 1
        r+= 1
    
    print(result)
    return result


# solution([3, 6, 8, 9])
solution([3, 6, 8, 9, 12])