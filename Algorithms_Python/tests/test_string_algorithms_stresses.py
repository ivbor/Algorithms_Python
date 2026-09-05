import logging
import random
import time

from Algorithms_Python.string_algorithms import (
    boyer_moore, find_pattern_brute_force, kasai_lcp, suffix_array_sa_is
)
from Algorithms_Python.suffix_tree import (
    mccreight_suffix_tree, SuffixTree, ukkonen_suffix_tree
)


def test_stress_suffix_array_and_lcp_against_naive_oracles():
    random.seed(12345)
    cases = 0
    total_length = 0
    logged_examples = 0
    suffix_array_time = 0
    built_in_suffix_array_time = 0
    lcp_time = 0
    built_in_lcp_time = 0

    for length in range(1, 80):
        for _ in range(25):
            text = ''.join(random.choice('abcd') for _ in range(length))
            start_time = time.perf_counter()
            suffix_array = suffix_array_sa_is(text)
            suffix_array_time += time.perf_counter() - start_time

            start_time = time.perf_counter()
            expected_suffix_array = \
                sorted(range(len(text)), key=lambda index: text[index:])
            built_in_suffix_array_time += time.perf_counter() - start_time

            start_time = time.perf_counter()
            expected_lcp = []
            for first, second in zip(suffix_array, suffix_array[1:]):
                common = 0
                while first + common < len(text) and \
                        second + common < len(text) and \
                        text[first + common] == text[second + common]:
                    common += 1
                expected_lcp.append(common)
            built_in_lcp_time += time.perf_counter() - start_time

            start_time = time.perf_counter()
            lcp = kasai_lcp(text, suffix_array)
            lcp_time += time.perf_counter() - start_time

            assert suffix_array == expected_suffix_array
            assert lcp == expected_lcp
            cases += 1
            total_length += length

            if logged_examples < 5:
                logging.debug(
                    'suffix_array_sa_is \n built_in: \n' +
                    f'{expected_suffix_array} \n developed: \n' +
                    f'{suffix_array}'
                )
                logging.debug(
                    'kasai_lcp \n built_in: \n' +
                    f'{expected_lcp} \n developed: \n' +
                    f'{lcp}'
                )
                logged_examples += 1

    logging.info(
        'suffix_array_sa_is and kasai_lcp stress statistics: ' +
        f'cases={cases}, min_length=1, max_length=79, ' +
        f'average_length={total_length / cases:.2f}, alphabet=abcd'
    )
    logging.info(
        'suffix_array_sa_is timing statistics: ' +
        f'developed_total={suffix_array_time:.6f}s, ' +
        f'built_in_total={built_in_suffix_array_time:.6f}s, ' +
        f'developed_avg={suffix_array_time / cases:.9f}s, ' +
        f'built_in_avg={built_in_suffix_array_time / cases:.9f}s'
    )
    logging.info(
        'kasai_lcp timing statistics: ' +
        f'developed_total={lcp_time:.6f}s, ' +
        f'built_in_total={built_in_lcp_time:.6f}s, ' +
        f'developed_avg={lcp_time / cases:.9f}s, ' +
        f'built_in_avg={built_in_lcp_time / cases:.9f}s'
    )


