# Write a function that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

## N is an integer within the range [1..100,000];
## each element of array A is an integer within the range [−1,000,000..1,000,000].
import time;

# ! Solution 1: performance 25/100, correctness 100/100
def solution(A):
    smallest_positive_int = 1
    
    while True:
        if smallest_positive_int in A:
            smallest_positive_int += 1
        else:
            return smallest_positive_int


# ! Solution 2: performance 100/100, correctness 100/100
def binary_search(value, array):
    low_index = 0
    high_index = len(array) - 1

    while low_index <= high_index:
        mid_index = (high_index + low_index) // 2
        if array[mid_index] < value:
            low_index = mid_index+1
        elif array[mid_index] > value:
            high_index = mid_index - 1
        else:
            return True
    return False
    
def solution2(numbers):
    smallest_positive_int = 1
    numbers.sort()

    while True:
        is_number_in_numbers = binary_search(smallest_positive_int, numbers)
        #is_number_in_numbers = smallest_positive_int in numbers
        if is_number_in_numbers:
            smallest_positive_int += 1
        else:
            return smallest_positive_int


def create_test_array(n):
    return_array = []
    for i in range(0, n):
        return_array.append(i)
    return return_array

def time_solution():
    test_array = create_test_array(30000)
    start_time = time.time()
    # answer = solution(test_array)
    answer2 = solution2(test_array)
    end_time = time.time()
    print('answer is: ' + str(answer2))
    print ("Time elapsed:", end_time - start_time)

time_solution()

#problem 2 - leetcode sliding window
def compress(self, chars):
    s = []
    start = 0
    end = 0
    if len(chars) <2:
        return len(chars)
    else:
        for i in range(0, len(chars) + 1):
            end = i
            if (end >= len(chars)) or (chars[start] != chars[end]):
                sub_str = chars[start: end]
                length = len(sub_str)
                s.append(sub_str[0])  #append single char of the repeating group
                if length > 1 and length < 10: #if length is less than 10
                    s.append(str(length))
                elif length >9:
                    for x in str(length): #if length is less than 10
                        s.append(x)
                start = end       
                sub_str = []
    
    #not needed 
    # TODO : refactoring needed
    # while len(chars) > 0:
    #     chars.pop()
    # for x in s:
    #     chars.append(x)
    # return len(chars)
    s[:] = chars


def groupAnagrams(strs):
    output = []
    word_group = []
    
    if len(strs) < 2:
        return output[strs]
    
    for i in range(0,len(strs)):
        word = strs.pop(i)
        word_group.append(word)
        
        for s in strs[i+1:]:
            if len(s) == len(word):
                for letter in word:
                    if letter not in s:
                        break
                s_idx = strs.index(s)
                anagram = strs.pop(s_idx)
                word_group.append(anagram)
        
        word_group = []
        
    return output