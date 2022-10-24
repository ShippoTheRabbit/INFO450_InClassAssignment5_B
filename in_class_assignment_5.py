#Problem 1. Sort With Quicksort.
#Brianna Boston 
# Oct 23, 2022
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python
# https://realpython.com/lessons/quicksort-algorithm/
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.
#hello Brianna Boston

'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''
import random

def quicksort(numbers_in_a_list):
     """
     This function takes a list of numbers and recursively sorts it, what it does is pick a pivot point and sorts everything above and below this point.
     QuickSort runs in either Best Case: O(nlogn) or Worst Case O(n^2)
     """
    #WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION
     low  = [] # lower than pivot
     high = [] # greater than pivot
     if len(numbers_in_a_list ) <= 1: #base case 
        return numbers_in_a_list
     else:
        #Geeks for Geeks said we have three ways to get the pivot, either the median, max, or random
        my_pivot = numbers_in_a_list[random.randint(0, len(numbers_in_a_list) - 1)] 
         #pivot = max(numbers_in_a_list) # another way to pick your pivot
        for i in numbers_in_a_list:
            if int(i) < my_pivot:
                low.append(i)
            else: 
                high.append(i)    
           
     return quicksort(low) + quicksort(high)


def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE
    final = []
    f = open("numbers.txt", "r")
    mylist = f.read()
    #print(mylist)
    mylist = mylist.replace('[','')
    mylist = mylist.replace(']','')
    mylist = mylist.replace(',','')
    mylist = mylist.split()
    for i in mylist:
        final.append(int(i))
    q = (quicksort(final))      
    c = open("sorted.txt", "w")
    c.write(str(q))
    c.close()
    c = open("sorted.txt", "r")
  
    
    return c.read() #WHAT DOES IT RETURN?


if __name__ == "__main__":
    print(main())
    
