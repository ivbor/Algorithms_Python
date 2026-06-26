<h1>Bloom Filter Module</h1>
  This module provides an implementation of a Bloom filter, a probabilistic data structure used to check whether an item is a member of a set with a certain probability of false positives. The Bloom filter is used for efficient membership testing.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-rot'><code>
rot(x) -> int
</code></a> <br> </li>
<li> <a href='#function-mix'><code>
mix(a, b, c) -> tuple[int, int, int]
</code></a> <br> </li>
<li> <a href='#function-final'><code>
final(a, b, c) -> tuple[int, int, int]
</code></a> <br> </li>
<li> <a href='#function-hashlittle2'><code>
hashlittle2(data, initval=0, initval2=0) -> int
</code></a> <br> </li>
<li> <a href='#function-hashlittle'><code>
hashlittle(data, initval=0) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    All functions above participate in calculating Jenkins hash of data
    using an optional seed.
<br></li>
</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-Bloom_filter'><code>
Bloom_filter(items_count=1000000, fp_prob=0.05, hashfunc='mmh3')
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Implements a Bloom filter data structure for efficient membership testing.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-hashlittle">
<strong>Function</strong>
<code>hashlittle</code></h1>
This function calculates Jenkins hash of data using initval as seed.

It utilises rot(), mix(), final(), hashlittle() functions to
calculate Jenkins hash as a python translation of the author's
original C++ algorithm.


<h2>Parameters</h2>
<ul>
<li> <strong>data</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Object of class with defined __getitem__ method consisting of characters (which could be passed to ord() function) <br></li>
<li> <strong>initval</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Seed for calculating hash Default value = 0 <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Jenkins hash of data <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Bloom_filter">
<strong>Class</strong>
<code>Bloom_filter</code></h1>
This is an implementation of the Bloom filter data structure.

Bloom filter is used to determine whether passed object has
already been passed to it. It has a false positive outcome
probability which depends on the expected items count to be passed
and amount of hash functions available.
This particular implementation requires expected false positives
probability and items to be passed count and determines its size
and creates all hash functions on its own provided the algorithm
for function family.


<h2>Attributes</h2>
<ul>
<li> <strong>fp_prob</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;False positives probability. Default value = 0.05 <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Real size of the structure, is calculated automatically <br></li>
<li> <strong>hash_count</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Amount of hashes needed to redeem fp_prob given items_count, is calculated automatically provided with hashfunc family <br></li>
<li> <strong>bit_array</strong>: <em>bitarray</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Special structure imported from bitarray module, allows usage of only one byte per bucket, compared to unlimited memory for integer values inside lists, hence taking much less memory. Consists of either 0's or 1's and has a size of self.size. It is the main storage and the filter itself. Cannot be modified directly, modifies itself when new values pass through filter. <br></li>
<li> <strong>hashfunc</strong>: <em>string</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Family of algorithms for generating hash functions. Default value = 'mmh3' (murmur3 hash), possible value = 'jenkins' for Jenkins hash <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, items_count: int = 1000000,
   fp_prob: float = 0.05, hashfunc: string = 'mmh3') -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

   Creates an instance of Bloom filter.
<br></li>
<li> <a href='#function-add'><code>
add(self, item: any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Passes through the Bloom filter given item.
<br></li>
<li> <a href='#function-check'><code>
check(self, item: any) -> Bloom_filter
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks whether the item was passed through Bloom filter.
<br></li>
<li> <a href='#function-get_size'><code>
get_size(self, items_count: int, fp_prob: float) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates full size of the Bloom filter.
<br></li>
<li> <a href='#function-get_hash_count'><code>
get_hash_count(self, size: int, items_count: int) -> int:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates the necessary amount of hash functions to ensure
    false positives probability with expected
    items to be passed count.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Creates an instance of Bloom filter


<h2>Parameters</h2>
<ul>
<li> <strong>items_count</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Expected amount of items to be passed through filter. Default value = 1000000 <br></li>
<li> <strong>fp_prob</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Expected false positive outcome probability. Default value = 0.05 <br></li>
<li> <strong>hashfunc</strong>: <em>'mmh3' or 'jenkins'</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Name of the family of functions to use for hash functions generation. Default value = 'mmh3' <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-add">
<strong>Function</strong>
<code>add</code></h1>
Passes given item through Bloom filter.


<h2>Parameters</h2>
<ul>
<li> <strong>item</strong>: <em>str or byte-like</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-check">
<strong>Function</strong>
<code>check</code></h1>
Checks whether the item was passed through the Bloom filter.


<h2>Parameters</h2>
<ul>
<li> <strong>item</strong>: <em>str or byte-like</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if the item was passed through, False if it was not. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_size">
<strong>Function</strong>
<code>get_size</code></h1>
Calculates the size of bloom filter for its initialization.


<h2>Parameters</h2>
<ul>
<li> <strong>items_count</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Amount of items expected to be passed through. <br></li>
<li> <strong>fp_prob</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;False positive case probability <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Size of the bloom filter. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_hash_count">
<strong>Function</strong>
<code>get_hash_count</code></h1>
Calculates amount of hash functions necessary to assure
required false probability.


<h2>Parameters</h2>
<ul>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Calculated size of the bloom filter. <br></li>
<li> <strong>items_count</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Amount of items expected to be passed through the filter. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Amount of hash functions to generate different hashes. <br>

---