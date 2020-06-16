Explanation problem 3 : Huffman Coding

To implment the huffman encoding, I choose to define the new data sturcture called human node with weights as attributes and re-defined comparison function;

To handle the updated sorted arrat, I use the min-hep to pop out the min two everty time and add a new virtual Node to the tree;
To imrpove the efficiency, a coding table is built;

The decoding basically follows the original methdo, go through tree untill itis a leaf point;

The time complexity of the Huffman algorithm is O(nlogn). By using a heap to store the weight of each tree, each iteration requires O(log n) time to place in the priority queue, and there are O(n) iterations, one for each item. The space complexity in building the Huffman Tree is O(#of distinct symbols in the data).
The decoding the time complexity is O(length of code) and space cmlexity is the tree space(O(n))