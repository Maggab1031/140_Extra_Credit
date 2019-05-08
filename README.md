# 140_Extra_Credit
Extra Credit for 140


1. For what values of n is insertion sort faster than mergesort?

For these problems, I made my own versions of each sorting algorithm, created random lists in doubling size, and timed them sorting each list. To make sure I was accounting for outliers, I averaged the results over 100 iterations at each size of list. I got this result, showing Iterative search's O(n^2) nature and Merge sorts O(nlog(n)) nature.

![Graph of Merge v Insertion](https://github.com/Maggab1031/140_Extra_Credit/blob/master/merge_v_insertion.png "Merge v Insertion")




2. What base is best to use with Radix sort when sorting lists with random ints?

I implemented Radix sort using the recomendations I found online at Geeksforgeeks.com. Using this, I used pyplot to make a graph comparing the runtimes of various bases, including the length of the list itself.

![Graph of Radix](https://github.com/Maggab1031/140_Extra_Credit/blob/master/radix.png "Radix")


If you are interested in the raw averages, here they are:
# Radix Base
| 2 |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |
|---|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|  5|0.000020|0.000030|0.000051|0.000076|0.000114|0.000185|0.000313|0.000657|0.001225|0.002525|
|  6|0.000020|0.000032|0.000051|0.000078|0.000114|0.000186|0.000313|0.000661|0.001215|0.002504|
|  7|0.000020|0.000028|0.000047|0.000069|0.000100|0.000162|0.000273|0.000565|0.001066|0.002172|
|  8|0.000020|0.000030|0.000047|0.000071|0.000101|0.000163|0.000270|0.000564|0.001055|0.002164|
|  9|0.000021|0.000030|0.000050|0.000074|0.000103|0.000164|0.000271|0.000569|0.001063|0.002160|
| 10|0.000020|0.000027|0.000043|0.000062|0.000087|0.000139|0.000231|0.000485|0.000899|0.001883|
| 11|0.000020|0.000028|0.000047|0.000063|0.000090|0.000141|0.000234|0.000483|0.000888|0.001833|
|n  |0.000033|0.000033|0.000051|0.000075|0.000094|0.000155|0.000207|0.000436|0.000845|0.001955|

1. You are allowed to copy code for the algorithms/data structures, but your testing code should be all your own and you should provide references to where you obtained any code you did not write.
2. I reserve the right to ask for changes if I am unconvinced your code reveals the correct answer. For example, simply sorting one list with insertion sort and merge sort is insufficient evidence to support a conclusion.
3. Your submission should include your code and a pdf write up that interprets the results of your program with a figure of relevant output. For example, a table of average run time with different bases and different
n's and an explanation of which base appears to be the best.
4. I will award extra credit for investigating at most two of the topics.
5. To submit, create a github, gitlab, bitbucket, or similar public repository and send me a link via email. Your repository should include both your code and the write up.
6. Submissions should be sent in on or before May 8th (the last day of class).







