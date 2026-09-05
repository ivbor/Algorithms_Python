"""Reusable task scenarios for string-algorithm stress tests.

The tests in this package deliberately look at algorithms through jobs that
users actually ask strings to solve:

* exact single-pattern search, where KMP, Boyer-Moore and Rabin-Karp compete;
* multi-pattern search, where Aho-Corasick should avoid rescanning the text;
* plagiarism-style shared passage search, where suffix arrays and suffix trees
  are natural indexing structures;
* prefix lookup, where the prefix trie is the intended data structure.

The inputs stay small enough for CI, but they are deliberately larger than
unit-test examples. Each task uses a workload shape that matches the algorithm:
long sparse searches for Boyer-Moore, many patterns for Aho-Corasick, and
many repeated queries after building suffix or prefix indexes.
"""

from __future__ import annotations

import random
import time
from collections import defaultdict
from typing import Callable, TypeVar

from Algorithms_Python.string_algorithms import (
    boyer_moore,
    find_pattern_brute_force,
    kasai_lcp,
    kmp,
    rabin_karp,
    suffix_array_sa_is,
)
from Algorithms_Python.suffix_tree import (
    mccreight_suffix_tree,
    ukkonen_suffix_tree,
)
from Algorithms_Python.trie import PrefixTrie, aho_corasick


ALPHABET = "abcde"
WIDE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
WORDS = (
    "alpha",
    "alpine",
    "algorithm",
    "beta",
    "better",
    "binary",
    "delta",
    "depth",
    "detect",
    "gamma",
    "garden",
    "graph",
    "suffix",
    "surface",
    "search",
)
T = TypeVar("T")


def run_task_stress_suite(seed: int = 314159) -> dict:
    """Run all task-oriented stress scenarios with deterministic data."""
    rng = random.Random(seed)
    tasks = [
        run_single_pattern_search(rng),
        run_multi_pattern_search(rng),
        run_plagiarism_search(rng),
        run_prefix_lookup(rng),
    ]
    return {"seed": seed, "tasks": tasks}


def run_single_pattern_search(rng: random.Random) -> dict:
    """Exercise exact matching algorithms on repeated and overlapping text."""
    timings: defaultdict[str, float] = defaultdict(float)
    checks = 0

    for case_number in range(8):
        pattern = _random_wide_word(rng, 24 + case_number % 5)
        text = _long_text_with_sparse_injections(rng, pattern, case_number)

        expected = _python_find_all(text, pattern)
        _assert_exact_matchers(text, pattern, expected, timings)
        checks += 4

    return _task_result(
        "Single-pattern exact search",
        8,
        checks,
        timings,
        "Long texts with rare long patterns show where Boyer-Moore can skip "
        "more positions than left-to-right matchers.",
    )


def run_multi_pattern_search(rng: random.Random) -> dict:
    """Compare one multi-pattern scan with repeated single-pattern scans."""
    timings: defaultdict[str, float] = defaultdict(float)
    checks = 0

    for case_number in range(2):
        patterns = [
            _random_wide_word(rng, 8 + index % 5)
            for index in range(240)
        ]
        text = _large_multi_pattern_text(rng, patterns, case_number)
        expected = {
            pattern: _python_find_all(text, pattern)
            for pattern in dict.fromkeys(patterns)
        }

        actual_aho = _time_call(
            timings,
            "aho_corasick",
            lambda: aho_corasick(text, patterns),
        )
        assert actual_aho == expected
        checks += 1

        for pattern, expected_positions in expected.items():
            _assert_exact_matchers(text, pattern, expected_positions, timings)
        checks += len(expected) * 4

    for case_number in range(2):
        patterns = [
            _random_word(rng, 5 + index % 4)
            for index in range(60)
        ]
        text = _multi_pattern_text(rng, patterns, case_number)
        expected = {
            pattern: _python_find_all(text, pattern)
            for pattern in dict.fromkeys(patterns)
        }
        _assert_suffix_index_batch(text, expected, timings)
        _assert_suffix_tree_batch(text, list(expected), timings)
        checks += len(expected) * 3 + 4

    return _task_result(
        "Multi-pattern search",
        4,
        checks,
        timings,
        "Aho-Corasick scans long text once for many patterns. Suffix arrays "
        "and suffix trees are measured as build-once, query-many indexes.",
    )


