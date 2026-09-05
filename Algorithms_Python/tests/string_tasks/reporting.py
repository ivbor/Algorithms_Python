"""Report helpers for task-oriented string stress tests."""

from __future__ import annotations

import json
from pathlib import Path


ARTIFACT_DIR = Path(__file__).resolve().parents[1] / "artifacts"


def write_task_report(report: dict) -> tuple[Path, Path]:
    """Write machine-readable and human-readable stress-test reports."""
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    json_path = ARTIFACT_DIR / "string_task_stress_report.json"
    markdown_path = ARTIFACT_DIR / "string_task_stress_report.md"

    json_path.write_text(json.dumps(report, indent=2, sort_keys=True))
    markdown_path.write_text(_format_markdown_report(report))
    return json_path, markdown_path


def _format_markdown_report(report: dict) -> str:
    lines = [
        "# String Algorithm Task Stress Report",
        "",
        f"Seed: `{report['seed']}`",
        "",
        "## Results",
        "",
    ]

    for task in report["tasks"]:
        lines.extend(
            [
                f"### {task['task']}",
                "",
                f"Cases: `{task['cases']}`",
                f"Checks: `{task['checks']}`",
                "",
                "| Algorithm | Total seconds |",
                "| --- | ---: |",
            ]
        )
        for name, seconds in sorted(task["timings"].items()):
            lines.append(f"| `{name}` | {seconds:.6f} |")
        lines.append("")
        lines.append(task["summary"])
        lines.append("")

    return "\n".join(lines)
