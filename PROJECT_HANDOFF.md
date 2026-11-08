# Project handoff

Prepared 8 November 2026 from the available conversation, current project files and a read-only repository inspection. This document intentionally excludes credentials, private application details, respondent records and unnecessary personal information.

## 1. Read this first

There are two independent research versions in this repository:

1. **Preserved OECD descriptive study:** Workplace AI Adoption, Perceived Performance and Implementation Barriers: A Comparative Secondary Analysis of OECD Employer and Worker Surveys.
2. **Newer regression study:** AI Use at Work, examining developers' AI adoption, reported agent productivity, debugging frustration, complex-task ratings and trust using Stack Overflow Developer Survey 2025.

Do not pool their data, substitute one population for the other, or describe either as a survey conducted by this project. The initial Chennai-manager primary-survey proposal was not collected and is archived. Operations Management remains the intended MBA domain; Data Analytics supplies the analytical methodology. Supervisor acceptance of the revised developer-focused scope has not been established.

Evidence labels used below:

- **File-verified:** observed in the current repository or stored outputs during handoff preparation. Stored results were inspected, not recalculated.
- **Previously reported:** established in earlier available conversation, not independently repeated during this handoff.
- **Pending/unknown:** requires external evidence or further verification.

No experiments, model fitting, builds or tests were run to prepare this handoff. Existing project files were not edited.

## 2. Objectives, scope and research decisions

### OECD version

The source is a genuine OECD employer/worker survey, fielded in 2022 and published in 2023. The user supplied the published PDF and supplementary Excel workbook. Original coverage: Austria, Canada, France, Germany, Ireland, United Kingdom and United States; manufacturing and finance/insurance. The source study reports 2,053 firms and 5,334 workers; these are original-study counts, not project recruitment totals.

The project processes selected published weighted estimates. It compares adoption by sector/firm size, perceived performance, task changes, pace/control, decision assistance and implementation barriers. Employer and worker populations are separate and cannot be linked as paired observations. Subgroup counts are unweighted source labels, not reconstructed weighted response counts. Seven-country coverage does not create seven independent country observations for each displayed sector estimate.

Decision: do not fit respondent-level regressions to these aggregates. The extracted rows represent different questions and eligible populations, not interchangeable individual records. One finance cost-motivation distribution totals 94%; it is disclosed and excluded rather than silently normalized.

### Stack Overflow version

Decision: use genuine public respondent-level data to perform an independent, revised empirical analysis without depending on OECD restricted-data approval. This changes the population and objectives; it does not fulfill the original Chennai sampling plan or establish decision-making/cost-saving outcomes that were not measured.

Stored audit identifies 49,191 archive records, 37,467 professional developers and an employed-professional-developer cohort of 28,774. Current tool users in that cohort: 16,670; current agent users: 6,117. These are overlapping eligibility groups, not a sequential participant recruitment flow.

The publisher headline is 49,009 analysed responses. The 182-record difference remains unexplained. Do not delete records merely to match that headline. The survey is voluntary and is not representative evidence for all employees, Chennai managers, India or all seven OECD countries.

Five exploratory binary logistic models use model-specific eligibility and complete cases. Adjustments include grouped experience, organisation size and country; user models include use frequency. Monthly use is the primary frequency reference, and under five years is the main experience reference. Missing or ineligible outcomes are not automatically coded as negative outcomes. Contradictory responses receive explicit handling in the analysis code.

## 3. Current file map