def run_plagiarism_search(rng: random.Random) -> dict:
    """Search for copied passages and longest shared substrings."""
    timings: defaultdict[str, float] = defaultdict(float)
    checks = 0

    for case_number in range(6):
        source = _document(rng, 95)
        start = 20 + case_number
        shared_passage = source[start:start + 45 + case_number % 12]
        suspect = _document(rng, 45) + shared_passage + _document(rng, 45)

        expected = _python_longest_common_substring(source, suspect)
        actual = _time_call(
            timings,
            "suffix_array_sa_is+kasai_lcp",
            lambda: _suffix_array_longest_common_substring(source, suspect),
        )
        assert len(actual) == len(expected)
        assert shared_passage in source
        assert shared_passage in suspect
        checks += 3

        expected_positions = _python_find_all(source, shared_passage)
        _assert_exact_matchers(
            source,
            shared_passage,
            expected_positions,
            timings,
        )
        _assert_suffix_indexes(
            source,
            shared_passage,
            expected_positions,
            timings,
        )
        _assert_suffix_trees(source, [shared_passage], timings)
        checks += 7

    return _task_result(
        "Plagiarism-style shared passage search",
        6,
        checks,
        timings,
        "Suffix indexes find the longest shared passage and exact matchers "
        "confirm injected copied spans.",
    )


def run_prefix_lookup(rng: random.Random) -> dict:
    """Compare trie prefix lookup with repeated Python prefix scans."""
    timings: defaultdict[str, float] = defaultdict(float)
    checks = 0

    for _ in range(12):
        words = [rng.choice(WORDS) + _random_word(rng, 4) for _ in range(800)]
        trie = _time_call(
            timings,
            "PrefixTrie.build",
            lambda: _build_trie(words),
        )

        prefixes = [
            "al",
            "alg",
            "alp",
            "be",
            "bet",
            "bi",
            "de",
            "det",
            "ga",
            "su",
            "sur",
            "zz",
        ]
        for prefix in prefixes:
            expected = any(word.startswith(prefix) for word in words)
            actual = _time_call(
                timings,
                "PrefixTrie.starts_with",
                lambda prefix=prefix: trie.starts_with(prefix),
            )
            baseline = _time_call(
                timings,
                "python_any_startswith",
                lambda prefix=prefix: any(
                    word.startswith(prefix)
                    for word in words
                ),
            )
            assert actual == baseline == expected
            checks += 1

    return _task_result(
        "Prefix lookup",
        12,
        checks,
        timings,
        "PrefixTrie checks whether any indexed word starts with a prefix.",
    )


def _assert_exact_matchers(
    text: str,
    pattern: str,
    expected: list[int],
    timings: defaultdict[str, float],
) -> None:
    matchers = {
        "brute_force": find_pattern_brute_force,
        "rabin_karp": rabin_karp,
        "kmp": kmp,
        "boyer_moore": boyer_moore,
    }
    for name, matcher in matchers.items():
        actual = _time_call(
            timings,
            name,
            lambda matcher=matcher: matcher(text, pattern),
        )
        assert actual == expected


def _assert_suffix_indexes(
    text: str,
    pattern: str,
    expected: list[int],
    timings: defaultdict[str, float],
) -> None:
    actual = _time_call(
        timings,
        "suffix_array_sa_is",
        lambda: _suffix_array_occurrences(text, pattern),
    )
    assert actual == expected


def _assert_suffix_index_batch(
    text: str,
    expected: dict[str, list[int]],
    timings: defaultdict[str, float],
) -> None:
    suffix_array = _time_call(
        timings,
        "suffix_array_sa_is.build",
        lambda: suffix_array_sa_is(text),
    )
    for pattern, expected_positions in expected.items():
        actual = _time_call(
            timings,
            "suffix_array_sa_is.lookup",
            lambda pattern=pattern: _suffix_array_occurrences_from_array(
                text,
                pattern,
                suffix_array,
            ),
        )
        assert actual == expected_positions


def _assert_suffix_trees(
    text: str,
    patterns: list[str],
    timings: defaultdict[str, float],
) -> None:
    for name, builder in (
        ("mccreight_suffix_tree", mccreight_suffix_tree),
        ("ukkonen_suffix_tree", ukkonen_suffix_tree),
    ):
        tree = _time_call(timings, name, lambda builder=builder: builder(text))
        for pattern in patterns:
            expected = _python_find_all(text, pattern) != []
            assert tree.search(pattern) is expected


def _assert_suffix_tree_batch(
    text: str,
    patterns: list[str],
    timings: defaultdict[str, float],
) -> None:
    for name, builder in (
        ("mccreight_suffix_tree.build", mccreight_suffix_tree),
        ("ukkonen_suffix_tree.build", ukkonen_suffix_tree),
    ):
        tree = _time_call(timings, name, lambda builder=builder: builder(text))
        lookup_name = name.replace(".build", ".lookup")
        for pattern in patterns:
            expected = _python_find_all(text, pattern) != []
            actual = _time_call(
                timings,
                lookup_name,
                lambda pattern=pattern: tree.search(pattern),
            )
            assert actual is expected


