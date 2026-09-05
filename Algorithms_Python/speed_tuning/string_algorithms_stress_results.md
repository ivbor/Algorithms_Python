# String Algorithms Stress Results

These timings come from the string stress tests in
`Algorithms_Python/tests/test_string_algorithms_stresses.py`.

They are correctness-oriented stress results, not a formal benchmark suite. The
inputs are deliberately small and varied, so the numbers are useful for spotting
large performance gaps and accidental regressions, but not for claiming stable
production throughput.

## Test Environment

Command:

```bash
source venv/bin/activate
PYTHONPATH=venv/lib/python3.14/site-packages python3 -m pytest \
  Algorithms_Python/tests/test_string_algorithms.py \
  Algorithms_Python/tests/test_trie.py \
  Algorithms_Python/tests/test_suffix_tree.py \
  Algorithms_Python/tests/test_string_algorithms_stresses.py \
  Algorithms_Python/tests/test_trie_stresses.py \
  -o addopts='-v --show-capture=no'
```

Result:

```text
88 passed in 0.41s
```

## Recorded Timings

### Suffix Array And LCP

Stress data:

```text
cases=1975, min_length=1, max_length=79, average_length=40.00,
alphabet=abcd
```

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| `suffix_array_sa_is` | 0.095038s total, 0.000048121s average | 0.013851s total, 0.000007013s average |
| `kasai_lcp` | 0.031249s total, 0.000015823s average | 0.026124s total, 0.000013227s average |

Approximate throughput:

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| `suffix_array_sa_is` | 20.8k cases/s | 142.6k cases/s |
| `kasai_lcp` | 63.2k cases/s | 75.6k cases/s |

### Single-Pattern Search

Stress data:

```text
cases=1350, min_text_length=0, max_text_length=89,
average_text_length=44.50, min_pattern_length=0, max_pattern_length=12,
average_pattern_length=5.88, alphabet=abcd
```

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| `boyer_moore` | 0.007521s total, 0.000005571s average | 0.003238s total, 0.000002399s average |

Approximate throughput:

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| `boyer_moore` | 179.5k cases/s | 416.8k cases/s |

### Prefix Trie

Stress data:

```text
insertions=500, distinct_words_after_delete=247, deletions=150,
exact_probes=797, prefix_probes=597, alphabet=abcde
```

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| Insert | 0.001505s total | n/a |
| Delete | 0.000259s total | n/a |
| Exact search | 0.000495s total | 0.000052s total |
| Prefix search | 0.000314s total | 0.003020s total |

Approximate throughput:

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| Insert | 332k ops/s | n/a |
| Delete | 579k ops/s | n/a |
| Exact search | 1.61M probes/s | 15.3M probes/s |
| Prefix search | 1.90M probes/s | 198k probes/s |

### Suffix Trees

Stress data for each builder:

```text
cases=34, min_length=1, max_length=34, substring_probes=1700,
random_probes=850, text_alphabet=abc, probe_alphabet=abcd
```

| Builder | Build time | Average build time |
| --- | ---: | ---: |
| `SuffixTree` | 0.000870s | 0.000025586s |
| `mccreight_suffix_tree` | 0.000923s | 0.000027134s |
| `ukkonen_suffix_tree` | 0.001293s | 0.000038019s |

Approximate build throughput:

| Builder | Throughput |
| --- | ---: |
| `SuffixTree` | 39.1k builds/s |
| `mccreight_suffix_tree` | 36.8k builds/s |
| `ukkonen_suffix_tree` | 26.3k builds/s |

Search timings:

| Builder | Developed search | Python substring baseline |
| --- | ---: | ---: |
| `SuffixTree` | 0.001854s total | 0.000161s total |
| `mccreight_suffix_tree` | 0.001886s total | 0.000163s total |
| `ukkonen_suffix_tree` | 0.001918s total | 0.000158s total |

Approximate search throughput:

