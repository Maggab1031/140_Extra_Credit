import os
import random
import time
import matplotlib.pyplot as plt

"""
Create a program to investigate any of the following:

1. For what values of n is insertion sort faster than mergesort?
2. What base is best to use with Radix sort when sorting lists with random ints?
3. For Dijkstra's algorithm, when is using a binary heap better than a Fibonacci heap?
4. What is the constant factor in Quicksort's and Merge sort's Θ(nlogn) runtime on random lists?
5. Another interesting question related to our class. (Requires prior approval from me)

Terms and conditions:
1. You are allowed to copy code for the algorithms/data structures, but your testing code should be all your own and you should provide references to where you obtained any code you did not write.
2. I reserve the right to ask for changes if I am unconvinced your code reveals the correct answer. For example, simply sorting one list with insertion sort and merge sort is insufficient evidence to support a conclusion.
3. Your submission should include your code and a pdf write up that interprets the results of your program with a figure of relevant output. For example, a table of average run time with different bases and different
n's and an explanation of which base appears to be the best.
4. I will award extra credit for investigating at most two of the topics.
5. To submit, create a github, gitlab, bitbucket, or similar public repository and send me a link via email. Your repository should include both your code and the write up.
6. Submissions should be sent in on or before May 8th (the last day of class).
"""

#inclusive for floor and ceiling
def random_list_of_ints(size,floor,ceiling):
    l = []
    for i in range(0,size):
        l.append(random.randint(floor,ceiling))
    return l

class Sort():

    def sort(list):
        return list

class Mergesort(Sort):

    def sort(lst):
        l = lst.copy()
        n = len(lst)
        if n  == 1:
            return l
        elif n == 0:
            return l
        else:
            mid = n//2
            left = Mergesort.sort(l[:mid])
            right = Mergesort.sort(l[mid:])
            l = []
            while(len(left)>0 and len(right)>0):
                if left[0]>right[0]:
                    l.append(right[0])
                    del right[0]
                else:
                    l.append(left[0])
                    del left[0]
            while(len(right)>0):
                l.append(right[0])
                del right[0]
            while(len(left)>0):
                l.append(left[0])
                del left[0]
            return l

class Insertion_Sort(Sort):

    def sort(list):
        l = list.copy()
        res = [l[0]]
        for i in l[1:]:
            index = 0
            j=0
            while j<len(res) and i>res[j]:
                j = j + 1
            res = res[:j]+[i]+res[j:]
        return res

class Radix_Sort():

    def sort(list):
        return list


def main():
    max = 1000
    max_length = 12
    iterations = 100
    d = {}
    d["merge"] = {}
    d["insertion"] = {}
    for i in range(max_length):
        n = 2**i
        print(n)
        total_n_merge = 0.0
        total_n_insertion = 0.0
        for i in range(iterations):
            lst = random_list_of_ints(n,0,max)
            start = time.time()
            Insertion_Sort.sort(lst)
            total = time.time() - start
            total_n_insertion = total_n_insertion + total

            start = time.time()
            Mergesort.sort(lst)
            total = time.time() - start
            total_n_merge = total_n_merge + total
        d["merge"][n] = total_n_merge/iterations
        d["insertion"][n] = total_n_insertion/iterations
    for i in range(max_length):
        n = 2**i
        print(n)
        print("merge:",d["merge"][n])
        print("insertion:",d["insertion"][n])
    return d

if __name__ == '__main__':
    main()
