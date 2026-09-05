import logging
import random
import time

from Algorithms_Python.string_algorithms import find_pattern_brute_force
from Algorithms_Python.trie import aho_corasick, PrefixTrie


def test_stress_prefix_trie_against_set():
    random.seed(23456)
    trie = PrefixTrie()
    words = set()
    inserted = 0
    exact_probes = 0
    prefix_probes = 0
    deleted = 0
    insert_time = 0
    delete_time = 0
    developed_search_time = 0
    built_in_search_time = 0
    developed_prefix_time = 0
    built_in_prefix_time = 0

    for _ in range(500):
        word = _random_word('abcde', 0, 12)
        start_time = time.perf_counter()
        trie.insert(word)
        insert_time += time.perf_counter() - start_time
        words.add(word)
        inserted += 1

    for word in words:
        start_time = time.perf_counter()
        assert trie.search(word) is True
        developed_search_time += time.perf_counter() - start_time
        start_time = time.perf_counter()
        assert trie.starts_with(word[:len(word) // 2]) is True
        developed_prefix_time += time.perf_counter() - start_time
        exact_probes += 1
        prefix_probes += 1

    for probe in (_random_word('abcde', 0, 12) for _ in range(200)):
        start_time = time.perf_counter()
        built_in_search = probe in words
        built_in_search_time += time.perf_counter() - start_time
        start_time = time.perf_counter()
        developed_search = trie.search(probe)
        developed_search_time += time.perf_counter() - start_time
        start_time = time.perf_counter()
        built_in_prefix = any(word.startswith(probe) for word in words)
        built_in_prefix_time += time.perf_counter() - start_time
        start_time = time.perf_counter()
        developed_prefix = trie.starts_with(probe)
        developed_prefix_time += time.perf_counter() - start_time

        assert developed_search == built_in_search
        assert developed_prefix == built_in_prefix
        exact_probes += 1
        prefix_probes += 1

    for word in list(words)[:150]:
        start_time = time.perf_counter()
        assert trie.delete(word) is True
        delete_time += time.perf_counter() - start_time
        words.remove(word)
        deleted += 1

    for probe in (_random_word('abcde', 0, 12) for _ in range(200)):
        start_time = time.perf_counter()
        developed_search = trie.search(probe)
        developed_search_time += time.perf_counter() - start_time
        start_time = time.perf_counter()
        built_in_search = probe in words
        built_in_search_time += time.perf_counter() - start_time
        assert developed_search == built_in_search
        exact_probes += 1

    logging.debug(
        'PrefixTrie \n built_in: \n' +
        f'{sorted(words)} \n developed size: \n{trie.size}'
    )
    logging.info(
        'PrefixTrie stress statistics: ' +
        f'insertions={inserted}, distinct_words_after_delete={len(words)}, ' +
        f'deletions={deleted}, exact_probes={exact_probes}, ' +
        f'prefix_probes={prefix_probes}, alphabet=abcde'
    )
    logging.info(
        'PrefixTrie timing statistics: ' +
        f'insert_total={insert_time:.6f}s, delete_total={delete_time:.6f}s, ' +
        f'developed_exact_search_total={developed_search_time:.6f}s, ' +
        f'built_in_exact_search_total={built_in_search_time:.6f}s, ' +
        f'developed_prefix_total={developed_prefix_time:.6f}s, ' +
        f'built_in_prefix_total={built_in_prefix_time:.6f}s'
    )


def test_stress_aho_corasick_against_brute_force_oracle():
    random.seed(45678)
    cases = 0
    total_text_length = 0
    total_patterns = 0
    total_pattern_length = 0
    developed_time = 0
    built_in_time = 0
    logged_examples = 0

    for text_length in range(1, 70):
        text = _random_word('abcd', text_length, text_length)
        patterns = []
        for _ in range(10):
            patterns.append(_random_word('abcd', 0, 8))

        start_time = time.perf_counter()
        developed = aho_corasick(text, patterns)
        developed_time += time.perf_counter() - start_time

        start_time = time.perf_counter()
        expected = {}
        for pattern in patterns:
            if pattern not in expected:
                expected[pattern] = find_pattern_brute_force(text, pattern)
        built_in_time += time.perf_counter() - start_time

        assert developed == expected
        cases += 1
        total_text_length += text_length
        total_patterns += len(patterns)
        total_pattern_length += sum(len(pattern) for pattern in patterns)

        if logged_examples < 5:
            logging.debug(
                'aho_corasick \n built_in: \n' +
                f'{expected} \n developed: \n{developed}'
            )
            logged_examples += 1

    logging.info(
        'aho_corasick stress statistics: ' +
        f'cases={cases}, min_text_length=1, max_text_length=69, ' +
        f'average_text_length={total_text_length / cases:.2f}, ' +
        f'total_patterns={total_patterns}, ' +
        'average_pattern_length=' +
        f'{total_pattern_length / total_patterns:.2f}, alphabet=abcd'
    )
    logging.info(
        'aho_corasick timing statistics: ' +
        f'developed_total={developed_time:.6f}s, ' +
        f'built_in_total={built_in_time:.6f}s, ' +
        f'developed_avg={developed_time / cases:.9f}s, ' +
        f'built_in_avg={built_in_time / cases:.9f}s'
    )


def _random_word(alphabet, min_length, max_length):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(alphabet) for _ in range(length))
