<h1>HyperLogLog Module</h1>
 This module implements the HyperLogLog algorithm for approximate cardinality estimation of large data sets.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-HyperLogLog'><code>
HyperLogLog
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A class implementing the HyperLogLog algorithm.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-HyperLogLog">
<strong>Class</strong>
<code>HyperLogLog</code></h1>
HyperLogLog Algorithm Implementation

This class provides methods to estimate the cardinality of a
large data set using the HyperLogLog algorithm.


<h2>Attributes</h2>
<ul>
<li> <strong>precision</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The precision parameter for the algorithm. This parameter corresponds to the amount of binary registers where the numbers will be written to. The higher the precision - the thinner bins for probability distribution for the algorithm. Default is 14. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, precision=14) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initialize HyperLogLog structure.
<br></li>
<li> <a href='#function-_hash'><code>
_hash(self, element: str) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Hash the element using SHA256.
<br></li>
<li> <a href='#function-_leading_zeros'><code>
_leading_zeros(self, binary_string: str) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Count the number of leading zeros in a binary string.
<br></li>
<li> <a href='#function-add'><code>
add(self, element: str) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Add an element to the HyperLogLog data structure.
<br></li>
<li> <a href='#function-count'><code>
count(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Estimate the cardinality of the data set.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initialize a HyperLogLog object with a given precision.


<h2>Parameters</h2>
<ul>
<li> <strong>precision</strong>: <em>int, optional</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The precision parameter for the algorithm. Default is 14. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_hash">
<strong>Function</strong>
<code>_hash</code></h1>
Hash the element using SHA256.


<h2>Parameters</h2>
<ul>
<li> <strong>element</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to be hashed. <br></li>
</ul>
<h2>Returns</h2>
<em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The binary hash value of the element. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_leading_zeros">
<strong>Function</strong>
<code>_leading_zeros</code></h1>
Count the number of leading zeros in a binary string.


<h2>Parameters</h2>
<ul>
<li> <strong>binary_string</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The binary string. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number of leading zeros. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add">
<strong>Function</strong>
<code>add</code></h1>
Add an element to the HyperLogLog data structure.


<h2>Parameters</h2>
<ul>
<li> <strong>element</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to be added. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-count">
<strong>Function</strong>
<code>count</code></h1>
Estimate the cardinality of the data set.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The estimated cardinality of the data set. <br>

---