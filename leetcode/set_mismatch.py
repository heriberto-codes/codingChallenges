"""
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to 
another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this 
set after the error. Find the number that occurs twice and the number that 
is missing and return them in the form of an array.

EXPLORE:

   non sorted
   s --> [1,4,2,2,5]
   
   <-- [2,3]

   sorted
   s --> [1,2,2,4,5]
   
   <-- [2,3]
      
   sorted
   s --> [1,4,2,2,5]
          ^
              ^
           
   set = (2)           
   s --> [1,4,2,2,5]
   
   
   n up to length of list (5) ---> [1, 2, 3]
        
            
   Assumptions:
    - can I assume that all numbers will be non negative integers and greater than 0 | ✅
    - can I assume the length of the array is greater than 2 | ✅
    - Can I assume will the array be sorted initialy | ❌
    - can I assume that if I have a duplicate number like 4,4 that the next number is 5 ❌
    - can I assume that a duplicate will only show up once as a duplicate? | ✅
    - can I assume that there will only be one set up duplicates | ✅
    
    
BRAINSTORM:
Algo1: an iteration 1 pass of a loop with a set to keep track of the duplicate  
Time: O(n) 
Space: O(n)

Algo2: a nested loop to find the duplicate while the first pointer keeps track of all the numbers in a dict  
Time: O(n2)
Space: O(n)

PLAN:
init a variable and assign it to an empty set
init a variable called seen and assign it as none

    loop through the list of numbers 
        if the number exist in the set
            re-assign the seen variable to the number I am currnelty looking at
        else
            add the current num the the set
          
    set n to the len of nums  
    loop through 1 - n, n being the length of the list. Include the last number in the list.
        if the current num I am looking at is not in the seen list
            set missing variable to i
            then break out the loop
"""
def findErrorNums(nums):
    seen_set = set()
    duplicate = None
    
    # find duplicate 
    for num in nums:
        if num in seen_set:
            duplicate = num
        else:
            seen_set.add(num)
            
    # find missing 
    print('seen_set -->', seen_set)
    # {1, 2, 4, 5}
    
    n = len(nums)
    print('n -->', n)
    for i in range(1, n + 1):
        print('i -->', i)
        if i not in seen_set:
            missing = i
            break
        
    print([duplicate, missing])
    return [duplicate, missing]
        
        
findErrorNums([1,4,2,2,5])