| Path | Purpose and cautions |
|---|---|
| `README.md` | Entry point; introduces the regression study, followed by extensive preserved OECD instructions. |
| `research_pipeline.py` | OECD source validation, extraction, descriptive calculations and report generation. |
| `build_report.py` | Runs the OECD build, dashboard/explainer work and submission packaging. Does not fit the independent regression models. |
| `stackoverflow_analysis.py` | Stack Overflow coding, eligibility, five regressions, sensitivity model, diagnostics and result exports. |
| `requirements.txt` | OECD dependencies. |
| `requirements-stackoverflow.txt` | Regression, document and chart dependencies. |
| `sources/` | Preserved OECD PDF, workbook and source manifest. |
| `results/` | OECD observations, comparisons, analysis, data-quality and verification outputs. |
| `report/PROJECT_REPORT.*` | Preserved OECD Markdown, HTML and PDF report. |
| `figures/` | Original OECD SVG charts. |
| `references/REFERENCES.md` | Preserved source references; not necessarily the full bibliography of every newer deliverable. |
| `explanation/` | Project explanation material. |
| `assets/` | Includes the supplied VIT logo used in the revised report. |
| `scripts/download_stackoverflow.py` | Downloads the exact public CSV/schema and checks SHA-256 hashes. |
| `scripts/build_stackoverflow_report.py` | Builds revised report artifacts using a supplied DOCX template and existing analysis outputs. |
| `scripts/build_research_figures.py` | Builds five separate OECD-context PNGs and two regression PNGs from existing results. Recent local, untracked addition at inspection. |
| `scripts/build_dashboard.py` | Rebuilds offline OECD comparison dashboard. |
| `scripts/build_explainer.py` | Builds explanation page with browser read-aloud controls. |
| `tests/` | Active OECD and Stack Overflow checks. Some regression checks skip when dependencies or downloaded data are absent. |
| `outputs/stackoverflow2025/` | Main revised DOCX/PDF/HTML, analysis audit, primary/full coefficient tables, model-row extracts, calibration tables, descriptive counts, questionnaire extract and seven PNG charts. |
| `outputs/AI_Comparison_Dashboard.html` | Offline OECD comparison interface; not a regression dashboard. |
| `outputs/Project_Complete_Explainer.html` | Standalone explanation with browser speech; voice availability depends on device/browser. |
| `outputs/AI_Use_at_Work_Updated_Review.pptx` | Newer 12-slide editable presentation adaptation; local untracked artifact at inspection. |
| `outputs/VIT_Project_Updated_Report_and_Presentation.zip` | Combined current/previous deliverables; local untracked artifact at inspection. |
| `outputs/Stack_Overflow_2025_Regression_Package.zip` | Regression submission package. |
| `outputs/MBA_Secondary_Data_Submission_Package.zip` | Broader package, including preserved OECD work and optional newer artifacts. |
| `Databricks_OECD_Analysis.py` | Databricks notebook for the OECD workflow, not a verified cloud regression deployment. |
| `DATABRICKS_SETUP.md` | Workspace/Git-folder instructions. Requested project folder spelling is exactly **Buisness projects**. |
| `SUBMISSION_BLOCKERS.md`, `SUBMISSION_HANDOFF.md`, `FINAL_SUBMISSION_STATUS.md` | Earlier OECD-oriented status documents; do not treat them as complete current regression release status. |
| `archive/chennai_primary/` | Historical primary-survey proposal, questionnaire, import infrastructure and tests. Not evidence of collected responses. |
| `work/` | Ignored downloads, local environments, build helpers and review material. Not included in a normal Git checkout. |
| `private/` | Ignored private material. Do not publish or reproduce its contents in handoffs. |

Other earlier presentations and a viva guide remain under `outputs/`; filenames alone do not establish which version is approved. Original Keynote documents were preserved, not natively edited/exported on Windows.

## 4. Completed work and stored results

### File-verified OECD outputs

`results/VERIFICATION.json` records a nine-page generated PDF, 152 extracted estimates, 36 distribution checks, one excluded source item and passing internal HTML/chart-link/PDF-text checks. These are stored software checks, not institutional validation. Earlier work reports 35 of 36 distributions passing, with the known excluded item accounting for the remaining check. `sector_comparisons.csv` contains 16 comparisons.

