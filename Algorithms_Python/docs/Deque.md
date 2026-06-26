<h1>Deque Module</h1>
  This module defines a Double-ended Queue (Deque) class, which represents a data structure that allows elements to be added or removed from both ends.  
<h2>Classes</h2>
<ul>
<li> <a href='#class-Deque'><code>
Deque
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Represents a Double-ended Queue (Deque) and provides methods for adding,    removing, and accessing elements from both ends.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-Deque">
<strong>Class</strong>
<code>Deque</code></h1>
Double-ended Queue (Deque) Class

The Deque class represents a double-ended queue,
which is a data structure that allows elements
to be added or removed from both ends.


<h2>Methods</h2>
<ul>
<li> <a href='#function-push_back'><code>
push_back(self, value)
    Add an element to the back (left) end of the deque,
    equivalent to enqueue in a queue.
</code></a> <br> </li>
<li> <a href='#function-pop_front'><code>
pop_front(self)
    Remove and return the element from the front (right) end of the deque,
    equivalent to dequeue in a queue.
</code></a> <br> </li>
<li> <a href='#function-pop_back'><code>
pop_back(self)
    Remove and return the element from the back (left) end of the deque,
    equivalent to pop in a stack.
</code></a> <br> </li>
<li> <a href='#function-push_front'><code>
push_front(self, value)
    Add an element to the front (right) end of the deque.
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-push_back">
<strong>Function</strong>
<code>push_back</code></h1>
Add an element to the back (left) end of the deque.


<h2>Parameters</h2>
<ul>
<li> <strong>value</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to be added to the deque. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-pop_front">
<strong>Function</strong>
<code>pop_front</code></h1>
Remove and return the element from the front (right) end of the deque.


<h2>Returns</h2>
<em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element removed from the front of the deque. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-pop_back">
<strong>Function</strong>
<code>pop_back</code></h1>
Remove and return the element from the back (left) end of the deque.


<h2>Returns</h2>
<em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element removed from the back of the deque. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-push_front">
<strong>Function</strong>
<code>push_front</code></h1>
Add an element to the front (right) end of the deque.


<h2>Parameters</h2>
<ul>
<li> <strong>value</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The element to be added to the front of the deque. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---