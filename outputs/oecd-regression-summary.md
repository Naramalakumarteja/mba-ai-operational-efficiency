# OECD workplace AI regression summary

Five exploratory binary logistic regressions use separate 2022 OECD employer and worker surveys covering manufacturing and finance and insurance in Austria, Canada, France, Germany, Ireland, the United Kingdom, and the United States.

| Model | Outcome | Complete cases | Holdout AUC |
|---|---|---:|---:|
| M1 | Employer-reported AI adoption | 1,991 | 0.609 |
| M2 | Perceived productivity increase among AI-adopting employers | 687 | 0.580 |
| M3 | Perceived performance improvement among workers using AI | 1,987 | 0.682 |
| M4 | Reported decision assistance among workers using AI | 1,974 | 0.664 |
| M5 | Employer-reported high costs as an AI adoption barrier | 1,920 | 0.531 |

Models use complete cases, unweighted estimates and independent-observation HC1 standard errors. Holdout AUC describes how well the models distinguish outcomes in an internal test split. The results describe associations in survey reports and do not establish causality or support complex-survey population inference.

OECD (2022), Microdata from the OECD AI surveys of employers and workers. Available via: https://www.oecd.org/future-of-work/reports-and-data/data-infographics.htm

Results and their interpretation are the sole responsibility of the author(s). The opinions expressed and arguments employed herein do not necessarily reflect the official views of the OECD or its Member countries.

[View regression tables, plots and diagnostics](oecd-regressions/README.md).