Examples: published adoption is 41.7% in finance/insurance and 29.0% in manufacturing. Positive employer productivity perceptions are 56.7% and 62.6%, respectively. These have different eligible denominators and must not be presented as directly measured productivity gains.

### File-verified regression outputs

The following are saved estimates in `outputs/stackoverflow2025/primary_results.csv`, not models rerun for this handoff:

| Model and nominated comparison | Complete-case n | Adjusted odds ratio | Pointwise 95% CI |
|---|---:|---:|---:|
| M1 adoption: 20+ vs under 5 years' experience | 19,773 | 0.591 | 0.525–0.665 |
| M2 reported agent productivity: daily vs monthly agent use | 5,383 | 7.999 | 6.769–9.453 |
| M3 debugging frustration: daily vs monthly AI-tool use | 14,947 | 0.801 | 0.731–0.878 |
| M4 favourable complex-task rating: daily vs monthly AI-tool use | 15,143 | 5.024 | 4.413–5.720 |
| M5 favourable trust: daily vs monthly AI-tool use | 15,939 | 5.099 | 4.534–5.734 |

All five saved primary Holm-adjusted p-values are below .001. Correction covers five nominated primary contrasts, not every exploratory coefficient. Confidence intervals are pointwise, not simultaneous. An odds ratio of eight does not mean eight times the productivity or eight times the probability.

Analysis uses explicit HC1 sandwich covariance with n/(n-k) correction. Earlier implementation identified a library-label issue in which GLM HC1 matched HC0; do not replace the explicit correction without checking its implementation. Stored diagnostics include convergence, VIF, GLM-versus-Logit agreement and in-sample calibration/discrimination. In-sample checks are not external predictive validation.

Previously reported sensitivity analysis excluding neutral productivity ratings used n=4,505 and OR approximately 12.59 versus 8.00 in the main model. Direction was stable but magnitude depends materially on coding. Do not hide this distinction.

### Previously reported delivery checks

- 23 tests passed in the later combined workflow: 15 OECD and eight Stack Overflow checks. Earlier references to 38 tests concern an older project stage and must not be used as the latest verified count.
- A 17-page revised report included seven charts plus the supplied logo; a 12-slide PowerPoint was rendered and checked.
- Dashboard checks and presentation/layout verification were previously reported. They were not repeated during handoff preparation.
- Combined ZIP included both old OECD context and new regression outputs, clearly separated.

## 5. Git and publication state

File-verified at inspection:

- Branch: `main`.
- HEAD: `818f1d867a1cab9eafacfab6ddd7ce7d58b4e6db`.
- HEAD subject: `Use public VIT GitHub repository in report and project instructions`.
- Configured `origin`: `https://github.com/Naramalakumarteja/mba-ai-operational-efficiency.git`.
- Intended public VIT repository: `https://github.com/saisri132000/mba-ai-operational-efficiency`.

These are separate repositories with separate history. Previously reported public snapshot commit was `380f453940f6d123e8f9e62f6609f69706e8c9cb`; its present remote state was not rechecked for this handoff. Earlier CLI access could push the original repository but only read the cousin's public repository; public updates used the authenticated browser. Do not assume those permissions remain unchanged.

The working tree was already dirty before this handoff. Modified tracked paths included `build_report.py`, both main submission ZIPs, revised regression DOCX/HTML/PDF/README, `requirements-stackoverflow.txt` and `scripts/build_stackoverflow_report.py`. Untracked paths included the newer presentation, combined ZIP, seven-chart folder, chart builder, earlier reconstructed presentations and viva guide. These are existing user work; do not discard, overwrite or silently stage it.

Consequently, a fresh GitHub checkout may omit the latest local charts, presentation and package revisions. No fresh checkout, push, remote synchronization or clean-tree claim is established by this handoff. Creating this file adds another untracked file; no commit or push is authorized by its creation.

## 6. Environment and reproduction instructions

