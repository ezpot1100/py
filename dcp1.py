# -*- coding: iso-8859-15 -*-

__author__ = 'naman'

#Given a list of numbers and a number k return whether any two numbers
#from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass
#Testing for Githubs

def find_num(input, num):
    counter = 0
    for j in range(len(input)):
        print
        print "j: %d in for loop" % j
        print "num: %d and input[%d]: %d" % (num, j, input[j])
        print
        if ((num - input[j]) in input) and (input[j] != (num - input[j])):
            counter += 1
            print
            print "For j: %d in if, value for counter is: %d" % (j, counter)
            print
    if counter > 0:
        return True
    else:
        return False

lst = []
size = int(raw_input("Enter the size of the list: "))

for i in range(size):
    elements = int(raw_input("Enter element [%d]: " % (i+1)))
    lst.append(elements)

print
print "Your list is: %s" % lst

print
k = int(raw_input("Enter the number for equals the sum of two numbers in the list: "))

print
#print find_num(lst, k)
if find_num(lst, k):
    print "Yay! you have two numbers in the list which equals to sum you entered"
else:
    print "Uhoh! you don't have two numbers in the list which equals to sum you entered"
