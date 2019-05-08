# 140_Extra_Credit
Extra Credit for 140


1. For what values of n is insertion sort faster than mergesort?
![Graph of Merge v Insertion](https://github.com/Maggab1031/140_Extra_Credit/blob/master/merge_v_insertion.png "Merge v Insertion")




2. What base is best to use with Radix sort when sorting lists with random ints?

I implemented Radix sort using the recomendations I found online at Geeksforgeeks.com. Using this, I used pyplot to make a graph comparing the runtimes of various bases, including the length of the list itself.

![Graph of Radix](https://github.com/Maggab1031/140_Extra_Credit/blob/master/radix.png "Radix")


If you are interested in the raw averages, here they are:
                     2                   4                   8                  16                  32                  64                 128                 256
 5               2e-05               3e-05               4e-05               7e-05             0.00012             0.00019             0.00032              0.0006
 6               2e-05               3e-05               5e-05               8e-05             0.00012             0.00019             0.00032             0.00059
 7               2e-05               3e-05               4e-05               7e-05              0.0001             0.00016             0.00028             0.00052
 8               2e-05               3e-05               4e-05               7e-05              0.0001             0.00016             0.00028             0.00052
 9               2e-05               3e-05               4e-05               7e-05             0.00011             0.00016             0.00028             0.00052
10               2e-05               3e-05               4e-05               6e-05               9e-05             0.00014             0.00024             0.00044
11               2e-05               3e-05               4e-05               6e-05               9e-05             0.00014             0.00024             0.00043
 n               3e-05               3e-05               4e-05               7e-05              0.0001             0.00016             0.00021             0.00039


1. You are allowed to copy code for the algorithms/data structures, but your testing code should be all your own and you should provide references to where you obtained any code you did not write.
2. I reserve the right to ask for changes if I am unconvinced your code reveals the correct answer. For example, simply sorting one list with insertion sort and merge sort is insufficient evidence to support a conclusion.
3. Your submission should include your code and a pdf write up that interprets the results of your program with a figure of relevant output. For example, a table of average run time with different bases and different
n's and an explanation of which base appears to be the best.
4. I will award extra credit for investigating at most two of the topics.
5. To submit, create a github, gitlab, bitbucket, or similar public repository and send me a link via email. Your repository should include both your code and the write up.
6. Submissions should be sent in on or before May 8th (the last day of class).







