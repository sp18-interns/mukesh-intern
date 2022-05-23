"""

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""
#solution:-
def same_first_last(nums):
  l = len(nums) # length of variable
  
  
  
  if(l>0 and nums[0] == nums[l -1]):
    return True
  return False
