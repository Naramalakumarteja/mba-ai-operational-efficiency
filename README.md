# Artificial Intelligence Adoption and Operational Efficiency

An MBA research project on productivity, cost optimization, and managerial decision-making in Chennai IT-enabled service operations. Operations Management is the primary domain; Data Analytics is the analytical methodology.

## Overview and problem statement

The project examines whether reported operational AI use is associated with perceived efficiency. It separates actual use from perceptions of benefits and distinguishes productivity, process efficiency, cost optimization, and decision effectiveness. It is a cross-sectional survey design, not a causal study.

**Evidence status:** the research design and questionnaire are drafted. No participant review, pilot, main survey dataset, or empirical results exist. This repository is a working research-design deliverable, not a completed empirical dissertation or an institution-approved submission.

## Implemented features

- Existing Chapters 1–3 and scholarly references preserved.
- One maintained questionnaire source, integrated at build time as Appendix A.
- Explicit evidence-status Chapters 4–5, without fabricated statistical tables.
- Offline HTML report with section navigation, responsive layout, readable tables, and browser print/save-as-PDF.
- Source checks for chapter completeness, questionnaire items, duplicate appendix, and machine-specific paths.
- Automated tests of navigation, output, error handling, and raw HTML escaping.

## Technology and architecture

Python 3.10+ and Python-Markdown 3.11. No database, backend framework, cloud service, API key, or JavaScript dependency is needed. The small inline print action uses the browser's native print dialog.

Workflow: report Markdown + questionnaire Markdown → source validation → Markdown rendering → self-contained HTML. Historical review/recruitment documents remain available but are not required to view or build the main report.

## Setup

From the repository folder:

```sh
python -m venv .venv
```

Activate on Windows PowerShell with `.\.venv\Scripts\Activate.ps1`, or on macOS/Linux with `source .venv/bin/activate`, then:

```sh
python -m pip install -r requirements.txt
```

No environment variables are required. No `.env` file should be created or committed.

## Build, run, and example usage

```sh
python build_report.py
```

Open `outputs/MBA_Project_Report.html` in a browser. It works offline without a server. Use section links to navigate and **Print / Save as PDF** for browser printing. For a local web preview:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory outputs
```

Visit `http://127.0.0.1:8000/MBA_Project_Report.html`. Stop the server with Ctrl+C. The server is a local read-only preview, not a survey collector. Rebuild after editing sources. An alternate destination is supported with `python build_report.py --output outputs/preview.html`.

## Tests and syntax checks

```sh
python -m unittest discover -s tests -v
python -m py_compile build_report.py tests/test_report.py
```

Tests use no real participant data and do not validate the questionnaire scientifically. There is no configured linter or type-checking tool; neither is required to build this small document renderer.

## Project structure

```text
build_report.py                   Report builder and source validation
requirements.txt                  Single pinned rendering dependency
tests/test_report.py              Critical automated checks
outputs/
  MBA_Project_Chapters_1_to_3.md   Main report source (historical filename)
  MBA_Draft_Questionnaire.md       Canonical questionnaire source
  MBA_Project_Report.html         Generated offline report, ignored by Git
  other .md files                 Existing research support documents
work/                             Ignored scratch area
```

The historical main-report filename is retained to preserve existing links. It now contains all five chapter headings, with Chapters 4–5 transparently documenting the lack of data. The standalone questionnaire is the authoritative source for the generated appendix.

## Privacy and GitHub delivery

Commit only report sources, code, tests, and documentation. Participant responses, contact details, code linkages, credentials, and exports belong outside this repository or in ignored local `private/`, `data/`, or `responses/` folders. Ignore rules reduce accidents but do not replace staged-diff review. Generated HTML is rebuilt locally.

The intended GitHub repository is private. The initial audit found no repository or remote. Upload uses the existing authenticated GitHub account when permissions permit. A collaborator invitation requires a known collaborator username; no username is inferred from a relative's relationship.

## Limitations and future improvements

The unknown institution requirements, respondent access, external questionnaire review, pilot, justified sample target, and collected data prevent empirical completion. Perceptions cannot establish causal effects, verified financial savings, or sector-wide adoption rates. Future work is genuine review and collection, followed by measurement assessment and analysis appropriate to organisational dependence. Final institution formatting can be applied when requirements are known. The current build does not collect surveys or compute statistical findings.