def _suffix_array_occurrences(text: str, pattern: str) -> list[int]:
    if pattern == "":
        return list(range(len(text) + 1))
    suffix_array = suffix_array_sa_is(text)
    return _suffix_array_occurrences_from_array(text, pattern, suffix_array)


def _suffix_array_occurrences_from_array(
    text: str,
    pattern: str,
    suffix_array: list[int],
) -> list[int]:
    return sorted(
        position
        for position in suffix_array
        if text.startswith(pattern, position)
    )


def _suffix_array_longest_common_substring(first: str, second: str) -> str:
    separator = "\0"
    joined = first + separator + second
    boundary = len(first)
    suffix_array = suffix_array_sa_is(joined)
    lcp = kasai_lcp(joined, suffix_array)
    best = ""

    for index, common_length in enumerate(lcp):
        left = suffix_array[index]
        right = suffix_array[index + 1]
        if (left < boundary) == (right < boundary):
            continue

        limited_length = min(
            common_length,
            _distance_to_separator(joined, left, boundary),
            _distance_to_separator(joined, right, boundary),
        )
        if limited_length > len(best):
            best = joined[left:left + limited_length]

    return best


def _python_longest_common_substring(first: str, second: str) -> str:
    best = ""
    for left in range(len(first)):
        for right in range(len(second)):
            length = 0
            while (
                left + length < len(first)
                and right + length < len(second)
                and first[left + length] == second[right + length]
            ):
                length += 1
            if length > len(best):
                best = first[left:left + length]
    return best


def _distance_to_separator(text: str, position: int, boundary: int) -> int:
    if position < boundary:
        return boundary - position
    return len(text) - position


def _text_with_injections(
    rng: random.Random,
    pattern: str,
    case_number: int,
) -> str:
    chunks = [_random_word(rng, 24) for _ in range(6)]
    injection_count = 2 + case_number % 4
    for index in range(injection_count):
        chunks.insert(1 + index * 2, pattern)
        if index % 2 == 0:
            chunks.insert(2 + index * 2, pattern[:3] + pattern)
    return "".join(chunks)


def _long_text_with_sparse_injections(
    rng: random.Random,
    pattern: str,
    case_number: int,
) -> str:
    text = _random_wide_word(rng, 20_000)
    if case_number % 2 == 0:
        insert_at = 3_000 + case_number * 900
        text = text[:insert_at] + pattern + text[insert_at:]
    return text


def _multi_pattern_text(
    rng: random.Random,
    patterns: list[str],
    case_number: int,
) -> str:
    chunks = [_random_word(rng, 18) for _ in range(10)]
    for index, pattern in enumerate(patterns):
        chunks.insert((index * 2 + case_number) % len(chunks), pattern)
        if index % 3 == 0:
            chunks.insert((index + 3) % len(chunks), pattern + pattern[:2])
    return "".join(chunks)


def _large_multi_pattern_text(
    rng: random.Random,
    patterns: list[str],
    case_number: int,
) -> str:
    chunks = [_random_wide_word(rng, 160) for _ in range(90)]
    for index, pattern in enumerate(patterns[:80]):
        chunks.insert((index * 3 + case_number) % len(chunks), pattern)
    return "".join(chunks)


def _document(rng: random.Random, words: int) -> str:
    return " ".join(rng.choice(WORDS) for _ in range(words))


def _build_trie(words: list[str]) -> PrefixTrie:
    trie = PrefixTrie()
    for word in words:
        trie.insert(word)
    return trie


def _random_word(rng: random.Random, length: int) -> str:
    return "".join(rng.choice(ALPHABET) for _ in range(length))


def _random_wide_word(rng: random.Random, length: int) -> str:
    return "".join(rng.choice(WIDE_ALPHABET) for _ in range(length))


def _python_find_all(text: str, pattern: str) -> list[int]:
    if pattern == "":
        return list(range(len(text) + 1))

    positions = []
    start = 0
    while True:
        position = text.find(pattern, start)
        if position == -1:
            return positions
        positions.append(position)
        start = position + 1


def _time_call(
    timings: defaultdict[str, float],
    name: str,
    callback: Callable[[], T],
) -> T:
    start = time.perf_counter()
    result = callback()
    timings[name] += time.perf_counter() - start
    return result


def _task_result(
    task: str,
    cases: int,
    checks: int,
    timings: defaultdict[str, float],
    summary: str,
) -> dict:
    return {
        "task": task,
        "cases": cases,
        "checks": checks,
        "timings": dict(timings),
        "summary": summary,
    }