def test_stress_pattern_matching_against_brute_force_oracle():
    random.seed(56789)
    cases = 0
    total_text_length = 0
    total_pattern_length = 0
    developed_time = 0
    built_in_time = 0
    logged_examples = 0

    for text_length in range(0, 90):
        for _ in range(15):
            text = ''.join(random.choice('abcd')
                           for _ in range(text_length))
            pattern_length = random.randint(0, 12)
            pattern = ''.join(random.choice('abcd')
                              for _ in range(pattern_length))

            start_time = time.perf_counter()
            developed = boyer_moore(text, pattern)
            developed_time += time.perf_counter() - start_time

            start_time = time.perf_counter()
            expected = find_pattern_brute_force(text, pattern)
            built_in_time += time.perf_counter() - start_time

            assert developed == expected
            cases += 1
            total_text_length += text_length
            total_pattern_length += pattern_length

            if logged_examples < 5:
                logging.debug(
                    'boyer_moore \n built_in: \n' +
                    f'{expected} \n developed: \n{developed}'
                )
                logged_examples += 1

    logging.info(
        'boyer_moore stress statistics: ' +
        f'cases={cases}, min_text_length=0, max_text_length=89, ' +
        f'average_text_length={total_text_length / cases:.2f}, ' +
        'min_pattern_length=0, max_pattern_length=12, ' +
        f'average_pattern_length={total_pattern_length / cases:.2f}, ' +
        'alphabet=abcd'
    )
    logging.info(
        'boyer_moore timing statistics: ' +
        f'developed_total={developed_time:.6f}s, ' +
        f'built_in_total={built_in_time:.6f}s, ' +
        f'developed_avg={developed_time / cases:.9f}s, ' +
        f'built_in_avg={built_in_time / cases:.9f}s'
    )


def test_stress_suffix_trees_against_substring_oracle():
    random.seed(34567)
    stats = {builder.__name__: {'cases': 0, 'substring_probes': 0,
                                'random_probes': 0, 'build_time': 0,
                                'developed_search_time': 0,
                                'built_in_search_time': 0}
             for builder in (SuffixTree, mccreight_suffix_tree,
                             ukkonen_suffix_tree)}

    for builder in (SuffixTree, mccreight_suffix_tree, ukkonen_suffix_tree):
        logged_examples = 0
        for length in range(1, 35):
            text = ''.join(random.choice('abc') for _ in range(length))
            start_time = time.perf_counter()
            tree = builder(text)
            stats[builder.__name__]['build_time'] += \
                time.perf_counter() - start_time

            assert tree.suffix_indexes() == list(range(length))
            stats[builder.__name__]['cases'] += 1
            for _ in range(50):
                left = random.randrange(0, length)
                right = random.randrange(left, length + 1)
                start_time = time.perf_counter()
                assert tree.search(text[left:right]) is True
                stats[builder.__name__]['developed_search_time'] += \
                    time.perf_counter() - start_time
                stats[builder.__name__]['substring_probes'] += 1

            for _ in range(25):
                probe_length = random.randint(1, 8)
                probe = ''.join(random.choice('abcd')
                                for _ in range(probe_length))
                start_time = time.perf_counter()
                built_in = probe in text
                stats[builder.__name__]['built_in_search_time'] += \
                    time.perf_counter() - start_time
                start_time = time.perf_counter()
                developed = tree.search(probe)
                stats[builder.__name__]['developed_search_time'] += \
                    time.perf_counter() - start_time
                assert developed == built_in
                stats[builder.__name__]['random_probes'] += 1

                if logged_examples < 3:
                    logging.debug(
                        f'{builder.__name__} search \n built_in: \n' +
                        f'{built_in} \n developed: \n{developed}'
                    )
                    logged_examples += 1

    for builder_name, builder_stats in stats.items():
        logging.info(
            f'{builder_name} stress statistics: ' +
            f'cases={builder_stats["cases"]}, min_length=1, max_length=34, ' +
            f'substring_probes={builder_stats["substring_probes"]}, ' +
            f'random_probes={builder_stats["random_probes"]}, ' +
            'text_alphabet=abc, probe_alphabet=abcd'
        )
        logging.info(
            f'{builder_name} timing statistics: ' +
            f'build_total={builder_stats["build_time"]:.6f}s, ' +
            'build_avg=' +
            f'{builder_stats["build_time"] / builder_stats["cases"]:.9f}s, ' +
            'developed_search_total=' +
            f'{builder_stats["developed_search_time"]:.6f}s, ' +
            'built_in_search_total=' +
            f'{builder_stats["built_in_search_time"]:.6f}s'
        )
