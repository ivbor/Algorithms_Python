<h1>Array Counting Sort Module</h1>
  
<h2>Functions</h2>
<ul>
<li> <a href='#function-array_count_sort'><code>
array_count_sort(arr: list[list[int]], key: int = 0) -> list[list[int]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sort a 2-dimensional array of integers based on a key index.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-array_count_sort">
<strong>Function</strong>
<code>array_count_sort</code></h1>
This function performs counting sort on the 2-dimensional array
of whole numbers.

This algorithm uses count sort to sort rows inside matrix
by ascending order. It works only with integer numbers,
so if your matrix contains floats - do not use this algorithm.
Time to work: O(number of rows in the array) or
O(difference between the biggest and the lowest value
in the key index) depending on what is more.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;2-dimensional array which will be sorted <br></li>
<li> <strong>key</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Shows by which index to sort, works even in situations when there are blank spaces with this index in the rows. In this case puts those rows higher than those with filled spaces. Default value: 0 <br></li>
</ul>
<h2>Returns</h2>
<em>list[list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Sorted array <br>

---