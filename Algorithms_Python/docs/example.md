<!--I HATE HTML BUT MARKDOWN CAN DO ALMOST NOTHING WITHOUT IT-->

<!--Hence, here is what's what-->

<!--h1 equals == in markdown-->

<!--h2 equals -- in markdown-->

<!--br breaks the line-->

<!--ul starts unordered list-->

<!--li is an entry in unordered list-->

<!--&nbsp is just a usual space-->

<!--strong is for bold-->

<!--em for italic-->

<h1>Bloom Filter Module</h1>
This module provides an implementation of a Bloom filter, a probabilistic
data structure used to check whether an item is a member of a set with a
certain probability of false positives. The Bloom filter is used
for efficient membership testing.
<h2>Functions</h2>
<ul>
<li> <a href='#function-rot'><code>
rot(x)
</code></a> <br> </li>
<li> <a href='#function-mix'><code>
mix(a, b, c)
</code></a> <br> </li>
<li> <a href='#function-final'><code>
final(a, b, c)
</code></a> <br> </li>
<li> <a href='#function-hashlittle2'><code>
hashlittle2(data, initval=0, initval2=0)
</code></a> <br> </li>
<li> <a href='#function-hashlittle'><code>
hashlittle2(data, initval=0)
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
All functions above participate in calculating Jenkins hash of data using 
an optional seed.
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

______________________________________________________________________

<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id='function-rot'>
<strong>Function</strong> 
<code>rot</code></h1>
<h2>Parameters</h2>
<ul> <!--Do not forget to close! -->
<li> <strong>x</strong></li>
<li> <strong>k</strong></li>
<li> <strong>parent</strong>: <em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;List where each vertex's index, being the index of the 
list, has its parent, index of vertex from which it was visited first, being 
the value in the list.<br></li>
</ul> <!-- Yesssss -->
<h2>Returns</h2>
<em>list[int]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Path from the start vertex to the target, including 
both.

______________________________________________________________________

<div style="page-break-after: always;"></div>
<br>
<h1 id='class-Graph_util'>
<strong>Class</strong> 
<code>Graph_util</code></h1>
Class storing utility methods for the main graph class.
<h2>Attributes</h2>
<ul>
<li> <strong>attribute1</strong>: <em>type</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Description. <br></li>
<li> <strong>attribute2</strong>: <em>type</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Description. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <code>
_find_arg(self, default: Any, arg_dict: dict[int, str], *args, **kwargs) -> Any

</code> <br>
<a href='#function-_find_arg' style='color: blue'>[to the method]</a> <br>
Method finding index of the vertex to remove among
kwargs by data or index. <br> </li>

<li> <code>
_find_index(self, **kwargs) -> int | None

</code> <br>
<a href='#function-_find_index' style='color: blue'>[to the method]</a> <br>
Method finding index of the vertex to remove among
kwargs by data or index. <br> </li>

<li> <code>
tarjan_dfs(self, vertex: int, index: list[int], stack: list[int], low_link: 
list[int], on_stack: list[bool], scc: list[list[int]]) -> None
</code> <br> 
<a href='#function-tarjan_dfs' style='color: blue'>[to the method]</a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Utility method which is used by tarjan_scc method. <br>
</li>
</ul>

______________________________________________________________________

<div style="page-break-after: always;"></div>
<br>
<h1 id='function-_find_arg'>
<strong>Function</strong> 
<code>_find_arg</code></h1>
Find the required argument among args.
<h2>Parameters</h2>
<ul>
<li> <strong>default</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Value to be returned if the required argument was not 
provided. <br> </li>
<li><strong>arg_dict</strong>: <em>dict[int, str]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Dictionary where index corresponds to the possible 
argument position in args, and value - in kwargs. <br> </li>
</ul>
<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The required argument found within args or kwargs or 
the default value if the argument was not found.

______________________________________________________________________

<div style="page-break-after: always;"></div>
<br>
<h1 id='function-_find_index'>
<strong>Function</strong> 
<code>_find_index</code></h1>
Find index of the vertex by data or index provided in kwargs for further 
removal.
<h2>Parameters</h2>
<ul>
<li> <strong>kwargs['index']</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Index of the vertex to remove. <br>
&nbsp;&nbsp;&nbsp;&nbsp;or </li>
<li> <strong>kwargs['data']</strong>: <em>Any</em>
&nbsp;&nbsp;&nbsp;&nbsp;Data inside the vertex to remove. <br> </li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the vertex to remove. <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If data or index were not found among kwargs.

______________________________________________________________________
