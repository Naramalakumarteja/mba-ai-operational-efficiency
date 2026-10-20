# Workplace AI Adoption, Perceived Performance and Implementation Barriers

**A comparative secondary analysis of OECD employer and worker surveys.**

Operations Management is the primary domain; descriptive Data Analytics is the method. The project reads genuine published OECD aggregates from 2022 fieldwork, checks them, compares finance/insurance and manufacturing, and generates a five-chapter report, charts, explanation page with read-aloud controls, and a submission ZIP.

## Evidence and boundaries

This is the canonical project. It replaces the uncollected Chennai primary-survey design, which is preserved under `archive/chennai_primary/` for history only. The GitHub repository retains its historical name; that name does not define the current population.

- Inputs: unchanged OECD PDF and supplementary workbook in `sources/`.
- Population: seven OECD countries, finance/insurance and manufacturing; not Chennai or India.
- Unit: published sector/firm-size response estimates, not individual records.
- Outputs: weighted percentages and descriptive percentage-point comparisons.
- No causal claims, objective savings, significance tests, or primary questionnaire collection.
- A finance cost-motivation distribution totals 94%; it is disclosed and excluded from comparisons.

## Questions answered

1. How does published AI adoption differ by sector and firm size?
2. What productivity and performance perceptions do the relevant employers/workers report?
3. What task changes, pace, and control are reported?
4. How prevalent is decision assistance, and what do assisted workers report about it?
5. What cost and skill barriers do employers report?

## Local setup and run

Python 3.10+:

```sh
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python build_report.py
.venv\Scripts\python -m unittest discover -s tests -v
```

macOS/Linux: use `.venv/bin/python` in the same commands. No environment variables, credentials, database, or API service are required. The three pinned libraries read Excel, generate PDF, and check PDF output. Standard-library code generates the CSV/JSON, SVG, HTML, and ZIP. Builds verify source SHA-256 hashes before reading the workbook.

## Databricks

Use **Buisness projects** as the folder inside your new Databricks workspace. Follow [DATABRICKS_SETUP.md](DATABRICKS_SETUP.md), clone this private repository there, and open `Databricks_OECD_Analysis.py`. It installs the same dependencies, runs the same pipeline, and displays the generated report inline. No Windows wheels or private tokens are committed. Cloud execution must be verified in your actual workspace; local tests do not certify Databricks execution.

## Outputs

| File/folder | Purpose |
|---|---|
| `report/PROJECT_REPORT.pdf` | Print-ready five-chapter report |
| `report/PROJECT_REPORT.html` | Navigable report; keep `figures/` beside `report/` |
| `report/PROJECT_REPORT.md` | Generated report text |
| `outputs/Project_Complete_Explainer.html` | Standalone interactive explanation with optional browser speech |
| `outputs/MBA_Secondary_Data_Submission_Package.zip` | Portable current package, including notebook and explainer |
| `results/observations.csv` | 152 source-traceable published estimates, not participants |
| `results/sector_comparisons.csv` | 16 descriptive comparisons |
| `results/data_quality.json` | Distribution checks and the excluded item |
| `results/VERIFICATION.json` | Build checks, not institutional approval |
| `figures/`, `references/`, `explanation/` | Charts, original source references, presentation/viva guide |

Open the HTML files directly in a browser. Available read-aloud voices depend on browser/device; some voices need a network connection.

## Architecture and reproducibility

`sources/` → `research_pipeline.py` → validation → descriptive calculations → `results/` + `figures/` + `report/` → `scripts/build_explainer.py` → ZIP via `build_report.py`.

The workbook remains unchanged. Proportions are multiplied by 100. Relevant answer categories are summed explicitly. Sector differences are manufacturing minus finance in percentage points. Original unweighted subgroup sizes are labels, not reconstructed weighted response counts. Existing source inconsistencies are never silently normalized. The builder checks required source cells and response totals, then records source hashes and results.

The active test suite covers source integrity, calculated values, source-quality handling, report/HTML structure, package contents, and notebook structure. Historical tests remain in the archived primary project. Generated PDF metadata can differ between builds; analysis values and source hashes are reproducible.

## Submission status and limitations

The descriptive secondary report and software are implemented. This is a bounded comparison of published survey findings, not a new causal study or comprehensive literature review. The references comprise the original report and supplementary workbook. Institution acceptance, identity details, declarations, signatures, and required formatting remain external. See [FINAL_SUBMISSION_STATUS.md](FINAL_SUBMISSION_STATUS.md) and [SUBMISSION_BLOCKERS.md](SUBMISSION_BLOCKERS.md).

Source: Lane, Williams, & Broecke (2023), OECD Working Paper No. 288, [DOI](https://doi.org/10.1787/ea0a0fe1-en), and its supplied supplementary workbook. OECD source rights and attribution remain applicable.
