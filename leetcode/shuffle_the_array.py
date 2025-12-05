"""
PROBLEM:
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    Example 1:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7] 
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

    Example 2:
    Input: nums = [1,2,3,4,4,3,2,1], n = 4
    Output: [1,4,2,3,3,2,4,1]

    Example 3:
    Input: nums = [1,1,2,2], n = 2
    Output: [1,2,1,2]

    Constraints:
    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3

EXPLORE:

    > n = 3
    > nums = [2,5,1,3,4,7]

             [2,5,1, 3,4,7]
                  ^      ^
    < [2,3,5,4,1,7]

    before I begin I would like to clarify contrainst to better understand the expecatations of time and space complexity.
        - how large is the input size?
            - < 1000 possible time O(n) - space O(n) or O(1) in place
        - can I assume that the list will be larger than 1? 
        - can I assume the list will be sorted?
            - not sorted but organized
        - can I assume the elements will be of type int?
            - all inputs will be ints
        - can I assume all input size length will be even?
            - yes input size will always be even
        - do you expect the solution to be done in-place, or is allocating a new array acceptable?

BRAINSTORM:
    algo1: two pointer approach with 1 iteration pass on the list
    time: O(n)
    space: runtime O(n) return O(n)


PLAN:
    init a result array
    init left pointer to start at the begining of the list
    init the right pointer to start at the middle of the list on N
    
    start a while loop and keep moving until the right pointer sees the last element in the list
        push the left pointer value to the result array
        push the right pointer value to the result array
        
        move the left pointer to the right
        move the right pointer to the right
        
    return the result array
"""

def shuffle(nums, n):
    result = []
    right = n
    left = 0

    
    while right < len(nums):
        result.append(nums[left])
        result.append(nums[right])
        
        left += 1
        right += 1
        
    return result
        