<h1>encodings.py</h1>
 Utility helpers for explicit **bytes ⇔ str** conversions.  This revision adds *table‑driven* codecs so you can convert **without** relying on Python’s implicit ``bytes(data)`` or ``str.encode/bytes.decode`` helpers. A few widely used single‑byte encodings come pre‑loaded.  
<h2>Functions</h2>
<ul>
<li> <a href='#function-- **normalize_encoding'><code>
- **normalize_encoding(enc)**          → canonical codec name.
- **to_str(data, encoding="utf-8")**    → smart decode (unchanged).
- **to_bytes(data, encoding="utf-8")**  → smart encode (unchanged).
- **to_str_explicit(...)** / **to_bytes_explicit(...)**
  Table‑driven conversions that *never* call ``decode`` / ``encode``.
- **available_encodings()**            → runtime codec list.
</code></a> <br> </li>
<li> <a href='#function-The explicit helpers use frozen mapping tables '><code>
The explicit helpers use frozen mapping tables (``MappingProxyType``) built from
CPython’s own *decoding_table* definitions in the ``encodings`` package.  This
keeps the implementation pure Python yet 100 % standards‑compliant.
</code></a> <br> </li>
</ul>

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-normalize_encoding">
<strong>Function</strong>
<code>normalize_encoding</code></h1>
Return a canonical Python codec name for *enc*.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-_load_decoding_map">
<strong>Function</strong>
<code>_load_decoding_map</code></h1>
Return *immutable* mapping {byte:int→char:str}; empty if unavailable.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_str_explicit">
<strong>Function</strong>
<code>to_str_explicit</code></h1>
Decode using our explicit charmap when available (see docs).

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_bytes_explicit">
<strong>Function</strong>
<code>to_bytes_explicit</code></h1>
Encode using our explicit charmap when available (see docs).

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_str">
<strong>Function</strong>
<code>to_str</code></h1>
Back‑compat: thin wrapper around builtin decode.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-to_bytes">
<strong>Function</strong>
<code>to_bytes</code></h1>
Back‑compat: thin wrapper around builtin encode.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-available_encodings">
<strong>Function</strong>
<code>available_encodings</code></h1>
Return **sorted** unique codec names available in this runtime.

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-bytes_to_hex">
<strong>Function</strong>
<code>bytes_to_hex</code></h1>
Convert binary data to a hex string
(e.g. b'' → '0102') without using built-in .hex().

---
<div style="page-break-after: always; visibility: hidden"></div>
<br>
<h1 id="function-hex_to_bytes">
<strong>Function</strong>
<code>hex_to_bytes</code></h1>
Convert a hex string to bytes
(e.g. '0102' → b'') without using fromhex().

---