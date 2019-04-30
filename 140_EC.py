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

    name = "merge"

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

    name = "insertion"

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

    name = "radix"

    def sort(list):
        return list

def compare(lst_of_comparison_functions):
        d = {}
        for func in lst_of_comparison_functions:
            d[func.name] = {}
        max = 10000
        max_length = 10
        iterations = 100
        for i in range(max_length):
            n = 2**i
            sub_d = {}
            for func in lst_of_comparison_functions:
                sub_d[func.name] = 0.0
            for i in range(iterations):
                lst = random_list_of_ints(n,0,max)
                for func in lst_of_comparison_functions:
                    start = time.time()
                    func.sort(lst)
                    total = time.time() - start
                    sub_d[func.name] = sub_d[func.name] + total
            for func in lst_of_comparison_functions:
                d[func.name][n] = sub_d[func.name]/iterations
        return d

def main():
    max_length = 10
    d = compare([Insertion_Sort,Mergesort])
    plt.plot([2**i for i in range(max_length)], [d["merge"][2**i] for i in range(max_length)], 'r--', linewidth=2, markersize=12,label="merge")
    plt.plot([2**i for i in range(max_length)], [d["insertion"][2**i] for i in range(max_length)], 'b--',label="insertion")
    plt.ylabel('time in seconds')
    plt.xlabel('n')
    plt.show()


if __name__ == '__main__':
    main()