| Builder | Developed search | Python substring baseline |
| --- | ---: | ---: |
| `SuffixTree` | 1.38M probes/s | 15.8M probes/s |
| `mccreight_suffix_tree` | 1.35M probes/s | 15.6M probes/s |
| `ukkonen_suffix_tree` | 1.33M probes/s | 16.1M probes/s |

### Aho-Corasick

Stress data:

```text
cases=69, min_text_length=1, max_text_length=69,
average_text_length=35.00, total_patterns=690,
average_pattern_length=3.89, alphabet=abcd
```

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| `aho_corasick` multi-pattern search | 0.004085s total, 0.000059200s average | 0.001349s total, 0.000019547s average |

Approximate throughput:

| Operation | Developed implementation | Baseline implementation |
| --- | ---: | ---: |
| `aho_corasick` multi-pattern search | 16.9k cases/s | 51.2k cases/s |

## Why The Educational Implementations Are Slower

The developed algorithms are asymptotically interesting, but the baselines are
not ordinary Python code. Python's built-in string, list, tuple, dictionary, and
set operations are implemented in optimized C and run tight loops without Python
bytecode dispatch for every step. The educational implementations in this
repository spend most of their time in Python-level loops, object allocation,
attribute lookups, dictionary access, list mutations, and recursive or
state-machine control flow.

This matters especially on small and medium inputs. The suffix-array stress
cases have average length 40 and maximum length 79. At that size, the constant
costs of SA-IS dominate: classifying positions, inducing buckets, remapping LMS
substrings, recursing, and rebuilding the result all require many Python
operations. The baseline uses Python's `sorted` over suffix start indexes. Even
though that comparison-based approach is not the theoretically optimal suffix
array algorithm, most of the sorting machinery is C-level Timsort, and the input
is small enough that lower constant overhead wins by a large margin.

Kasai LCP is much closer to the baseline because both implementations do similar
linear work once the suffix array is available. It still loses slightly because
the baseline oracle is simple on these short strings, while Kasai has setup
costs for rank arrays and explicit Python loop control.

Boyer-Moore uses extra preprocessing for bad-character and good-suffix shifts.
Those tables make the algorithm interesting on long texts and selective
patterns, but the stress cases here are short. The baseline brute-force checker
mostly spends its time in CPython substring comparisons, while this educational
version performs Python-level table construction and right-to-left loop control
for every case.

Suffix trees show the largest difference from the substring baseline during
search. Tree traversal is algorithmically valuable when the tree is reused for
many queries on larger text, but each search in this implementation follows
Python objects, edge labels, dictionaries, and per-character comparisons. The
baseline expression `probe in text` calls CPython's optimized string-search
implementation, which operates on compact string memory in C. For short strings
and short probes, that C loop is hard to beat, even if the suffix tree has a
better theoretical query model after preprocessing.

The prefix trie exact-search baseline is a Python `set` lookup, and hash-table
membership is one of the most optimized common operations in CPython. A trie
must walk one character at a time through nested nodes, so exact lookup is much
slower. Prefix lookup is the case where the trie wins in this stress test:
checking whether any word starts with a prefix is natural for a trie, while the
baseline has to scan candidate words and call `startswith`.

Aho-Corasick has the same educational-versus-built-in tradeoff. Its theoretical
advantage is that it searches for all patterns in one pass over the text after
building failure links. The stress inputs here are short, with average text
length 35 and ten short patterns per case. Building the trie and failure links
therefore costs more Python object work than the baseline spends repeatedly
calling the already-optimized brute-force matcher on tiny strings. On longer
texts with many patterns, Aho-Corasick is the algorithmic choice; in this test
shape, CPython's low constants still dominate.

The important conclusion is that these implementations are useful as readable
algorithmic references and correctness targets. They should not be expected to
beat CPython built-ins on small strings. To compete on speed, the same algorithms
would need lower-level implementation techniques: C extensions, Cython, Rust
bindings, array-backed node storage, fewer Python objects, batched benchmark
runs, and input sizes large enough for asymptotic differences to overcome
constant factors.
