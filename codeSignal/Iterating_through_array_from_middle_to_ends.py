"""
You are provided with an array of n integers, where n can range from 1 to 200, inclusive. 
Your task is to create a new array that takes two pairs of 'opposite' elements from the 
original array at each iteration, starting from the center and moving towards both ends, 
to calculate the resulting multiplication of each pair.

By 'opposite' elements, we mean pairs of elements symmetrically located relative to 
the array's center. If the array's length is odd, the center element doesn't have an 
opposite and should be included in the result array as is. Each element in the array 
can range from -100 to 100, inclusive. For example, if the input array is 
[1, 2, 3, 4, 5], the returned array should be [3, 8, 5]. This is because the center 
element 3 remains as it is, the multiplication of 2 and 4 is 8, 
and the multiplication of 1 and 5 is 5.

EXPLORE:

    > [1, 2, 3, 4, 5]
             ^
       ^           ^
    
    new array
    < [3]

    Before we begin I would like to clarify some constraints to have a better idea on time and space complexities. 
        - how large is the input size? 
            1 - 200 inclusive
        - will the input be of odd or even length
        - will the input be of type int for each element in the array?
        - how do you want me to handle an empty list?
        - Will duplicate numbers in the list affect my algo?
        - Can I assume the elements in the input list will be non-negative numbers?
        - Will the list be sorted or unsorted?
        - can I assume the list will always be > 1?
        

BRAINSTORM:
    Algo1: 
    Time: O(n) n being the list we are iterating over
    Space: O(n) On runtime O(n) on return

PLAN:
    init a variable to a new empty list
    init a variable to find the mid
    
    if the list is odd
        grab the mid point and move it to the new empty list
        set a pointer for the left of the center
        set a pointer for the right of the center
        
        init a while loop that keeps going until the 
        right pointer reaches the end of the list and
        the left pointer reaches the beggining of the list
        
            multiply both pointers 
            push result to the new empty list
            
            move left pointer one over to the left
            move right pointer one over to the right  
    
    if the list is even
        set the right pointer to be the middle 
        set the left pointer to be one slot to the left of the middle
        
        init a while loop that keeps going until the 
        right pointer reaches the end of the list and
        the left pointer reaches the beggining of the list
        
            multiply both pointers 
            push result to the new empty list
            
            move left pointer one over to the left
            move right pointer one over to the right
            
    return new empty list
"""
def solution(numbers):
    new_list = []
    mid = len(numbers) // 2
    
    if len(numbers) % 2 == 1:
        new_list.append(numbers[mid])
        left = mid - 1
        right = mid + 1
        
        while right < len(numbers) and left >= 0:
            multiply_left_and_right = numbers[left] * numbers[right]
            new_list.append(multiply_left_and_right)
            
            left -= 1
            right += 1
    else:
        right = mid
        left = mid - 1
        
        while right < len(numbers) and left >= 0:
            multiply_left_and_right = numbers[left] * numbers[right]
            new_list.append(multiply_left_and_right)
            
            left -= 1
            right += 1
            
    return new_list