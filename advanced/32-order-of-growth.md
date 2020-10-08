 ### Order of Growth for various python operations
 
 |Operation|Example|OoG|
 |----|----|----|
 |Variable assignment |  a = 1 | Constant Time|
 |Addition|c = a + b|Constant time|
 |Subtraction|c = a - b|Constant time|
 |Multiplication|c = a * b|Constant time|
 |Division|c = a / b|Constant time|
 |Find an element in the list|list[4]|Constant time|
 |For loop to get few elements|for element in list: print(e)|Linear O(n)|
 |String concat|name = "First" + "last"|Linear O(n)|
 |Getting a char from string|char = String[0]|Constant time|
 |Get len of string|len(string)|Constant time|
 |Adding a list of Strings|for i in range(10): a += "hello" |Quadratic O(n^2) |
 |Sorting List|list.sort()|Linear O(n log n)|
 |Adding to list|list.append(4)|Constant time|
 |Copy a list|list1 = list2|Linear O(n)|
 |Dictionary operations|dict = {0,1} |Constant time|
 
 ### Search Algorithms
 
|Operation|OoG|
|----|----|
|Linear search| Linear O(n)|
|Binary search| Logarithmic O(log n)|

### Sorting Algorithms

|Operation|OoG|
|----|----|
|Bogo Sort| Unbounded O(n+1)!|
|Selection Sort|**O(n^2)** for search & O(n) swaps|
|Insertionn Sort|**O(n^2)** and O(n^2) swaps|
|Bubble Sort|**O(n^2)** and O(n^2) swaps|
|Quick Sort| **O(n^2)** and O(n^2) swaps|
|Merge Sort|O(n log n)|
