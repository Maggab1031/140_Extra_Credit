# CS140 Extra Credit
## Gabe Magee

*In all tables, the best values are in **bold***

1. For what values of n is insertion sort faster than mergesort?

For these problems, I made my own versions of each sorting algorithm, created random lists in doubling size, and timed them sorting each list. To make sure I was accounting for outliers, I averaged the results over 100 iterations at each size of list. I got this result, showing Iterative search's O(n^2) nature and Merge sorts O(nlog(n)) nature.

The actual mean times are as follows:
# Merge v Insertion
|n        |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |
|---------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|insertion|**0.000001**|**0.000003**|**0.000006**|**0.000017**|**0.000051**|**0.000198**|0.000656|0.002094|0.008489|0.039241|0.143518|
|merge    |0.000002|0.000006|0.000015|0.000036|0.000079|0.000208|**0.000437**|**0.000844**|**0.001777**|**0.004369**|**0.008508**|


After noticing that for values under 128 are better for insertion than merged, I decided to make a version of mergesort that would use insertion sort for smaller lists, so the recursion takes overall less time. In the results for the lists tested below, my merge-mixed sort does as well or better than Merge sort and almost always is as quick or better than insertion sort. Because of this, I would recommend the mixed sort in most cases. However, when choosing between insertion and pure merge, I would choose Insertion for lists smaller than 128 and Merge for larger lists.

# Merge v Insertion v Merge Mixed
| n=  |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  | 4096  |
|-----------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|------:|
|insertion  |**0.000001**|**0.000002**|**0.000005**|0.000015|**0.000049**|0.000158|0.000594|0.002044|0.009161|0.036160|0.155227|0.59200|
|merge      |0.000002|0.000006|0.000013|0.000031|0.000079|0.000177|0.000394|0.000827|0.001903|**0.004028**|0.009217|0.01899|
|merge_mixed|**0.000001**|**0.000002**|0.000006|**0.000014**|**0.000049**|**0.000157**|**0.000395**|**0.000815**|**0.001901**|**0.004028**|**0.009138**|**0.01888**|


In the below graph, Merge-Mixed and Merge are so close that it is hard to see the difference at this scale. THis likely means the constants are better with Merge-Mixed than pure Merge.

![Graph of Merge v Insertion v Merge Mixed](https://github.com/Maggab1031/140_Extra_Credit/blob/master/Merge_v_insertion_with_merge_mixed.png "Merge v Insertion v merge mixed")

2. What base is best to use with Radix sort when sorting lists with random ints?

I implemented Radix sort using the recomendations I found online at Geeksforgeeks.com. Using this, I used pyplot to make a graph comparing the runtimes of various bases, including the length of the list itself. Similar to the other, I iterated over various lengths of random lists 

If you are interested in the raw averages, here they are:
# Radix Base
| n = |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |
|----|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|   5|0.000020|0.000029|0.000041|0.000074|0.000120|0.000185|0.000314|0.000633|0.001319|0.002404|0.004718|
|   6|0.000020|0.000028|0.000041|0.000073|0.000121|0.000186|0.000314|0.000629|0.001309|0.002374|0.004678|
|   7|0.000019|0.000026|0.000037|0.000064|0.000104|0.000163|0.000273|0.000547|0.001139|0.002071|0.004085|
|   8|0.000020|0.000027|0.000039|0.000066|0.000106|0.000164|0.000273|0.000545|0.001135|0.002094|0.004075|
|   9|0.000020|0.000029|0.000040|0.000068|0.000110|0.000164|0.000275|0.000544|0.001130|0.002068|0.004058|
|  10|0.000020|0.000026|0.000035|0.000058|0.000092|0.000142|0.000232|0.000460|0.000960|0.001764|0.003526|
|  11|0.000020|0.000028|0.000036|0.000060|0.000095|0.000141|0.000233|0.000461|0.000952|0.001736|0.003434|
|   n|0.000032|0.000031|0.000040|0.000072|0.000097|0.000156|0.000207|0.000417|0.000911|0.001910|0.003757|


After some advice from Professor DeVanny, I decided to add some more variable bases to my model.

# Radix Extra Bases
| base  |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |  4096  |
|-------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|      2|0.000030    |0.000044  |0.000069  |0.000105  |0.000192|0.000395|0.000707|0.001568|0.003359|0.006786|0.014670|0.028430|
|      8|0.000020    |0.000026  |0.000037  |0.000052  |0.000085|0.000171|0.000303|0.000651|0.001384|0.002804|0.006070|0.011522|
|      5|0.000019    |0.000027  |0.000039  |0.000055  |0.000095|0.000194|0.000341|0.000745|0.001607|0.003279|0.007058|0.013538|
|     10|0.000019    |**0.000025**|**0.000033**|**0.000045**|**0.000075**|0.000147|0.000253|0.000558|0.001161|0.002427|0.005240|0.010492|
|     16|0.000023    |0.000029  |0.000039  |0.000050  |0.000079|0.000154|0.000258|0.000549|0.001175|0.002366|0.005076|0.009988|
|n      |0.000029    |0.000028  |0.000036  |0.000049  |**0.000075**|0.000165|**0.000229**|0.000513|0.001476|0.003383|0.006765|0.014038|
|n/2    |**0.000001**|0.000043  |0.000042  |0.000050  |0.000078|**0.000137**|0.000248|**0.000415**|**0.000898**|0.002082|0.004599|0.011493|
|2n     |0.000020    |0.000026  |0.000038  |0.000052  |0.000101|0.000175|0.000302|0.000718|0.001966|0.004473|0.011935|0.019400|
|sqrt(n)|**0.000001**|0.000044  |0.000068  |0.000061  |0.000095|0.000173|0.000254|0.000539|0.000949|**0.001929**|**0.004237**|**0.008358**|

![Graph of Radix 2](https://github.com/Maggab1031/140_Extra_Credit/blob/master/new_radix.png "Radix")

In this chart, we can see that at large values, a base of square root of n is the best to use. However, in lower size lists, it is better to use a base of 10 or even n or n/2. A lot of the runtime depends on the maximum value present in the list, as the runtime for radix sort is O(nlog_b(k)), where b is the base and k is the largest element.

