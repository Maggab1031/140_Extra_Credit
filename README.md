# CS140 Extra Credit
## Gabe Magee


1. For what values of n is insertion sort faster than mergesort?

For these problems, I made my own versions of each sorting algorithm, created random lists in doubling size, and timed them sorting each list. To make sure I was accounting for outliers, I averaged the results over 100 iterations at each size of list. I got this result, showing Iterative search's O(n^2) nature and Merge sorts O(nlog(n)) nature.

![Graph of Merge v Insertion](https://github.com/Maggab1031/140_Extra_Credit/blob/master/merge_v_insertion.png "Merge v Insertion")

The actual mean times are as follows:
# Merge v Insertion
|n        |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |
|---------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|insertion|0.000001|0.000003|0.000006|0.000017|0.000051|0.000198|0.000656|0.002094|0.008489|0.039241|0.143518|
|merge    |0.000002|0.000006|0.000015|0.000036|0.000079|0.000208|0.000437|0.000844|0.001777|0.004369|0.008508|


![Graph of Merge v Insertion v Merge Mixed](https://github.com/Maggab1031/140_Extra_Credit/blob/master/Merge_v_insertion_with_merge_mixed.png "Merge v Insertion v merge mixed")

# Merge v Insertion v Merge Mixed
| n         |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  | 4096  |
|-----------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|------:|
|insertion  |0.000001|0.000002|0.000005|0.000015|0.000049|0.000172|0.000727|0.002150|0.010812|0.035475|0.146041|0.59265|
|merge      |0.000002|0.000005|0.000013|0.000032|0.000079|0.000192|0.000483|0.000869|0.002263|0.003938|0.008715|0.01894|
|merge_mixed|0.000001|0.000002|0.000006|0.000015|0.000050|0.000175|0.000477|0.000872|0.002261|0.003914|0.008658|0.01901|


2. What base is best to use with Radix sort when sorting lists with random ints?

I implemented Radix sort using the recomendations I found online at Geeksforgeeks.com. Using this, I used pyplot to make a graph comparing the runtimes of various bases, including the length of the list itself.Similar to the other, I iterated over various lengths of random lists and did multiple trials

![Graph of Radix](https://github.com/Maggab1031/140_Extra_Credit/blob/master/radix.png "Radix")


If you are interested in the raw averages, here they are:
# Radix Base
|base|   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |
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

# Radix Base
| base  |   2    |   4    |   8    |   16   |   32   |   64   |  128   |  256   |  512   |  1024  |  2048  |  4096  |
|-------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|      2|0.000036|0.000046|0.000068|0.000109|0.000185|0.000333|0.000645|0.001282|0.002786|0.006042|0.012538|0.024074|
|      8|0.000023|0.000028|0.000036|0.000052|0.000087|0.000148|0.000273|0.000535|0.001135|0.002506|0.005082|0.009685|
|      5|0.000023|0.000028|0.000037|0.000057|0.000094|0.000169|0.000313|0.000620|0.001316|0.002859|0.005848|0.011331|
|     10|0.000022|0.000025|0.000034|0.000049|0.000072|0.000127|0.000233|0.000461|0.000972|0.002230|0.004380|0.008492|
|     16|0.000026|0.000030|0.000038|0.000053|0.000076|0.000130|0.000240|0.000454|0.000959|0.002151|0.004329|0.008316|
|n      |0.000034|0.000029|0.000035|0.000052|0.000074|0.000140|0.000210|0.000412|0.000930|0.002084|0.005700|0.009316|
|n/2    |0.000001|0.000045|0.000040|0.000052|0.000079|0.000117|0.000227|0.000345|0.000741|0.001695|0.003498|0.007057|
|2n     |0.000023|0.000027|0.000038|0.000053|0.000102|0.000164|0.000271|0.000605|0.001241|0.004333|0.007442|0.016051|
|sqrt(n)|0.000001|0.000046|0.000067|0.000063|0.000094|0.000147|0.000236|0.000460|0.000786|0.001742|0.003620|0.007291|

![Graph of Radix 2](https://github.com/Maggab1031/140_Extra_Credit/blob/master/new_radix.png "Radix")


It seems the higher we go, the better the base. Some bases are better, like 5,8,10 (possibly due to their nature interacting with different numbers). Theoretically, n should be the best. But with higher max numbers present in the list it becomes more and more of a burden.
