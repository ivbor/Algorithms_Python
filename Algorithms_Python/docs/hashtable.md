<h1>Hash Table Implementations with Open and Closed Addressing</h1>
  This module provides two hash table implementations: HashTable_closed and HashTable_open, using closed and open addressing, respectively, for collision resolution. Both implementations offer methods for adding, retrieving, and removing key-value pairs.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-gen_primes'><code>
gen_primes()
    Generate an infinite sequence of prime numbers for use as hash table
    capacity.
</code></a> <br> </li>
<li> <a href='#function-gen_prime'><code>
gen_prime(stop: int = 30) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Generate prime numbers up to a specified stop value.
<br></li>
<li> <a href='#function-poly_hash'><code>
poly_hash(x: Any) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculate a polynomial hash value for a given input.
<br></li>
</ul>

<h2>Classes</h2>
<ul>
<li> <a href='#class-HashTable_closed'><code>
HashTable_closed
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A hash table implementation using closed addressing (separate chaining) to    handle collisions.
<br></li>
<li> <a href='#class-HashTable_open'><code>
HashTable_open
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A hash table implementation using open addressing (multiple and cuckoo    hashing) to handle collisions with multiple hash functions.
<br></li>
<li> <a href='#class-PairsVector'><code>
PairsVector
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A specialized vector for storing key-value pairs in hash tables using    closed addressing.
<br></li>
<li> <a href='#class-ElementsList'><code>
ElementsList
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A specialized list for storing elements in hash tables using open    addressing.
<br></li>
<li> <a href='#class-Pair'><code>
Pair
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;
    A named tuple representing a key-value pair.
<br></li>
</ul>
---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-HashTable_closed">
<strong>Class</strong>
<code>HashTable_closed</code></h1>
A hash table implementation using closed addressing
for collision resolution.

This class represents a hash table that uses closed addressing
(separate chaining) to handle collisions.
It means that multiple key-value pairs with the same hash value
are stored in linked lists within the hash table.
It provides methods for adding, retrieving, and removing key-value pairs.


<h2>Attributes</h2>
<ul>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the hash table. <br></li>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number of key-value pairs currently stored in the hash table. <br></li>
<li> <strong>hashfunc</strong>: <em>str or callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The hashing function family used to determine the index for storing keys. Supported values: 'poly' (polynomial hash), 'md5', 'sha1', or a custom callable function. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, capacity: int = 30,
  hashfunc: str or callable = simple_hash,
  load_factor_threshold: float = 0.75) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes a HashTable_closed object with specified capacity
    and hash function.
