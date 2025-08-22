""""
Given an integer array nums and an integer val, remove all occurrences 
of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain 
the elements which are not equal to val. The remaining elements of nums 
are not important as well as the size of nums.

Return k.

EXPLORE:

    val = 3
     
    -> [3,2,2,3]
          r
          ^
    
    <- [2,2]
    
    assumptions:
        - assume I can use python methods like append, pop, slice 
        - Assume I have to do it in place
        - Assume that I am returning the same array, need to modify the array in place
        - can I assume that the length of the array will be > 1?
        - How do I hanlde a list of all vals?
    
    list methods:
    - remove(takes a value not an index) 
    - pop(index)
    - slice()

BRAINSTORM:

PLAN:

""" 
def removeElement(nums, val):
    # pointer to place the next non-val element
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3, 2, 2, 3]
k = removeElement(nums, 3)
print("k:", k)          # number of elements not equal to val
print("nums:", nums)    # modified array
# [2,2,2,3]