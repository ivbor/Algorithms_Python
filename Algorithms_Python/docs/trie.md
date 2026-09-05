<h1>Trie Structures</h1>
  This module contains trie-like string data structures and algorithms.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-aho_corasick'><code>
aho_corasick(text: str, patterns: list[str]) -> dict[str, list[int]]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Finds all occurrences of many patterns using the Aho-Corasick algorithm.
<br></li>
</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-AbstractTrie'><code>
AbstractTrie
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Common interface for trie-like string data structures.
<br></li>
<li> <a href='#class-TrieNode'><code>
TrieNode
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Node used by trie-like structures.
<br></li>
<li> <a href='#class-PrefixTrie'><code>
PrefixTrie
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    Concrete prefix trie for storing whole words and prefix queries.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-AbstractTrie">
<strong>Class</strong>
<code>AbstractTrie</code></h1>
Common interface for trie-like string data structures.


<h2>Methods</h2>
<ul>
<li> <a href='#function-insert'><code>
insert(text: str)
    Insert text into the trie-like structure.
</code></a> <br> </li>
<li> <a href='#function-search'><code>
search(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check whether text is present.
<br></li>
<li> <a href='#function-starts_with'><code>
starts_with(prefix: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check whether at least one stored text starts with prefix.
<br></li>
<li> <a href='#function-delete'><code>
delete(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Delete text if the concrete structure supports deletion.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Insert text into the trie-like structure.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Check whether text is present.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-starts_with">
<strong>Function</strong>
<code>starts_with</code></h1>
Check whether at least one stored text starts with prefix.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-delete">
<strong>Function</strong>
<code>delete</code></h1>
Delete text from the trie-like structure.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-TrieNode">
<strong>Class</strong>
<code>TrieNode</code></h1>
Node used by trie-like structures.


<h2>Attributes</h2>
<ul>
<li> <strong>children</strong>: <em>dict[str, TrieNode]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Outgoing transitions by character. <br></li>
<li> <strong>is_terminal</strong>: <em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Whether this node ends an inserted word. <br></li>
<li> <strong>output</strong>: <em>list[str]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Patterns ending exactly at this node. <br></li>
<li> <strong>matched_output</strong>: <em>list[str]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Patterns reported by Aho-Corasick when it reaches this node. It contains this node's output and outputs inherited through failure links. <br></li>
<li> <strong>failure</strong>: <em>TrieNode | None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Aho-Corasick fallback link to the longest proper suffix represented by another trie node. <br></li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-PrefixTrie">
<strong>Class</strong>
<code>PrefixTrie</code></h1>
Concrete prefix trie for storing words.


<h2>Attributes</h2>
<ul>
<li> <strong>root</strong>: <em>TrieNode</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Root node of the trie. <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Number of distinct words stored in the trie. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-insert'><code>
insert(text: str)
    Insert a word.
</code></a> <br> </li>
<li> <a href='#function-search'><code>
search(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check whether a word is stored.
<br></li>
<li> <a href='#function-starts_with'><code>
starts_with(prefix: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Check whether a stored word has the given prefix.
<br></li>
<li> <a href='#function-delete'><code>
delete(text: str) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Delete a stored word.
<br></li>
<li> <a href='#function-Examples
--------
>>> trie = PrefixTrie'><code>
Examples
--------
>>> trie = PrefixTrie()
>>> trie.insert("cart")
>>> trie.starts_with("car")
True
>>> trie.search("car")
False
</code></a> <br> </li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-insert">
<strong>Function</strong>
<code>insert</code></h1>
Insert a word.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Check whether a word is stored.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-starts_with">
<strong>Function</strong>
<code>starts_with</code></h1>
Check whether a stored word has the given prefix.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-delete">
<strong>Function</strong>
<code>delete</code></h1>
Delete a stored word.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-aho_corasick">
<strong>Function</strong>
<code>aho_corasick</code></h1>
Find all occurrences of many patterns using Aho-Corasick algorithm.

The algorithm first builds a prefix trie of the patterns. Then it adds
failure links, which are the multi-pattern analogue of the fallback links
used by Knuth-Morris-Pratt: after a mismatch, the search jumps to the
longest suffix that is also a prefix of at least one pattern.

Time complexity: O(n + m + z), where n is text length, m is the total
pattern length, and z is the number of reported matches.
Space complexity: O(m + z).


<h2>Parameters</h2>
<ul>
<li> <strong>text</strong>: <em>str</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Text in which to search. <br></li>
<li> <strong>patterns</strong>: <em>list[str]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Patterns to search for. Duplicate patterns are treated as one pattern because the result is keyed by pattern text. <br></li>
</ul>
<h2>Returns</h2>
<em>dict[str, list[int]]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Mapping from every distinct pattern to all starting indexes where it occurs in the text.  Examples -------- >>> aho_corasick("ushers", ["he", "she", "his", "hers"]) {'he': [2], 'she': [1], 'his': [], 'hers': [2]} <br>

---