#!/usr/bin/env python3
"""Summarize a diagnostic worst-output CSV. No external dependencies.

Usage: python3 skills/ai-feature-go-no-go/analyze_failures.py skills/ai-feature-go-no-go/worst-20-template.csv

WARNING: These diagnostic counts are not representative failure rates.
"""
import argparse
import csv
from collections import Counter
from pathlib import Path

REQUIRED = {"case_id", "segment", "failure_type", "severity", "observed_output",
            "expected_behavior", "impact", "mitigation", "owner"}
SEVERITIES = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def analyze(path):
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV must have a header row")
        missing = REQUIRED - set(reader.fieldnames)
        if missing:
            raise ValueError("Missing CSV columns: " + ", ".join(sorted(missing)))
        cases = list(reader)

    if not cases:
        print("No cases yet. Fill in the CSV template and rerun.")
        return

    for index, case in enumerate(cases, start=2):
        severity = (case["severity"] or "").strip().lower()
        if severity not in SEVERITIES:
            raise ValueError(f"Line {index}: invalid severity {case['severity']!r}; "
                             "choose critical/high/medium/low")
        case["severity"] = severity

    def display(label, column):
        print(f"\n{label}")
        for value, count in Counter(
            (case[column] or "(missing)").strip() for case in cases
        ).most_common():
            print(f"  {value}: {count}")

    print(f"Diagnostic cases reviewed: {len(cases)}")
    print("NOTE: This worst-case collection is biased; counts are NOT error rates.")
    display("By failure type:", "failure_type")
    display("By segment (case counts, NOT rates):", "segment")
    display("By severity:", "severity")

    print("\nPriority cases (critical and high):")
    priority = sorted(
        (case for case in cases if case["severity"] in ("critical", "high")),
        key=lambda c: (SEVERITIES[c["severity"]], c["case_id"]),
    )
    if not priority:
        print("  None labeled critical/high; verify review coverage.")
    for case in priority:
        print(f"  [{case['severity'].upper()}] {case['case_id']}: "
              f"{case['failure_type']} | segment={case['segment']} "
              f"| owner={case['owner'] or 'UNASSIGNED'}")
    print("\nBefore launch: review representative evals with sample sizes, "
          "segment-level rates, guardrail tests and rollback gates.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="Path to de-identified failure CSV")
    args = parser.parse_args()
    try:
        analyze(args.csv_file)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"Error: {error}\n")


if __name__ == "__main__":
    main()
