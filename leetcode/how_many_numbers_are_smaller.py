"""
Given the array nums, for each nums[i] find out how many numbers in the array are 
smaller than it. That is, for each nums[i] you have to count the number of 
valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

CONSTRAINTS:
    2 <= nums.length <= 500
    0 <= nums[i] <= 100

    Upper Bound 
        O(n2) Quadratic
    Lower Bound
        O(n) Linear

EXPORE:
    non sorted
    > [8,1,2,2,3] 
               ^ 
               ^
    < [4, 0, 1, 1, 3]
    
    sorted
    > [1, 2, 2, 3, 8] sorted
       0  1  2  3  4. <- use index to determine answer
                   ^ 
       
    < [0, 1, 1, 3, 4]
    
    Assumptions:
        - can I assume all duplicates get the same count
        - can I assume all inputs adhear to the contraints
        

BRAINSTORM:
    Algo1: Sort the array then iterate through the sorted list store 
           the frequency of value in the list in a dictionary
    Time: O(n log n) n in the length if the input array
    Space: O(n) n being growth the dictionary
    
    Algo2: use a 2 pointer approach with nested looops to compare each element
    Time: O(n2) Quadratic
    Space: O(n) n being growth the dictionary 

PLAN:
init a vairable and assign it an empty final list
init a variable called sorted 
assign the varibale the sorted list 
init a variable for pointer 1
init a variable for pointer 2

iterate through the list
    if pointer 1 is not the same as pointer 2
        push the value currently sitting in pointer 1 to the final list
        move pointer 1 and pointer 2 to the next slot
    if pointer 1 is equal to pointer 2
        iterate both pointerns to the next slot
        
return final list
"""

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    counts = {}

    for index, number in enumerate(sorted_nums):
        if number not in counts:
            counts[number] = index

    return [counts[number] for number in nums]


print(smallerNumbersThanCurrent([6, 5, 4, 8]))
