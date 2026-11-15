# OECD exploratory regression outputs

See the [regression summary](../oecd-regression-summary.md) for the survey scope, model outcomes and interpretation.

Each model has an odds-ratio table and forest plot, a variance inflation factor table, an in-sample calibration table and plot, and a JSON summary with internal holdout metrics. These unweighted HC1 models are exploratory.

Publication copies omit raw records and response-code audits. Calibration bins are merged where either outcome class has fewer than 10 observations. Fitted-probability cutpoints and detailed exclusion counts are omitted. Where any predictor category has fewer than 10 observations in either outcome class, all terms for that predictor and the model intercept are omitted from the publication coefficient output. The underlying fits are unchanged.

- M3_worker_performance omits reported terms for employeeagecat2.

- M4_decision_assistance omits reported terms for employeerole.

OECD (2022), Microdata from the OECD AI surveys of employers and workers. Available via: https://www.oecd.org/future-of-work/reports-and-data/data-infographics.htm

Results and their interpretation are the sole responsibility of the author(s). The opinions expressed and arguments employed herein do not necessarily reflect the official views of the OECD or its Member countries.
