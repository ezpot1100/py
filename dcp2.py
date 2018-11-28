__author__ = 'naman'

#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element
#at index i of the new array is the product of all the numbers in the
#original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output
#would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?


input = [10, 3, 5, 6, 2]

def new_function(lst):
    result = []
    product = 1

    for i in input:
        product *= i

    for j in input:
        result.append(product/j)
    return result

print "Your initial array of integers: %s" % input
print "Your output as array of integers: %s" % new_function(input)


"""
# Python program for product array puzzle
# with O(n) time and O(1) space.

import math

# epsilon value to maintain precision
EPS = 1e-9

def productPuzzle(a, n):

    # to hold sum of all values
    sum = 0
    for i in range(n):
        sum += math.log10(a[i])

    # output product for each index
    # antilog to find original product value
    for i in range(n):
        print int((EPS + pow(10.00, sum - math.log10(a[i])))),

    return

# Driver code
a = [10, 3, 5, 6, 2 ]
n = len(a)
print "The product array is: "
productPuzzle(a, n)

"""
