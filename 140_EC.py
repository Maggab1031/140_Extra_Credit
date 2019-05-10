import os
import random
import time
import matplotlib.pyplot as plt
import math

from pytablewriter import MarkdownTableWriter






#inclusive for floor and ceiling
def random_list_of_ints(size,floor,ceiling):
    l = []
    for i in range(0,size):
        l.append(random.randint(floor,ceiling))
    return l

class Sort():

    def sort(list):
        return list

class Radix_Sort(Sort):

    name = "radix"

    @staticmethod
    def sort( lst, RADIX =10 ):
        if RADIX ==0 or RADIX == 1:
            pass
        else:
            aList = lst.copy()
            maxLength = False
            tmp , placement = -1, 1
            while not maxLength:
                maxLength = True
                # declare and initialize buckets
                buckets = [list() for _ in range( RADIX )]
                # split aList between lists
                for i in aList:
                    tmp = i / placement
                    buckets[int(tmp % RADIX)].append( i )
                    if maxLength and int(tmp) > 0:
                        maxLength = False
                # empty lists into aList array
                a = 0
                for b in range( RADIX ):
                    buck = buckets[b]
                    for i in buck:
                        aList[a] = i
                        a += 1
                # move to next digit
                placement *= RADIX
            return aList

def toBase(n,base):
    return int(toString(n,base))

def toString(n,base):
   convertString = "0123456789"
   if n < base:
      return convertString[n]
   else:
      return toString(n//base,base) + convertString[n%base]




class Mergesort(Sort):

    name = "merge"

    @staticmethod
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

    @staticmethod
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

def compare_radix_sort(floor=2,ceiling=10,max_length=10):
    d = {}
    for i in range(floor,ceiling+1):
        d[str(i)] = {}
    d["n"] = {}
    max = 10000
    iterations = 100
    for j in range(1,max_length):
        print(j)
        n = 2**j
        sub_d = {}
        sub_d["n"] = 0.0
        for i in range(floor,ceiling+1):
            sub_d[str(i)] = 0.0
        for k in range(iterations):
            lst = random_list_of_ints(n,0,max)
            start = time.time()
            Radix_Sort.sort(lst,n)
            total = time.time() - start
            sub_d["n"] = sub_d["n"] + total
            for i in range(floor,ceiling+1):
                start = time.time()
                Radix_Sort.sort(lst,i)
                total = time.time() - start
                sub_d[str(i)] = sub_d[str(i)] + total
        for i in range(floor,ceiling+1):
            d[str(i)][n] = sub_d[str(i)]/iterations
        d["n"][n] = sub_d["n"]/iterations
    return d

def compare_radix_sort_2(list_of_bases,max_length=10):
    d = {}
    for i in list_of_bases:
        d[i] = {}
    max = 10000
    iterations = 10
    for j in range(1,max_length):
        print(j)
        n = 2**j
        sub_d = {}
        for i in list_of_bases:
            sub_d[i] = 0.0
        for k in range(iterations):
            print(j,k)
            lst = random_list_of_ints(n,0,max)
            for i in list_of_bases:
                print(j,k,i)
                if i.isdigit():
                    start = time.time()
                    Radix_Sort.sort(lst,int(i))
                    total = time.time() - start
                    sub_d[i] = sub_d[i] + total
                elif i=="n":
                    start = time.time()
                    Radix_Sort.sort(lst,n)
                    total = time.time() - start
                    sub_d[i] = sub_d[i] + total
                elif i=="n/2":
                    start = time.time()
                    Radix_Sort.sort(lst,int(n/2))
                    total = time.time() - start
                    sub_d[i] = sub_d[i] + total
                elif i=="2n":
                    start = time.time()
                    Radix_Sort.sort(lst,n*2)
                    total = time.time() - start
                    sub_d[i] = sub_d[i] + total
                elif i=="sqrt(n)":
                    start = time.time()
                    Radix_Sort.sort(lst,int(math.sqrt(n)))
                    total = time.time() - start
                    sub_d[i] = sub_d[i] + total
        for i in list_of_bases:
            d[i][n] = sub_d[i]/iterations
    return d



def compare(lst_of_comparison_functions,max_n):
        d = {}
        for func in lst_of_comparison_functions:
            d[func.name] = {}
        max = 10000
        max_length = max_n
        iterations = 100
        for i in range(1,max_length):
            print(i)
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

def print_out(d,max_n):
    row_format ="{:>20}" * (max_n + 1)
    l = [2**i for i in range(1,max_n)]
    print(row_format.format("", *l))
    for base in d.keys():
        print(row_format.format("|"+base, *["|"+str(round(d[base][2**i], 5)) ]),end="|")




def main():
    max_length = 13
    """
    d = compare([Insertion_Sort,Mergesort],max_length)
    writer = MarkdownTableWriter()
    writer.table_name = "Merge v Insertion"
    writer.headers = ["function"]+[str(2**i) for i in range(1,max_length)]
    writer.value_matrix = [[func]+[d[func][2**i] for i in range(1,max_length)]for func in d.keys()]
    writer.write_table()
    print([2**i for i in range(1,max_length)])
    fig = plt.figure()
    plt.plot([2**i for i in range(1,max_length)], [d["merge"][2**i] for i in range(1,max_length)], 'r-', linewidth=2, markersize=12,label="merge")
    plt.plot([2**i for i in range(1,max_length)], [d["insertion"][2**i] for i in range(1,max_length)], 'b-',label="insertion")
    plt.legend(loc='upper left')
    plt.ylabel('time in seconds')
    plt.xlabel('n')
    plt.show()
    fig.savefig("merge_v_insertion.png", dpi=fig.dpi)
    plt.clf()
    """
    d = compare_radix_sort_2(["2","8","5","10","16","n","n/2","2n","sqrt(n)"],max_length)
    writer = MarkdownTableWriter()
    writer.table_name = "Radix Base"
    writer.headers = ["base"]+[str(2**i) for i in range(1,max_length)]
    writer.value_matrix = [[base]+[d[base][2**i] for i in range(1,max_length)]for base in d.keys()]
    writer.write_table()
    fig = plt.figure()
    for base in d.keys():
        plt.plot([2**i for i in range(1,max_length)], [d[base][2**i] for i in range(1,max_length)], linewidth=2, markersize=12,label=str(base))
    plt.legend(loc='upper left',title='base')
    plt.ylabel('time in seconds')
    plt.xlabel('n')
    plt.show()

    #fig.savefig("radix_("+min+"_"+max+").png", dpi=fig.dpi)





if __name__ == '__main__':
    main()
