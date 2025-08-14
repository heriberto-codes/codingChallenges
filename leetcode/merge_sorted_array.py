"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 

To accommodate this, nums1 has a length of m + n, where the first m elements denote the 
elements that should be merged, and the last n elements are set to 0 
and should be ignored. nums2 has a length of n.

EXAMPLE:

-> [1,2,3,0,0,0], 3, 
    ^
      ^
    
   [2,5,6], 3
    ^                

<- [1, ]

    Assumptions:
        - can I assume duplicates will be ignored? 
            - duplicates are not ignored and part of the final array
        - can I assume 0's will be ignored in the final sorted array?
            - Yes 0's will be ignored 
        - can I assume the two inputs will already be sorted in non-decreasing order?
            - yes the original two inputs will already be sorted in non-decreasing order.
        - can I assume that I am allowed to use built in python methods to come to a solution 
        i.e array.insert(index, value)?
        - can I assume nums 2 will always have a length greater than 1?
        - can I assume all values in the list will ne non-negative numbers?
        - can I assume all values in the list will be the type of int?    

            
-> [1,2,3,0,0,0], 3, 
        ^
          ^
   [2,5,6], 3
        ^                
<- [1,2,2,3,5,6] 


-> [5,6,7,0] 1,
    ^
      
   [2, 9, 10] 0,
    ^
    
-> [5]    


BRAINSTORM:
Algo: a two pointer linear iterative search through num1list while comparing againts num2list
Time: O(n)
Space: O(n) on runtime O(n) on retrun value


PLAN:
Need a pathway for three conditionals: > < ==

method to insert:
array.insert(index, value)

init two pointers

Iterate though nums2 with a while loop
while nums2 in not out of bounds 
    set pointer to 0 at both nums2 and nums1
    
    



"""
def merge(nums1, m, nums2, n):
    # Start from the end
    p1 = m - 1  # pointer for nums1 (valid elements only)
    p2 = n - 1  # pointer for nums2
    p = m + n - 1  # pointer for end of nums1

    # While there are elements in nums2 to merge
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    
merge([1,2,3,0,0,0], 3, [2,5,6], 3)