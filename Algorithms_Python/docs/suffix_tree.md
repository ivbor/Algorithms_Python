<h1>Suffix Tree</h1>
  This module contains compressed suffix tree structures and construction algorithms.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-mccreight_suffix_tree'><code>
mccreight_suffix_tree(text: str) -> SuffixTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Builds a suffix tree using McCreight construction.
<br></li>
<li> <a href='#function-ukkonen_suffix_tree'><code>
ukkonen_suffix_tree(text: str) -> SuffixTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Builds a suffix tree using Ukkonen construction.
<br></li>
</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-SuffixTreeNode'><code>
SuffixTreeNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Node used by compressed suffix trees.
<br></li>
<li> <a href='#class-SuffixTree'><code>
SuffixTree
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Compressed suffix tree with substring search and suffix-index traversal.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-SuffixTreeNode">
<strong>Class</strong>
<code>SuffixTreeNode</code></h1>
Node used by compressed suffix trees.


<h2>Attributes</h2>
<ul>
<li> <strong>children</strong>: <em>dict[str, SuffixTreeNode]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Outgoing compressed edges by their first character. <br></li>
<li> <strong>start</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Inclusive edge-label start in the tree text. <br></li>
<li> <strong>end</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Exclusive edge-label end in the tree text. <br></li>
<li> <strong>suffix_index</strong>: <em>int | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Starting position of the suffix ending at this leaf. <br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-SuffixTree">
<strong>Class</strong>
<code>SuffixTree</code></h1>
Compressed suffix tree with substring search.

The tree stores all suffixes of one text. A private terminator is appended
when needed so every suffix ends at a distinct leaf.


<h2>Attributes</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Original text without the private terminator. <br></li>
<li> <strong>root</strong>: <em>SuffixTreeNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Root node of the compressed suffix tree. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-insert'><code>
insert(text: str)
    Rebuild the suffix tree for text.
</code></a> <br> </li>
<li> <a href='#function-search'><code>
search(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check whether text is a substring of the stored text.
<br></li>
<li> <a href='#function-starts_with'><code>
starts_with(prefix: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check whether the stored text starts with prefix.
<br></li>
<li> <a href='#function-delete'><code>
delete(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Not supported for suffix trees.
<br></li>
<li> <a href='#function-suffix_indexes'><code>
suffix_indexes() -> list[int]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Return all suffix indexes represented by leaves.
<br></li>
<li> <a href='#function-Examples
--------
>>> tree = SuffixTree'><code>
Examples
--------
>>> tree = SuffixTree("banana")
>>> tree.search("ana")
True
>>> tree.suffix_indexes()
[0, 1, 2, 3, 4, 5]
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Rebuild the suffix tree for text.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Check whether text is a substring of the stored text.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-starts_with">
<strong>Function</strong>
<code>starts_with</code></h1>
Check whether the stored text starts with prefix.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-delete">
<strong>Function</strong>
<code>delete</code></h1>
Suffix trees in this module are static and do not support deletion.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-suffix_indexes">
<strong>Function</strong>
<code>suffix_indexes</code></h1>
Return all suffix indexes represented by leaves.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-mccreight_suffix_tree">
<strong>Function</strong>
<code>mccreight_suffix_tree</code></h1>
Build a suffix tree using McCreight construction.

McCreight construction inserts suffixes from left to right. After an
insertion creates a head node, the next suffix starts from that head's
suffix link and uses fast-find to descend over already-known edge labels.

Time complexity: O(n)
Space complexity: O(n)


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Text for which the suffix tree is built. <br></li>
</ul>
<h2>Returns</h2>
<em>SuffixTree</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Compressed suffix tree storing all suffixes of text.  Examples -------- >>> tree = mccreight_suffix_tree("banana") >>> tree.search("ana") True <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-ukkonen_suffix_tree">
<strong>Function</strong>
<code>ukkonen_suffix_tree</code></h1>
Build a suffix tree using Ukkonen construction.

Ukkonen construction adds the text one phase at a time while maintaining
an active point and a remainder of suffixes still to extend.

Time complexity: O(n)
Space complexity: O(n)


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Text for which the suffix tree is built. <br></li>
</ul>
<h2>Returns</h2>
<em>SuffixTree</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Compressed suffix tree storing all suffixes of text.  Examples -------- >>> tree = ukkonen_suffix_tree("banana") >>> tree.search("nan") True <br>

---