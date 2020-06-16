### Finding the Square Root of an Integer
O(log(n)) give the hint of using the binary search;
 the searching range (0-N/2+1) and update the median;
 Only thing is to return median-1 if need to get the floored root;

 time: O(log(n))
 space: O(1)