Commands below are instructions for a future authorized run; they were not executed for this handoff. Run from the repository root. Use a clean environment and inspect dependency compatibility rather than assuming every pinned version works on every runtime.

The stored regression audit records Python 3.12.14. OECD documentation says Python 3.10+, which is not proof that the newer regression dependency set supports every such version. Existing authoring used Windows, Word COM for DOCX-to-PDF export and bundled tooling; Cloud does not inherit those facilities.

### Setup

```sh
python -m venv .venv
```

Activate `.venv` with the platform's standard command, or invoke `.venv/bin/python` on Linux/macOS and `.venv\Scripts\python` on Windows.

OECD dependencies: openpyxl 3.1.5, reportlab 4.4.9, pypdf 6.10.0.

```sh
python -m pip install -r requirements.txt
python build_report.py
python -m unittest discover -s tests -v
```

Regression dependencies: numpy 2.3.5, pandas 3.0.1, scipy 1.18.1, statsmodels 0.15.0, python-docx 1.2.0 and matplotlib 3.11.2.

```sh
python -m pip install -r requirements-stackoverflow.txt
python scripts/download_stackoverflow.py
python stackoverflow_analysis.py
python -m unittest discover -s tests -p test_stackoverflow_analysis.py -v
python scripts/build_research_figures.py
python scripts/build_stackoverflow_report.py --template outputs/stackoverflow2025/AI_Use_at_Work_Regression_Report.docx
```

Inspect the report builder before relying on PDF production in Cloud; Windows Word is not available there, and previous local LibreOffice rendering attempts lacked an installed LibreOffice executable. A DOCX build alone does not establish a freshly rendered PDF. Do not mark success based solely on an old output file remaining on disk.

The chart builder is currently untracked and may be missing from a remote checkout. The OECD release builder can package optional existing regression outputs but does not refit them. Newer deck/combined-package authoring helpers lived under ignored `work/`; complete clean-checkout regeneration of those deliverables is not established. Do not claim a committed presentation build command exists without inspecting the checkout.

### Data provenance

Public CSV: `https://media.githubusercontent.com/media/StackExchange/Survey/main/packages/archive/2025/results.csv`.

Public schema: same directory, `schema.csv`.

Downloader destination: `work/stackoverflow_2025/`. Analysis defaults to those files and writes to `outputs/stackoverflow2025/`. It also accepts `--data`, `--schema` and `--output` paths.

Expected SHA-256 values in the saved audit:

```text
results.csv  2d1f65308877282edfb4470520eabbc08cb499118432a3dcec6a66c086aa2baa
schema.csv   1d24951e04eab46c6f9fecef6ce8e6b32a0a14a3f0eecdcf62f70833a74b3ff8
```

Source changes should trigger review, not silent hash replacement. These public-file hashes are identifiers, not credentials.

HTML reports and dashboard can be opened locally. Browser speech is optional and device dependent. No database, API key or Databricks service is required for local analysis. Databricks cloud execution remains unverified; the existing notebook addresses the OECD workflow. A previously supplied workspace URL is not evidence of a successful run.

## 7. Academic status, known issues and remaining work

1. **Scope acceptance pending:** obtain supervisor confirmation for the developer-focused secondary study and real institutional requirements. Do not invent a handbook, approval, pilot validation or signed declaration.
2. **Submission-version choice pending:** distinguish the newer regression report from the user's supplied OECD-only Word draft. The latter explicitly excludes regression. User previously asked to leave matching issues aside while viewing graphs; that did not resolve submission consistency.
3. **Supplied Word draft review:** incorrect manual contents-page numbers, list headings after their tables, 15-versus-16 indicator wording, an old repository link, unfinished reference-check wording and a contents-listed checklist absent from the body were identified. They were reviewed only, not fixed. Keep this distinct from claims about the generated regression report.
4. **Documentation drift:** root status/blocker files still describe the OECD-only version, and some Git/Databricks wording is historical. Consult actual code, results and Git state before following older instructions.
5. **Publication pending:** latest local revisions are not established as committed or present in the public repository. Audit changes, secrets and package contents before any separately authorized release.
6. **Reproducibility gaps:** report PDF rendering and deck/combined-package generation need a documented portable route if complete Codex Cloud regeneration is required. Do not modify them unless requested.
7. **Statistical limits:** no causal identification, random sample, measured productivity gain, realized cost savings or representative Chennai findings. Missingness, model-specific selection, coding sensitivity and self-report bias remain material. Model samples overlap.
8. **External inputs:** supervisor scope acceptance, institutional format, required formalities/signatures and any required source-access authorization remain external. Genuine primary questionnaires are not prerequisites for the current secondary study.

