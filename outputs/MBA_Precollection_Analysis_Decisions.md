# Pre-collection analysis decisions

**Draft v0.1 — 1 October 2026**

This is a working protocol, not a registered study or a completed analysis. Freeze final decisions before main collection after the pilot and access audit. Any subsequent changes must be dated, justified, and distinguished from the original plan.

## Research model

Primary exposure: A02, AI-use frequency over the whole preceding six months, ordinal 0–4. Four separate outcomes are proposed: productivity, process efficiency, cost optimization, and managerial decision effectiveness. Outcome scores remain conditional on conceptual and measurement support. Coverage A03 and integration A04 are secondary adoption descriptors. No causal chain, mediation model, or grand efficiency score is specified.

## Record inclusion

Include eligible, consenting main-study unit records. Pilot and routing-test records are excluded from the main dataset. Retain the first eligible submission for a duplicate unit. If it is unusable, document the reason before considering the next eligible submission. Do not select records based on favourable answers. Preserve an exclusion log with counts and reasons.

Uncertain geographic, activity, or sector eligibility must be resolved before inclusion. Unknown adoption does not disqualify an otherwise eligible record from clearly labelled outcome descriptions, but excludes it from adoption-association analyses. Unknown cost knowledge produces cost-domain missingness only.

## Adoption coding

A02: Never=0; less than monthly=1; monthly but less than weekly=2; weekly but less than daily=3; daily/almost daily=4. Treat as ordinal; do not describe one category change as an equal increase in use.

For A01=No, zero-use descriptors may be derived only from the explicit confirmed non-use route. For A01=Unknown, adoption descriptors remain unknown. Contradictions or ambiguous tool descriptions are flagged; if not resolvable without guessing, adoption is unclassified for association analysis. A missing optional tool example alone does not establish misclassification. Changing integration is a non-scored category for A04. First-use timing and stopped use are reported separately from frequency.

## Outcome scoring

Primary scoring rule: a three-item domain mean requires all three valid 1–5 responses and defensible domain coherence. Report domain-specific sample counts. Two-of-three means may be examined in a labelled sensitivity analysis. No mean imputation across respondents, and no midpoint substitution for unknown responses. Cost results concern the cost-informed subgroup; discuss how its composition differs from the broader sample.

If a domain cannot be supported, report its items descriptively rather than choose the item with the best association. Document any reformulation before main collection where possible. A high alpha alone is not evidence of adequate construct coverage or distinctiveness. Three-item domains provide limited evidence for broader measurement claims.

## Descriptive reporting

Report recruitment flow, known invitation denominators, eligibility exclusions, duplicate counts, retained organisations and units, operational activity, role, tenure, headcount, adoption categories, and unknown-response rates. Report item distributions and medians/interquartile ranges where useful. Percentages require clearly stated denominators. The sample adoption proportion is not Chennai-sector prevalence.

## Primary associational analysis

Proposed estimate: Spearman correlation between A02 and each supported domain mean. All four tests are two-sided. If defensible inferential procedures are available, apply Holm adjustment across the four prespecified outcomes. If an outcome is not estimable, report it as untested; for a conservative implementation retain the original family of four by treating untested comparisons as p=1 for adjustment only, without presenting a fabricated observed p-value.

Report effect magnitude and appropriate uncertainty alongside any tests. The final interval method and handling of ordinal ties and organisation dependence remain to be specified based on the access design. No ordinary individual-row bootstrap or independent-observation significance test is automatically authorised for multiple units from the same organisation. With too few organisations for reliable dependence handling, descriptive associations may be more defensible than confirmatory significance claims.

Do not interpret a non-significant result as proof of zero association. Do not interpret a small adjusted p-value as proof of operational importance, causality, or sample representativeness.

## Secondary and sensitivity analysis

- A03 and A04 associations: exploratory; report their missingness and avoid selective significance reporting.
- Recent-adopter and discontinued-use patterns: describe exposure differences. Any exclusion sensitivity must be labelled and retain the original primary analysis.
- Outcome means with two valid items: compare cautiously with complete-item results if justified.
- Organisation concentration: report how much the sample depends on its largest contributors; do not treat removal of an inconvenient organisation as a new primary result.
- Adjusted models: optional only if sample and design support them. Unit size and activity are the proposed minimal contextual variables; do not choose controls by p-values.

## Decisions still open

The sample target, stopping dates, actual organisation spread, smallest useful association, interval method, measurement evaluation feasible at achieved N, confidentiality retention period, and final platform are not known. This protocol records those gaps; it does not fill them with assumptions presented as fact.

## Claims permitted by this design

Example: “In the sampled units with complete responses, reported AI-use frequency was associated with perceived process efficiency.” Add the estimate and uncertainty when real data exist.

Claims such as “AI caused savings,” “Chennai firms became more productive,” or “AI adoption is X% across the sector” are unsupported by this design. A six-month recall period does not make the study longitudinal.
