# String Algorithm Task Stress Tests

The task-oriented stress suite lives in
`Algorithms_Python/tests/test_string_algorithm_tasks.py` and uses reusable
scenario builders from `Algorithms_Python/tests/string_tasks/`.

It compares string algorithms on jobs they are commonly selected for:

* single-pattern exact search: brute force, Rabin-Karp, KMP, Boyer-Moore,
  suffix arrays and suffix trees are checked against Python `find`;
* multi-pattern search: Aho-Corasick is checked against repeated exact
  searches, suffix-array lookups and suffix-tree containment checks;
* plagiarism-style shared passage search: suffix array plus Kasai LCP finds
  the longest common substring, while exact matchers and suffix trees confirm
  injected copied passages;
* prefix lookup: `PrefixTrie` is checked against Python `startswith` scans.

Running `pytest Algorithms_Python/tests/test_string_algorithm_tasks.py` writes
the latest machine-readable and Markdown reports to
`Algorithms_Python/tests/artifacts/`. Those files are intentionally ignored by
Git because they contain environment-specific timings.

## Latest Local Run

Command:

```bash
source venv/bin/activate
PYTHONPATH=venv/lib/python3.14/site-packages python3 -m pytest \
  Algorithms_Python/tests/test_string_algorithm_tasks.py \
  -q -o addopts='-q --show-capture=no'
```

Seed: `314159`

| Task | Cases | Checks |
| --- | ---: | ---: |
| Single-pattern exact search | 8 | 32 |
| Multi-pattern search | 4 | 2290 |
| Plagiarism-style shared passage search | 6 | 60 |
| Prefix lookup | 12 | 144 |

### Single-pattern exact search

| Algorithm | Total seconds |
| --- | ---: |
| Boyer-Moore | 0.002024 |
| Brute force | 0.010896 |
| KMP | 0.010429 |
| Rabin-Karp | 0.037579 |

### Multi-pattern search

| Algorithm | Total seconds |
| --- | ---: |
| Aho-Corasick | 0.013491 |
| Boyer-Moore | 0.194492 |
| Brute force | 0.528459 |
| KMP | 0.541118 |
| McCreight suffix tree build | 0.002552 |
| McCreight suffix tree lookup | 0.000193 |
| Rabin-Karp | 1.806271 |
| SA-IS suffix array build | 0.002593 |
| SA-IS suffix array lookup | 0.003586 |
| Ukkonen suffix tree build | 0.003488 |
| Ukkonen suffix tree lookup | 0.000179 |

### Plagiarism-style shared passage search

| Algorithm | Total seconds |
| --- | ---: |
| Boyer-Moore | 0.000185 |
| Brute force | 0.000263 |
| KMP | 0.000342 |
| McCreight suffix tree | 0.009145 |
| Rabin-Karp | 0.000976 |
| SA-IS suffix array | 0.006732 |
| SA-IS suffix array + Kasai LCP | 0.019412 |
| Ukkonen suffix tree | 0.011643 |

### Prefix lookup

| Algorithm | Total seconds |
| --- | ---: |
| PrefixTrie build | 0.024843 |
| PrefixTrie starts_with | 0.000086 |
| Python any startswith | 0.000448 |

The first version of this suite used tiny strings and only a handful of
patterns. That made `brute_force` look best almost everywhere because its
inner comparison is Python slicing backed by optimized C code, while KMP,
Boyer-Moore, Aho-Corasick and the suffix structures do more Python-level
bookkeeping. These revised workloads use the conditions where the algorithms
are normally chosen: Boyer-Moore gets long rare patterns, Aho-Corasick gets
hundreds of patterns in one pass, and suffix/prefix structures get many
queries after their indexes are built.
