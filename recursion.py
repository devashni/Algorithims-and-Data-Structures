# question 1: calculate the sum of a list of numbers.
def sum_lst(lst):
    if len(lst) == 1:
        return lst[0]

    total_sum = lst[0] + sum_lst(lst[1:])
    return total_sum

# ! Test case: sum_lst
# if (sum_lst([10,1,2,3])) == 16 and (sum_lst([100])) == 100 and (sum_lst([])) == 0:
#     print ("sum_lst function works")

# Python program to get the factorial of a non-negative integer
def calc_factorial (num):
    #base case, i.e, exit condition
    if num == 1 or num == 0:
         return 1
         
    factorial = num * calc_factorial(num-1)
    return factorial

# ! Test case: calc_factorial
# if (calc_factorial(10)) == 3628800 and (calc_factorial(0)) == 1 and (calc_factorial(2)) == 2:
#     print ("calc_factorial function works")

#Python program to solve the Fibonacci sequence using recursion.
# TODO
def fibonacci(n): #return nth_num in the sequence
    F=[]
    F[0] = 0
    F[1] = 1

    # ! F[n] = F[n-1] + F[n-2] ; such that
    # 0,1,1,2,3,5,8,13,21,34,55,89,144...

# Write a Python program to get the sum of a non-negative integitger
def sumDigits(num):
    if len(digits) == 0:
        return sum

    sum = d_lst[0] + sumDigits

# ! Test case: SumDigits
# sumDigits(345) -> 12
# sumDigits(45) -> 9