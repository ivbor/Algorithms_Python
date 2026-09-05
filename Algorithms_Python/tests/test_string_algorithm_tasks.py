"""Task-oriented stress tests for string algorithms and string structures."""

from Algorithms_Python.tests.string_tasks.reporting import write_task_report
from Algorithms_Python.tests.string_tasks.scenarios import run_task_stress_suite


def test_string_algorithms_on_task_oriented_stress_cases():
    report = run_task_stress_suite()
    json_path, markdown_path = write_task_report(report)

    assert report["tasks"]
    assert json_path.exists()
    assert markdown_path.exists()