<br></li>
<li> <a href='#function-__setitem__'><code>
__setitem__(self, key: Hashable, value: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Adds a key-value pair to the hash table.
<br></li>
<li> <a href='#function-__getitem__'><code>
__getitem__(self, key: Hashable) -> Any
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Retrieves the value associated with a given key.
<br></li>
<li> <a href='#function-__delitem__'><code>
__delitem__(self, key: Hashable) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Removes a key-value pair from the hash table.
<br></li>
<li> <a href='#function-to_dict'><code>
to_dict(self) -> dict
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns a dictionary representation of the hash table.
<br></li>
<li> <a href='#function-__contains__'><code>
__contains__(self, key: Hashable) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks if a key exists in the hash table.
<br></li>
<li> <a href='#function-from_dict'><code>
from_dict(cls, dictionary: dict) -> HashTable_closed
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Creates a new hash table from a dictionary.
<br></li>
<li> <a href='#function-__str__'><code>
__str__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns a string representation of the hash table.
<br></li>
<li> <a href='#function-__repr__'><code>
__repr__(self) -> str
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Used for printing the contents of the hash table.
<br></li>
<li> <a href='#function-__eq__'><code>
__eq__(self, other: HashTable_closed) -> bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Checks if two hash tables are equal.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a HashTable_closed object with specified capacity
and hash function.


<h2>Parameters</h2>
<ul>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the hash table. <br></li>
<li> <strong>hashfunc</strong>: <em>str or callable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The hashing function family used to determine the index for storing keys. Supported values: 'poly' (polynomial hash), 'md5', 'sha1', or a custom callable function. <br></li>
<li> <strong>load_factor_threshold</strong>: <em>float</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The maximum size / capacity ratio. When the actual value excesses this factor - the hashtable increases its size. When the actual value < this / 4 - the hashtable decreases its size. Can be set to any between 0 and 1, but is recommended to be set around 0.7 - 0.9. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_hash">
<strong>Function</strong>
<code>get_hash</code></h1>
Calculates the hash value for a given key
using the selected hash function.


<h2>Parameters</h2>
<ul>
<li> <strong>x</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be hashed. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The calculated hash value.   <br>
<h2>Raises</h2>
<strong>TypeError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;If hash function provided during init is not acceptable. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-pairs">
<strong>Function</strong>
<code>pairs</code></h1>
Property getter method for retrieving the pairs attribute
of the hash table.


<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A copy of the internal list of pairs in the hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-pairs">
<strong>Function</strong>
<code>pairs</code></h1>
Setter method for the pairs attribute.

<h2>Parameters</h2>
<ul>
<li> <strong>value</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value to be set (not used). <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; Raises ------ NotImplementedError: Always raised since the pairs attribute is read-only. <br>
<h2>Raises</h2>
<strong></strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-size">
<strong>Function</strong>
<code>size</code></h1>
Property getter method for retrieving the size attribute of the
hash table.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The number of key-value pairs currently stored in the hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-size">
<strong>Function</strong>
<code>size</code></h1>
Setter method for the size attribute.

<h2>Parameters</h2>
<ul>
<li> <strong>size</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value to be set (not used). <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; Raises ------ NotImplementedError: Always raised since the size attribute is read-only. <br>
<h2>Raises</h2>
<strong></strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-capacity">
<strong>Function</strong>
<code>capacity</code></h1>
Property getter method for retrieving the capacity attribute
of the hash table.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The current capacity of the hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-capacity">
<strong>Function</strong>
<code>capacity</code></h1>
Setter method for the capacity attribute.

<h2>Parameters</h2>
<ul>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value to be set (not used). <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; Raises ------ NotImplementedError: Always raised since the capacity attribute is read-only. <br>
<h2>Raises</h2>
<strong></strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__len__">
<strong>Function</strong>
<code>__len__</code></h1>
The number of key-value pairs currently stored in the hash table.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The size of the hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__setitem__">
<strong>Function</strong>
<code>__setitem__</code></h1>
Adds or updates (if already taken)
a key-value pair to the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be added. <br></li>
<li> <strong>x</strong>: <em>any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value associated with the key. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__getitem__">
<strong>Function</strong>
<code>__getitem__</code></h1>
Retrieves the value associated with a given key from the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>i</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key for which to retrieve the value. <br></li>
</ul>
<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value associated with the key.   <br>
<h2>Raises</h2>
<strong>    KeyError: If the key is not found in the hash table.</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-increase_capacity">
<strong>Function</strong>
<code>increase_capacity</code></h1>
Increases the capacity of the hash table.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-recapacitate_and_rehash">
<strong>Function</strong>
<code>recapacitate_and_rehash</code></h1>
Recalculates the hash values and rehashes the key-value pairs.


<h2>Parameters</h2>
<ul>
<li> <strong>old_capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The previous capacity of the hash table. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-decrease_capacity">
<strong>Function</strong>
<code>decrease_capacity</code></h1>
Decreases the capacity of the hash table.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Searches for a key in the hash table and returns the index if found,
or False if not found.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to search for. <br></li>
</ul>
<h2>Returns</h2>
<em>int or False</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the key in the hash table if found, or False if not found. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__delitem__">
<strong>Function</strong>
<code>__delitem__</code></h1>
Removes a key-value pair from the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be removed. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_dict">
<strong>Function</strong>
<code>to_dict</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- dict[Hashable, Any] A dictionary containing the key-value pairs from the hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__contains__">
<strong>Function</strong>
<code>__contains__</code></h1>
Checks if a key exists in the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to check for existence. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if the key exists in the hash table, False otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-from_dict">
<strong>Function</strong>
<code>from_dict</code></h1>
Creates a new HashTable_closed object from a dictionary.


<h2>Parameters</h2>
<ul>
<li> <strong>dictionary</strong>: <em>dict</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The dictionary to create the hash table from. <br></li>
</ul>
<h2>Returns</h2>
<em>HashTable_closed</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A new HashTable_closed object initialized with the contents of the dictionary. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__str__">
<strong>Function</strong>
<code>__str__</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- str A string representation of the hash table as a dictionary. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__repr__">
<strong>Function</strong>
<code>__repr__</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- str A string representation of the hash table as a dictionary. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__eq__">
<strong>Function</strong>
<code>__eq__</code></h1>
Checks if two hash tables are equal by comparing their
dictionary representations.


<h2>Parameters</h2>
<ul>
<li> <strong>other</strong>: <em>Mappable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Another object to compare. <br></li>
</ul>
<h2>Returns</h2>
<em>bool</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;True if the hash tables are equal, False otherwise. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="class-HashTable_open">
<strong>Class</strong>
<code>HashTable_open</code></h1>
A hash table implementation using open addressing
for collision resolution.
It provides methods for adding, retrieving, and removing key-value pairs.
This hash table uses open addressing (multiple and cuckoo hashing)
to resolve collisions, which means that when a collision occurs,
it looks for alternative positions within the table using multiple
hash functions.
Supported hash functions include 'md5', 'sha1', 'poly' (polynomial hash),
and custom callable functions.


<h2>Attributes</h2>
<ul>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the hash table. <br></li>
<li> <strong>hashfuncs</strong>: <em>list[str | Callable]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of hash functions used to determine the index for storing keys. Supported values: 'md5', 'sha1', 'poly' (polynomial hash), or custom callable functions. <br></li>
</ul>
<h2>Methods</h2>
<ul>
<li> <a href='#function-__init__'><code>
__init__(self, capacity: int = 30,
   hashfuncs: list[str | Callable] = [hash, simple_hash],
   max_displasements: int = 16) -> None:
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Initializes a HashTable_open instance with the given capacity
    and hash functions.
<br></li>
<li> <a href='#function-__setitem__'><code>
__setitem__(self, key: Hashable, value: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Adds a key-value pair to the hash table.
<br></li>
<li> <a href='#function-__getitem__'><code>
__getitem__(self, key: Hashable) -> Any
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Retrieves the value associated with a given key.
<br></li>
<li> <a href='#function-__delitem__'><code>
__delitem__(self, key: Hashable) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Removes a key-value pair from the hash table.
<br></li>
<li> <a href='#function-to_dict'><code>
to_dict(self) -> dict[Hashable, Any]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Returns a dictionary representation of the hash table.
<br></li>
<li> <a href='#function-update'><code>
update(self, key: Hashable, value: Any) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Updates the value associated with a given key in the hash table.
<br></li>
<li> <a href='#function-search'><code>
search(self, key: Hashable) -> tuple[int, int] | bool
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Searches for a key in the hash table and returns
    the table index and hashed key index if found, or False if not found.
<br></li>
<li> <a href='#function-increase_capacity'><code>
increase_capacity(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Increases the capacity of the hash table.
<br></li>
<li> <a href='#function-decrease_capacity'><code>
decrease_capacity(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Decreases the capacity of the hash table.
<br></li>
<li> <a href='#function-one_table_capacity'><code>
one_table_capacity(self) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Calculates the capacity of each individual
    hash table within the open addressing scheme.
<br></li>
<li> <a href='#function-get_hashes'><code>
get_hashes(self, key: Hashable) -> Generator[int, None, None]
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Generates hash values for a key using the specified hash functions.
<br></li>
<li> <a href='#function-current_hashed_key'><code>
current_hashed_key(self, key: Hashable, table_index: int) -> int
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Computes the hashed key index for a key based on
    the current table index.
<br></li>
<li> <a href='#function-recapacitate_and_rehash'><code>
recapacitate_and_rehash(self) -> None
</code></a> <br>
&nbsp;&nbsp;&nbsp;&nbsp;

    Recapacitates and rehashes hashtable.
<br></li>
</ul>


---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__init__">
<strong>Function</strong>
<code>__init__</code></h1>
Initializes a HashTable_open instance with the given capacity
and hash functions.


<h2>Parameters</h2>
<ul>
<li> <strong>capacity</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The initial capacity of the hash table, by default 30. <br></li>
<li> <strong>hashfuncs</strong>: <em>list[str | Callable]</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A list of hash functions used to determine the index for storing keys, by default ['md5', 'sha1']. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-one_table_capacity">
<strong>Function</strong>
<code>one_table_capacity</code></h1>
Calculates the capacity of each individual hash table
within the open addressing scheme.


<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The capacity of one hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-get_hashes">
<strong>Function</strong>
<code>get_hashes</code></h1>
Generates hash values for a key using the specified hash functions.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key for which hash values are generated. <br></li>
</ul>
<h2>Yields</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A hash value for the key. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-current_hashed_key">
<strong>Function</strong>
<code>current_hashed_key</code></h1>
Computes the hashed key index for a key based on the
current table index.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key for which the hashed key index is computed. <br></li>
<li> <strong>table_index</strong>: <em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The index of the hash table within the open addressing scheme. <br></li>
</ul>
<h2>Returns</h2>
<em>int</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The hashed key index for the key in the specified table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-elements">
<strong>Function</strong>
<code>elements</code></h1>
Defensive copying of the elements array.


<h2>Returns</h2>
<em>list</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A copy of the elements array. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__setitem__">
<strong>Function</strong>
<code>__setitem__</code></h1>
Adds a key-value pair to the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be added. <br></li>
<li> <strong>value</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value associated with the key. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-update">
<strong>Function</strong>
<code>update</code></h1>
Updates the value associated with a given key in the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key for which the value should be updated. <br></li>
<li> <strong>value</strong>: <em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The new value to associate with the key. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;  <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if no value is present for the corresponding key. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__delitem__">
<strong>Function</strong>
<code>__delitem__</code></h1>
Removes a key-value pair from the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be removed. <br></li>
</ul>
<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-__getitem__">
<strong>Function</strong>
<code>__getitem__</code></h1>
Retrieves the value associated with a given key in the hash table.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key for which the value is retrieved. <br></li>
</ul>
<h2>Returns</h2>
<em>Any</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The value associated with the key.   <br>
<h2>Raises</h2>
<strong>KeyError</strong> <br>
&nbsp;&nbsp;&nbsp;&nbsp;Raised if no value is found for the corresponding key. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-search">
<strong>Function</strong>
<code>search</code></h1>
Searches for a key in the hash table and returns
the table index and hashed key index if found,
or False if not found.


<h2>Parameters</h2>
<ul>
<li> <strong>key</strong>: <em>Hashable</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;The key to be searched for. <br></li>
</ul>
<h2>Returns</h2>
<em>tuple[int, int] or False</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;A tuple containing the table index and hashed key index if found, or False if the key is not present in the hash table. <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-recapacitate_and_rehash">
<strong>Function</strong>
<code>recapacitate_and_rehash</code></h1>
Recapacitates the hash table and rehashes its contents.


<h2>Returns</h2>
<em>None</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp; <br>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_dict">
<strong>Function</strong>
<code>to_dict</code></h1>

<h2>Returns</h2>
<em>Returns</em> <br>
&nbsp;&nbsp;&nbsp;&nbsp;------- dict A dictionary containing key-value pairs from the hash table. <br>

---