## Rearrange Array Elements

The idea to is have the top two large number as the first digit of two value; (if the number of the list is odd, we pop the largest number);
Then, it require we pop the largest two every time, a efficient way is to use the max_heap data structure;


time: O(nlog(n))
space: O(log(n))



