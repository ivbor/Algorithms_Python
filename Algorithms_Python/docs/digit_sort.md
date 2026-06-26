<h1>Digit Sort</h1>
  This module provides functions for performing digit sort, a sorting algorithm specifically designed for integers.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-digit_sort'><code>
digit_sort(array: list[int], base: int = 10) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Sort a list of non-negative integers using the digit sort algorithm.
<br></li>
<li> <a href='#function-to_m_based'><code>
to_m_based(number: int, base: int) -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Convert a decimal number to an M-based representation.
<br></li>
<li> <a href='#function-restore_to_nums'><code>
restore_to_nums(array: list[int], base: int = 10) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Restore an M-based representation to its decimal form.
<br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_m_based">
<strong>Function</strong>
<code>to_m_based</code></h1>
Convert a decimal number to an M-based representation.

This function converts a decimal number into its M-based
representation, where M is the specified base. The result
is returned as a list of digits in the M-based representation.
Optionally, you can choose to return the result as an array or
restore it to its original decimal form.


<h2>Parameters</h2>
<ul>
<li> <strong>number</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The decimal number to be converted to an M-based representation. <br></li>
<li> <strong>base</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The base (M) to which the number should be converted. It must be a positive integer greater than or equal to 2. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of integers representing the M-based representation of the decimal number. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-restore_to_nums">
<strong>Function</strong>
<code>restore_to_nums</code></h1>
Restore an M-based representation to its decimal form.

This function takes a list of digits representing an M-based
representation and restores it to its original decimal form.
You can specify the base (M) used for the representation,
which defaults to 10 for decimal restoration.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of digits representing an M-based number. <br></li>
<li> <strong>base</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The base (M) used for the M-based representation. It must be a positive integer greater than or equal to 2. The default value is 10 for decimal restoration. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The decimal number restored from the M-based representation. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-digit_sort">
<strong>Function</strong>
<code>digit_sort</code></h1>
This function performs digit sort on a list of non-negative integers.

Digit sort is a sorting algorithm that works specifically for
non-negative integers. It sorts the integers by their individual
digits, starting from the least significant digit to the most
significant digit. This algorithm has a time complexity of O(n * k),
where n is the number of integers in the input list and k is
the maximum number of digits in any integer inside array.
It is important that the amount of digits can be reduced by
changing the base for the integers. Hence, when k = 1 this sort
appears to be counting sort with O(n) time complexity.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of non-negative integers to be sorted using digit sort.
base: int The array's integers' base depending on which number of digits will be determined. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A sorted list of non-negative integers. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-digit_sort_opt">
<strong>Function</strong>
<code>digit_sort_opt</code></h1>
Sort a list of non-negative integers using the digit + radix sort
algorithm.


<h2>Parameters</h2>
<ul>
<li> <strong>array</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of non-negative integers to be sorted using digit sort.
base: int The array's integers' base depending on which number of digits will be determined. <br></li>
</ul>
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A sorted list of non-negative integers. <br>

---