Recommended future order: establish the accepted submission version; inspect current local changes and corresponding remote content; reconcile relevant report text and references; preserve existing results/provenance; rerun only checks justified by authorized changes; render and inspect deliverables; release only when explicitly requested. Optional probability charts, missing-data flow and sensitivity visualizations were recommended but not authorized or implemented by that recommendation alone.

## 8. OECD access, licensing and correspondence

The published report/workbook are distinct from restricted respondent-level microdata. Current OECD code reads local public tables; it does not call a live OECD API or scrape respondent records. Public availability does not remove attribution or source-specific reuse conditions. Do not automatically label the 2023 report with a later default Creative Commons licence.

Stack Overflow source attribution and applicable ODbL/DbCL notices must be retained. Public response identifiers must not be used to identify people. Do not copy model-row extracts into this handoff.

OECD restricted microdata approval and institutional authorization are not established. Prior OECD correspondence clarified possible institutional arrangements, but clarification is not approval. Do not assume restricted data may be uploaded to GitHub, Databricks or AI services. Review actual approval terms first.

Most recent correspondence action: a clarification email asking whether electronic signatures are accepted or a handwritten-signed scanned PDF is required was sent to the OECD survey contact, with a tool-confirmed SENT result. No subsequent reply has been checked. Do not resend automatically or treat either signature method as accepted until confirmed. Applicant names, application links and private institutional details are deliberately omitted here.

## 9. User constraints and Cloud continuation checklist

- Be concise and mindful of token use; prioritize useful implementation over unnecessary documents or features.
- Never fabricate data, responses, participant numbers, citations, statistical findings, approvals or institutional requirements.
- Preserve working architecture, names, assets and outputs. Inspect before changes; fix genuine problems rather than redesigning without authorization.
- Distinguish actual completed work, planned analysis, historical verification and pending empirical/institutional evidence.
- Do not force regression into every objective. Use models supported by actual variables and eligible records.
- Do not confuse OECD aggregates, Stack Overflow respondents and archived Chennai plans.
- Do not publish secrets, credentials, environment files, private applications or personal information. Keep ignored working/private material out of release packages.
- For email, the user explicitly requested opening a fresh tab and asking them to log in or confirm the sending account. An email action requires explicit authorization; previous permission to send one message is not permission to send others.
- Use the cousin's public repository link in VIT-facing material where appropriate; do not assume local `origin` points there or that authentication permits pushing to it.
- Latest authorization is **only to create this handoff file**. Do not alter other files, commit, push or change branches as part of this task.

A new Codex Cloud conversation should first read this document, `README.md`, `outputs/stackoverflow2025/README.md`, relevant source code and Git status. Verify which uncommitted local files actually reached the Cloud checkout. Read applicable repository instructions if present; none were listed among tracked AGENTS.md files during this inspection. Obtain needed artifacts through authorized means instead of inventing missing content. Treat conversation history as context, not proof of current remote state. Ask before resolving genuinely ambiguous submission scope, but continue independent authorized work when possible.

This handoff is a status/provenance document, not an institutional approval, a fresh test certificate or evidence that the dissertation is ready for final submission.
